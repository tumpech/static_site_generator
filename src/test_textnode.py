import unittest

from textnode import TextNode, TextType


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
        node1 = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is another text node", TextType.NORMAL)
        self.assertNotEqual(node1, node2)
    def test_mode_neq(self):
        node1 = TextNode("This is a text node", TextType.NORMAL)
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
    

if __name__ == "__main__":
    unittest.main()
