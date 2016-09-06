import unittest

from mock import patch

from pluralizer import pluralize, pluralize_handler, maybe_pluralize


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


if __name__ == "__main__":
    unittest.main()