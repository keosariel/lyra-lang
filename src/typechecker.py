# Typed Lyra: static typechecker

from src.types import *
from src.ast.nodes import *

PRIMITIVES = {
    "i32": LyraIntType(32),
    "i64": LyraIntType(64),
    "bool": LyraBoolType(),
    "char": LyraIntType(8),
    "void": LyraVoidType(),
    "f32": LyraFloatType(),
    "f64": LyraDoubleType()
}

class LyraTypeChecker:

    def __init__(self, module, source):
        self.module = module
        self.source = source.split("\n")
        self.types_def = PRIMITIVES
        self.func_def = {}
        
        for node in module:
            self.visit(node)

    def visit(self, node):
        t = None

        if isinstance(node, FunctionDef):
            t = self.visit_function(node)

    def visit_function(self, node):
        return_type = node.type
        arglist = node.arglist or []
        func_name = node.target.value

        exists = []
        _lyra_ret = self._type_exists(return_type)
        _lyra_params = []

        for name, typ in arglist:
            name_str = name.value

            if name_str in exists:
                self.error(f"Arguement `{name_str}` appears more than once", name)
            else:
                exists.append(name_str)

            _lyra_params.append(self._type_exists(typ))

        func_typ =  LyraFunctionType(_lyra_ret, *_lyra_params)
        func_sig = f"{func_name}_{func_typ.str_rep()}"

        setattr(node, "functype", func_typ)
        self.func_def[func_sig] = func_typ

    def _type_exists(self, node):
        if node is None:
            return self.types_def["void"]

        if isinstance(node, Name):
            n_str = node.value

            if n_str not in self.types_def:
                self.error(f"Unknown datatype `{n_str}`", node)
            return self.types_def[n_str]
        
        elif isinstance(node, GetItem):
            n_type = self._type_exists(node.target)
            # TODO: create a array with int constant check
            return n_type

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
