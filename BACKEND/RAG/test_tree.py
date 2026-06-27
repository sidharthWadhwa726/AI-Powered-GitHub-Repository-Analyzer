from tree_sitter_language_pack import get_parser

code = """
class A:
    def hello(self):
        pass

def route():
    pass
"""

parser = get_parser("python")
tree = parser.parse(code)

root = tree.root_node()

print(type(root))
print(dir(root))