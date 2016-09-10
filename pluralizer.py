"""
pluralizer: A Lambda handler to pluralize (or not) a noun.
"""


class BadRequest(Exception):
    """Stub class to stop any bad request raising just a plain Exception."""


def bad_request(message):
    """Utility to return a BadRequest error with the given message."""
    return BadRequest("Bad Request: {}".format(message))


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
        raise bad_request("{} not given".format(str(e)))

    if noun == "":
        raise bad_request("noun is empty")
    if not isinstance(quantity, int):
        raise bad_request("quantity must be an integer")
    if not isinstance(noun, str):
        raise bad_request("noun must be a string")

    return {
        "result": maybe_pluralize(noun, quantity)
    }
