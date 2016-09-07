"""
pluralizer: A Lambda handler to pluralize (or not) a noun.

"""

from pprint import pprint


def pluralize(noun):
    """Given a noun, make it a plural."""
    if noun.endswith("y"):
        return noun[:-1] + "ies"
    return noun + "s"


def maybe_pluralize(noun, quantity):
    """
    Given a noun and number of occurrences, potentially make the noun a
    plural.
    """
    if quantity == 1:
        return noun
    return pluralize(noun)


def pluralize_handler(event, context):
    """
    Given an "event", extract the noun and quantity and return the result
    of pluralizing the noun.
    """
    try:
        noun = event["noun"]
        quantity = event["quantity"]
    except KeyError as e:
        raise ValueError("Bad Request: noun or quantity not provided.")
    return maybe_pluralize(noun, quantity)
