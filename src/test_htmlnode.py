import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_single(self):
        node = HTMLNode("a", "Click here", props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')

    def test_props_to_html_empty(self):
        node = HTMLNode("p", "Text", props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_none(self):
        node = HTMLNode("p", "Text")
        self.assertEqual(node.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()
