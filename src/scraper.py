#!/usr/bin/env python3

import requests, argparse, sys, re
from halo import Halo # extremely important
from bs4 import BeautifulSoup

from operatorClasses.Operator import Operator
from detailedSearchFunctions import findTalents, findBaseSkills, createStatsJSON, parseStats, findSkills
from inputReader import readLinesIntoDict, readLineFromFile
from scraperFunctions import scrapeForOperator

# created 06/06/2020
# last edited: 03/07/2020
# version: 1.5.0
# author: Joseph Wang (EmeraldEntities)

### FUNCTIONS ########################
def initializeArguments():
  """Initializes cmd arguments and flags and returns the arguments."""
  # Using the argparse library, initializes cmd arguments
  parser = argparse.ArgumentParser(description="Find information about any operator in Arknights!")
  parser.add_argument("operator", help="The operator you want information for. For spaces, use a '-' in place of the space. No special characters.")
  parser.add_argument("-i", "--info", help="Displays the specified operator's stats.", action="store_true")
  parser.add_argument("-s", "--skills", help="Displays the specified operator's skills.", action="store_true")
  parser.add_argument("-t", "--talent", help="Displays the specified operator's talent.", action="store_true")
  parser.add_argument("-b", "--base", help="Displays the specified operator's base skills.", action="store_true")
  # parser.add_argument("-u", "--upgrades", help="Displays the specified operator's upgrade stages and what this operator needs. In-dev", action="store_true")
  
  parser.add_argument("-a", "--all", help="Displays all the information about this specified operator.", action="store_true")
  args = parser.parse_args()

  return args

def parseOperatorData(src, args):
  imagesDict = readLinesIntoDict("./info/imageToText.txt")
  jsonReplacementNames = readLinesIntoDict("./info/jsonOperatorReplacements.txt")

  soup = BeautifulSoup(src, "lxml")
  # soup = BeautifulSoup(open("debug.html", "r", encoding="utf-8"), "lxml") # debugging
    
  # Finding the default information that should be displayed for every operator
  # (eg. tags, description, etc.)
  tags = list(map(lambda souptxt: souptxt.text.strip(), soup.find_all("div", "tag-title")))

  # We can find the rarity of an operator by finding the div named rarity-cell and counting how
  # many images of stars are in it
  rarity = len(soup.find("div", "rarity-cell").find_all("img"))

  professionCell = soup.find("div", "profession-title")
  professionText = professionCell.text.strip()

  desc = soup.find_all("div", "description-box")

  descText = (["No proper description."] 
              if (len(desc) < 3) 
              else ["".join(desc[item].text).strip() + "\n" for item in range(3)])
  
  formattedName = args.operator.replace("-", " ").title()
  # Since the JSON I use to find stats may have another name for an operator, I have to 
  # convert any name to a good one
  properName = (formattedName
                if formattedName not in jsonReplacementNames.keys()
                else jsonReplacementNames[formattedName])

  stats = createStatsJSON(soup, properName)

  operator = Operator(properName, rarity, professionText, stats, descText, tags)
  # Any optional messages/properties are stored in operator.properties for convenience
  # and also to make sure that printing properties doesn't take 50 lines of code.
  # Also, we can reuse the properties this way as it is stored in a compact location.

  # Checking and calling the appropriate functions for optional flags
  # Taking advantage of python's functional programming paradigms to adhere to DRY principles
  #TODO: is this even good practice??? I'm trying to adhere to DRY principles but this makes me start to sweat
  conditionals = [
    ['skills'     , args.skills, findSkills,     [soup]]           ,
    ['talent'     , args.talent, findTalents   , [soup, imagesDict]],
    ['base skills', args.base  , findBaseSkills, [soup, imagesDict]],
  ]

  for prop, flag, findInfoFunction, arguments in conditionals:
    if flag or args.all:
      operator.setProperty(prop, findInfoFunction(*arguments))

  return operator

######################################

def main():
  spinner = Halo(text="Fetching...", spinner="dots", color="magenta")
  # Initialize the arguments for cmd purposes 
  args = initializeArguments()
  spinner.start()

  response = scrapeForOperator(args.operator) 

  if response != None:
    spinner.text = "Parsing..."
    spinner.colour = "yellow"
    operator = parseOperatorData(response.content, args)
    spinner.succeed("Success!")

    # Print out the results
    allProperties = [operator.getProperty(prop) for prop in operator.getAllProperties()]
    allMessages = [ parseStats(operator.getAllStats()) ] + allProperties

    sys.stdout.write("\n\n" + operator.name + "   ")
    sys.stdout.write("*" * operator.rarity + "   ") # Star rarity
    sys.stdout.write(operator.profession + "\n")

    sys.stdout.write(operator.getFormattedTags() + "\n\n")

    for descText in operator.description: 
      sys.stdout.write(descText)

    
    for prop in allMessages:
      for text in prop:
        sys.stdout.write(text + '\n') 

  else:
    spinner.fail("Failed.")
    sys.stdout.write("\n\n" + args.operator.replace("-", " ").title() + "\n")
    sys.stdout.write("\n" + "Could not find operator! Either the server is down, or your spelling is! \n")
    
  sys.stdout.write("\n\n")

if __name__ == "__main__":
  main()