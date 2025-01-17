import unittest

from textnode import TextNode, TextType, text_node_to_html_node, split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link


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
        self.assertEqual(html_node.tag, "img")
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
    
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = extract_markdown_images(text)
        correct = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        self.assertEqual(result,correct)
    def test_extract_markdown_link(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result = extract_markdown_links(text)
        correct = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(result,correct)
    
    def test_split_nodes_link(self):
        text = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",TextType.TEXT)
        result = split_nodes_image([text])
        correct = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
        ]
        self.assertEqual(result,correct)

    def test_split_nodes_link(self):
        text = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT)
        result = split_nodes_link([text])
        correct = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(result,correct)

if __name__ == "__main__":
    unittest.main()
