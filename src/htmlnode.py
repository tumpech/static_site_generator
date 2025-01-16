class HTMLNode():
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        if self.props == None:
            return ""
        return ''.join([f' {x}="{self.props[x]}"' for x in self.props])

    def __repr__(self):
        return f"HTMLNode({self.tag},{self.value},{self.children},{self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
    def to_html(self):
        if self.value == None:
            raise ValueError("Invalid HTML: no value.")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)
    def to_html(self):
        if self.tag == None:
            raise ValueError("Invalid HTML: no tag")
        
        if self.children == None:
            raise ValueError('Invalid HTML: no children')
        
        #children_rendered = "".join([x.to_html() in x for self.children])
        children_rendered = ""
        for i in self.children:
            children_rendered += i.to_html()
        
        return f"<{self.tag}{self.props_to_html()}>{children_rendered}</{self.tag}>"
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"