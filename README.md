# arknights-scraper

A small scraper that uses gamepress.gg's easy URLs to find information about Arknights. For when you're too lazy to spin up your browser to find info on the newest operator.

Designed to be a pretty small, simple, and non-instrusive project. This program won't save any information. There may be some formatting errors!

Thanks, [gamepress.gg](https://gamepress.gg/)! :)

## Libraries used

- [requests](https://requests.readthedocs.io/en/master/) (to GET the data)
- [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) (to help parse through the data)
- [argparse](https://docs.python.org/3/library/argparse.html) (standard lib — so that command line works and is nice to work with)
- [re](https://docs.python.org/3/library/re.html) (standard lib regex — useful for working with strings)
- [json](https://docs.python.org/3/library/json.html) (standard lib — needed for working with JSON)
- [halo](http://halo.josealerma.com/index.html) (literally the best and most important library)

See requirements.txt for the versions of each library.

## Details

The only important file (and main file) is `scraper.py`. Everything other file contains functions or classes that are used by this program to format, retrieve data, etc.

Taken from the argparse -h command:

`python scraper.py [-h] [-s | -v] [-i] [-t] [-b] [-a] operator`

**Positional Arguments:**
- `operator` The operator you want information about. For spaces, use a '-' in place of the space. No special characters.

**Optional Arguments:**
- `-h, --help` show this help message and exit
- `-s, --skills` Displays the max tier of each of the specified operator's skills.
- `-v, --vskills` Stands for 'verbose skills'. Displays the 1st tier, 7th tier, and M3 (if possible) tier of each of the specified operator's skills.
- `-i, --info` Displays the specified operator's stats.
- `-t, --talent` Displays the specified operator's talent.
- `-b, --base` Displays the specified operator's base skills.
- `-a, --all` Displays all the information about this specified operator. Unless paired with the -v tag, this will only show the max tier of each skill this operator has.

## To-Do

- [x] ~~Add basic operator information~~
  - [x] ~~Add basic information~~
  - [x] ~~Add support for talents~~
  - [x] ~~Add support for skills~~
  - [x] ~~Add support for stats~~
  - [x] ~~Add support for base skills~~
- [ ] Add quality of life updates
  - [x] Add different skill levels, not just max?
  - [ ] Add support for upgrade information
  - [ ] Perhaps add support for calculating stages, etc?
- [ ] Add operator comparison?
- [ ] Add stage functionality?
- [ ] Add item descriptions?
- [ ] Add recruitment tag functionality?
- [ ] Add idk other functionality when needed
