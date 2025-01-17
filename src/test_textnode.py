import unittest

from textnode import TextNode, TextType, text_node_to_html_node, split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_text_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2)
    def test_link_eq(self):
        node1 = TextNode("This is a link to boot.dev", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("This is a link to boot.dev", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(node1, node2)
    def test_img_eq(self):
        node1 = TextNode("This is an image", TextType.IMAGE, "public/image.png")
        node2 = TextNode("This is an image", TextType.IMAGE, "public/image.png")
        self.assertEqual(node1, node2)
    def test_text_neq(self):
        node1 = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is another text node", TextType.TEXT)
        self.assertNotEqual(node1, node2)
    def test_mode_neq(self):
        node1 = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)
    def test_text_mode_neq(self):
        node1 = TextNode("This is a bold text node", TextType.BOLD)
        node2 = TextNode("This is an italic text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)
    def test_link_neq(self):
        node1 = TextNode("This is a link to boot.dev", TextType.LINK, "https://www.boot.dev/")
        node2 = TextNode("This is a link to boot.dev", TextType.LINK, "https://www.boot.dev")
        self.assertNotEqual(node1, node2)
    def test_img_neq(self):
        node1 = TextNode("This is an image", TextType.IMAGE, "public/image.png")
        node2 = TextNode("This is an image", TextType.IMAGE, "public/image.jpg")
        self.assertNotEqual(node1, node2)
    def test_mode_img_neq(self):
        node1 = TextNode("This is an image", TextType.IMAGE, "public/image.png")
        node2 = TextNode("This is an image", TextType.LINK, "https://example.com/public/image.png")
        self.assertNotEqual(node1, node2)
    def test_text_mode_img_new(self):
        node1 = TextNode("This is a link to boot.dev", TextType.LINK, "https://www.boot.dev/")
        node2 = TextNode("This is an image", TextType.IMAGE, "public/image.jpg")
        self.assertNotEqual(node1, node2)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text")
    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "public/image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props,{"src": "public/image.jpg", "alt": "This is an image"})

class TestSplitNodeDelimeter(unittest.TestCase):
    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        correct_new_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes,correct_new_nodes)
    def test_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        correct_new_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes,correct_new_nodes)
    def test_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        correct_new_nodes = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes,correct_new_nodes)

if __name__ == "__main__":
    unittest.main()
