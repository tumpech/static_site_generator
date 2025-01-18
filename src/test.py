from markdown_blocks import markdown_to_blocks, markdown_to_html_node, block_to_block_type

md = """
# this is an h1

this is paragraph text

## this is an h2
"""
node = markdown_to_html_node(md)
print(node.to_html())