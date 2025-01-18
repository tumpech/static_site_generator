#!/usr/bin/env python3
from textnode import TextNode, TextType
import os,shutil

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

def main():
    print("Copy start")
    copy_folder(os.path.join(PROJECT_PATH,'static'),os.path.join(PROJECT_PATH,'public'))
    print('Copy end')
    #print(TextNode("This is a text node",TextType.BOLD,"https://www.boot.dev"))

if __name__ == "__main__":
    main()
