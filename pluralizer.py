"""
pluralizer: A Lambda handler to pluralize (or not) a noun.
"""


class LambdaException(Exception):
    """Stub class to stop any bad request raising just a plain Exception."""


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


def pluralize_handler(event, _=None):
    """
    Given an "event", extract the noun and quantity and return the result
    of pluralizing the noun.
    """
    try:
        noun = event["noun"]
        quantity = event["quantity"]
    except KeyError as e:
        raise LambdaException("Bad Request: {} not given".format(str(e)))

    if noun == "":
        raise LambdaException("Bad Request: noun is empty")
    if not isinstance(quantity, int):
        raise LambdaException("Bad Request: quantity must be an integer")

    return {
        "result": maybe_pluralize(noun, quantity)
    }
