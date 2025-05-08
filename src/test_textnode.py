import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Another text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_equal_different_type(self):
        node = TextNode("Text with URL", TextType.LINK, "https://example.com")
        node2 = TextNode("Text with URL",TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_not_equal_differnt_text_type(self):
        node = TextNode("Click here", TextType.LINK, "https://example.com")
        node2 = TextNode("Click here", TextType.BOLD, "https://example.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()