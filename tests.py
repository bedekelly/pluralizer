import unittest

from mock import patch

from pluralizer import pluralize, maybe_pluralize, pluralize_handler, \
    LambdaException


class TestPluralizer(unittest.TestCase):
    """Test the functionality of the `pluralizer` file."""

    def test_pluralize(self):
        """
        The `pluralize` function should return the plural form of any noun.
        """
        self.assertEqual(
            pluralize("marker"),
            "markers"
        )

        self.assertEqual(
            pluralize("tree"),
            "trees"
        )
                      
        self.assertEqual(
            pluralize("story"),
            "stories"
        )

    def test_maybe_pluralize_one(self):
        """
        `pluralize` should not be called if `quantity` is 1.
        """
        unpluralized = maybe_pluralize("tree", 1)
        self.assertEqual(unpluralized, "tree")

    @patch("pluralizer.pluralize")
    def test_maybe_pluralize_many(self, pluralize_):
        """
        `pluralize` should be called in all other cases.
        """
        expected = pluralize_.return_value = "pluralize's return value"

        return_value = maybe_pluralize("tree", 2)
        self.assertEqual(return_value, expected)
        pluralize_.assert_called_once_with("tree")

    def test_pluralize_handler_no_noun(self):
        event = {"quantity": 10}
        self.assertRaises(
            LambdaException,
            lambda: pluralize_handler(event, None)
        )

    @patch("pluralizer.maybe_pluralize")
    def test_pluralize_handler_correct(self, maybe_pluralize):
        """
        When pluralize_handler is called correctly, check it delegates to
        maybe_pluralize and wraps the result in a dict accordingly.
        """
        event = {"quantity": 2, "noun": "strawberry"}
        result = pluralize_handler(event, None)
        maybe_pluralize.assert_called_once_with("strawberry", 2)
        self.assertEqual(
            result, {"result": maybe_pluralize.return_value}
        )
