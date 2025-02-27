from textnode import TextType, TextNode

from re import findall as re_findall

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

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        text_string = old_node.text
        for image_alt, image_link in images:
            text_list = text_string.split(f"![{image_alt}]({image_link})",1)
            if text_list[0] != '':
                   new_nodes.append(TextNode(text_list[0],TextType.TEXT))
            new_nodes.append(TextNode(image_alt,TextType.IMAGE,image_link))
            text_string = text_list[1]
        if text_string != '':
            new_nodes.append(TextNode(text_string,TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        links = extract_markdown_links(old_node.text)
        text_string = old_node.text
        for link_text, link_url in links:
            text_list = text_string.split(f"[{link_text}]({link_url})",1)
            if text_list[0] != '':
                   new_nodes.append(TextNode(text_list[0],TextType.TEXT))
            new_nodes.append(TextNode(link_text,TextType.LINK,link_url))
            text_string = text_list[1]
        if text_string != '':
            new_nodes.append(TextNode(text_string,TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    initial_node = TextNode(text, TextType.TEXT)
    nodes = split_nodes_delimiter([initial_node], "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
