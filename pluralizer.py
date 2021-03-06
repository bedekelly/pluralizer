"""
pluralizer: A Lambda handler to pluralize (or not) a noun.
"""
from lambda_utils import bad_request

O_EXCEPTIONS = [
    "canto",
    "hetero",
    "photo",
    "zero",
    "piano",
    "portico",
    "pro",
    "quarto",
    "kimono",
]


def pluralize(noun):
    """Given a noun, make it a plural."""
    normal_noun = noun.lower().strip()
    for ending in ("ss", "o", "ge", "tch"):
        if normal_noun.endswith(ending) and normal_noun not in O_EXCEPTIONS:
            return noun + "es"
    if normal_noun.endswith("y") and normal_noun[-2] not in "aeiou":
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
    if not isinstance(noun, (str, unicode)):
        raise bad_request("noun must be a string")

    return {
        "result": maybe_pluralize(noun, quantity)
    }
