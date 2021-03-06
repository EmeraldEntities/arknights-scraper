"""A basic Operator class that can be created for parsing/testing
that stores some essential information about each Operator."""

import sys


class Operator:
    """The class for creating Operator objects, which stores information
    about Operators.

    This solely exists so that operator information can be
    held in a convienient location, and can be reused for other
    future features.

    Public variables:

    name -- string,

    rarity -- int,

    profession -- string,

    description -- list,

    tags -- list,

    stats -- dict

    Public methods:

    set_property(property, value)

    get_property(property)

    get_all_properties()

    has_property(property)

    get_formatted_tags()

    has_stats()

    """

    def __init__(
            self,
            name,
            rarity,
            profession,
            description=None,
            tags=None
    ):
        """Initializes an Operator object.

        Keyword arguments:

        name -- string, the name of the operator

        rarity -- int, the rarity of the operator as a number
        (5 star = 5, etc.)

        profession -- string, what class the operator is

        description -- list, a list containing the description strings
        of an operator (default: None)

        tags -- list, a list containing the tags of this operator
        (default: None)
        """

        self.name = name
        self.rarity = rarity
        self.profession = profession
        self.description = (
            description
            if description is not None
            else ["No description available!"]
        )
        self.tags = (
            tags
            if tags is not None
            else ["No tags available!"]
        )

        self.stats = {}
        self._properties = {}

    def set_property(self, prop, value):
        """Set the specified property of this operator to a value.

        If the value already exists, this method will assume the
        value is a list and append the provided value
        to the existing value.
        """
        if prop in self._properties.keys():
            # We're assuming all property stuff are in arrays
            self._properties[prop].append(value)
        else:
            self._properties[prop] = value

    def get_property(self, prop):
        """Return the specified property of this operator, which is
        normally a list, if it has it. Return None otherwise."""
        if self.has_property(prop):
            return self._properties[prop]
        else:
            return None

    def get_all_properties(self):
        """Return all the stored property names as a list."""
        return self._properties.keys()

    def has_property(self, prop):
        """Checks to see if this Operator has a property. True if so, False otherwise."""
        if prop in self._properties.keys():
            return True

        return False

    def get_formatted_tags(self):
        """Retrieves all the tags that this Operator has, formatted into a string."""
        tag_string = ""
        for tag in self.tags:
            tag_string += tag + "     "

        return tag_string

    # I don't like this, but this is so that we don't need to load in
    # stats for the operator every single time we want them...
    @property
    def stats(self):
        """Retrieves all this Operator's stats."""
        return self._stats

    @stats.setter
    def stats(self, other_stats):
        """Sets this Operator's stats to a provided parameter."""
        self._stats = other_stats

    def has_stats(self):
        """Checks to see if this Operator has stats set or not."""
        return self.stats != {} and not self.stats is None


if __name__ == "__main__":
    sys.stdout.write(
        "Wrong python file to run! The main file to run is `ark.py`.\n\n"
    )
