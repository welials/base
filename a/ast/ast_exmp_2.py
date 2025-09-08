import ast

"""
https://habr.com/ru/companies/piter/articles/493424/
"""

my_tree = ast.parse("3 + 4*x")
print(ast.dump(my_tree, indent=4))
"""
Module(
    body=[
        Expr(
            value=BinOp(
                left=Constant(value=3),
                op=Add(),
                right=BinOp(
                    left=Constant(value=4),
                    op=Mult(),
                    right=Name(id='x', ctx=Load()))))])
"""
my_tree = ast.parse("a.append(3)")
print(ast.dump(my_tree, indent=4))
"""
Module(
    body=[
        Expr(
            value=Call(
                func=Attribute(
                    value=Name(id='a', ctx=Load()),
                    attr='append',
                    ctx=Load()),
                args=[
                    Constant(value=3)]))])
"""
my_tree = ast.parse("del x")
print(ast.dump(my_tree, indent=4))
"""
Module(
    body=[
        Delete(
            targets=[
                Name(id='x', ctx=Del())])])
"""
my_tree = ast.parse("y = 3")
print(ast.dump(my_tree, indent=4))
"""
Module(
    body=[
        Assign(
            targets=[
                Name(id='y', ctx=Store())],
            value=Constant(value=3))])
"""


class MyOptimizer(ast.NodeTransformer):

    def visit_Name(self, node: ast.Name):
        if node.id == 'pi':
            return ast.Constant(value=3.14159265) # ast.Num(n=3.14159265) <- DeprecationWarning
        return node


tree = ast.parse("y = 2 * pi")
optimizer = MyOptimizer()
tree = optimizer.visit(tree)
print(ast.dump(tree, indent=4))

"""
Module(
    body=[
        Assign(
            targets=[
                Name(id='y', ctx=Store())],
            value=BinOp(
                left=Constant(value=2),
                op=Mult(),
                right=Constant(value=3.14159265)))])
"""


class MyOptimizer(ast.NodeTransformer):

    def visit_Name(self, node: ast.Name):
        if node.id == 'pi':
            result = ast.Constant(value=3.14159265) # ast.Num(n=3.14159265) <- DeprecationWarning
            result.lineno = node.lineno
            result.col_offset = node.col_offset
            return result
        return node


tree = ast.parse("print(2 * pi)")
optimizer = MyOptimizer()
tree = optimizer.visit(tree)
code = compile(tree, "<string>", "exec")
exec(code)
# 6.2831853