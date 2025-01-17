from re import findall as re_findall
from htmlnode import LeafNode
from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    def __repr__(self):
        return f"TextNode({self.text},{self.text_type.value},{self.url})"

def text_node_to_html_node(text_node):
    match(text_node.text_type):
        case(TextType.TEXT):
            return LeafNode(None,text_node.text)
        case(TextType.BOLD):
            return LeafNode("b",text_node.text)
        case(TextType.ITALIC):
            return LeafNode("i",text_node.text)
        case(TextType.CODE):
            return LeafNode("code",text_node.text)
        case(TextType.ITALIC):
            return LeafNode("a",text_node.text,{"href": text_node.url})
        case(TextType.IMAGE):
            return LeafNode("i","",{"src": text_node.url, "alt": text_node.text})
        case _:
            ValueError(f"Invalid text type: {text_node.text_type}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        texts = old_node.text.split(delimiter)
        if len(texts) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(texts)):
            if texts[i] == '':
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(texts[i],TextType.TEXT))
            else:
                new_nodes.append(TextNode(texts[i],text_type))
    return new_nodes

def extract_markdown_images(text):
    return re_findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
def extract_markdown_links(text):
    return re_findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
