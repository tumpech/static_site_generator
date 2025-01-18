#!/usr/bin/env python3
from textnode import TextNode, TextType
import os,shutil
from markdown_blocks import markdown_to_html_node

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = os.path.dirname(DIR_PATH)

def copy_folder(from_path,to_path):
    if os.path.exists(to_path):
        print(f'Removing {to_path}')
        shutil.rmtree(to_path)
    print(f'Creating {to_path}')
    os.mkdir(to_path)
    for element in os.listdir(from_path):
        joined_from = os.path.join(from_path,element)
        joined_to   = os.path.join(to_path,element)
        print(f'Copying {joined_from} to {joined_to}')
        if os.path.isfile(joined_from):
            shutil.copy(joined_from,to_path)
        elif os.path.isdir(joined_from):
            copy_folder(joined_from, joined_to)
        else:
            print(f"WARNING: {joined_from} is not a file or dir, we won't copy it.")
            continue

def extract_title(markdown):
    for line in markdown.split('\n'):
        if line.startswith('# '):
            return line.strip('#').strip()

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        content = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    content_node = markdown_to_html_node(content)
    content_html = content_node.to_html()
    header = extract_title(content)
    html = template.replace('{{ Title }}', header).replace('{{ Content }}', content_html)
    os.makedirs(os.path.dirname(dest_path),exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(html)
    return True


def main():
    print("Copy static start")
    copy_folder(os.path.join(PROJECT_PATH,'static'),os.path.join(PROJECT_PATH,'public'))
    print('Copy static end')
    print(generate_page(os.path.join(PROJECT_PATH,"content/index.md"),os.path.join(PROJECT_PATH,"template.html"),os.path.join(PROJECT_PATH,"public/index.html")))
    #print(TextNode("This is a text node",TextType.BOLD,"https://www.boot.dev"))

if __name__ == "__main__":
    main()
