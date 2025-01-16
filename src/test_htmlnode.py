import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_html_link_props(self):
        node1 = HTMLNode('a','This is a link',None,{"href": "https://www.google.com","target": "_blank",})
        props_result = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node1.props_to_html(), props_result)
    def test_html_img_props(self):
        node1 = HTMLNode("img","Yup! This is an image.", None, {"src": "public/image.png","alt":"This is an image.","width":"104","height":"142"})
        props_result = ' src="public/image.png" alt="This is an image." width="104" height="142"'
        self.assertEqual(node1.props_to_html(), props_result)
    def test_html_eq(self):
        node1 = HTMLNode("img","Yup! This is an image.", None, {"src": "public/image.png","alt":"This is an image.","width":"104","height":"142"}).__repr__()
        node2 = HTMLNode("img","Yup! This is an image.", None, {"src": "public/image.png","alt":"This is an image.","width":"104","height":"142"}).__repr__()
        self.assertEqual(node1, node2)
    def test_html_none_props(self):
        node1 = HTMLNode("img","Yup! This is an image.", None, None)
        node2 = HTMLNode("img","Yup! This is an image.", None, None)
        self.assertEqual(node1.props_to_html(), node2.props_to_html())
    def test_to_html(self):
        node1 = LeafNode("p","Hello World!")
        html_result = "<p>Hello World!</p>"
        self.assertEqual(node1.to_html(),html_result)
    def test_to_html_no_tag(self):
        node1 = LeafNode(None,"Hello World!")
        html_result = "Hello World!"
        self.assertEqual(node1.to_html(),html_result)

if __name__ == "__main__":
    unittest.main()
