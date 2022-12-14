# Typed Lyra: static typechecker

from src.types import *
from src.ast.nodes import *

PRIMITIVES = {
    "i32": LyraIntType(32),
    "i64": LyraIntType(64),
    "bool": LyraBoolType(),
    "void": LyraVoidType(),
    "f32": LyraFloatType(),
    "f64": LyraDoubleType()
}

class LyraTypeChecker:

    def __init__(self, module, source):
        self.module = module
        self.source = source.split("\n")


        for node in module:
            self.visit(node)

    def visit(self, node):
        t = None

        if isinstance(node, FunctionDef):
            t = self.visit_function(node)

    def visit_function(self, node):
        return_type = node.type
        arglist = node.arglist or []
        func_name = node.target

        exists = []
        for name, typ in arglist:
            name_str = name.value

            if name_str in exists:
                self.error(f"Arguement `{name_str}`appears more than once", name)
            else:
                exists.append(name_str)

            print(name, typ)

    def _check_name(self, node):
        """
        A check to confirm a node is of type `nodes.Name`

        Args:
            node (nodes.LyraNode): node to check

        Returns:
            value (None)
        """

        if not isinstance(node, Name):
            self.error("Expected an Identifier", node)

    def error(self, msg, node):
        line = node.line
        col = node.column
        col_end = node.end_column

        line_source = self.source[line-1]
        fname = "<filename>"
        err_msg = f"{fname}:{line}:{col} "
        err_msg += msg + "\n"
        err_msg += line_source + "\n"
        err_msg += " "*(col-1) + ("^"*(col_end-col))
        print(err_msg)
        exit(1)
