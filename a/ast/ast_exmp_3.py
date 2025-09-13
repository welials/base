import ast

"""
https://greentreesnakes.readthedocs.io/en/latest/tofrom.html
"""
tree = ast.parse("print('hello world')")
print(tree)
# <_ast.Module object at 0x9e3df6c>
exec(compile(tree, filename="<ast>", mode="exec"))
# hello world

class IntegerWrapper(ast.NodeTransformer):
    """Wraps all integers in a call to Integer()"""
    def visit_Num(self, node):
        if isinstance(node.value, int):
            return ast.Call(func=ast.Name(id='Integer', ctx=ast.Load()),
                            args=[node], keywords=[])
        return node

tree = ast.parse("1/3")
tree = IntegerWrapper().visit(tree)
# Add lineno & col_offset to the nodes we created
print(ast.fix_missing_locations(tree))
# ast.Module object at 0x000002AC7D06B350>
# The tree is now equivalent to Integer(1)/Integer(3)
# We would also need to define the Integer class and its __truediv__ method.