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

"""
TODO: strings
TODO: array & struct property assignment
TODO: structs
TODO: pointers
"""

class LyraTypeChecker:

    def __init__(self, module, source):
        self.module = module
        self.source = source.split("\n")
        self.types_def = PRIMITIVES
        self.func_def = {}
        
        for node in module:
            self.visit(node, {})

    def visit(self, node, s_locals):
        if isinstance(node, FunctionDef):
            return self.visit_function(node)
            
        elif isinstance(node, Call):
            return self.visit_call(node, s_locals)
        
        elif isinstance(node, Name):
            return self.visit_name(node, s_locals)

        elif isinstance(node, Number):
            return self.visit_number(node)

        elif isinstance(node, Declaration):
            return self.visit_declaration(node, s_locals)

        elif isinstance(node, IfBlock) or isinstance(node, WhileBlock) or isinstance(node, UntilBlock):
            self.visit_cond_block(node, s_locals)

        elif isinstance(node, CompareOp):
            return self.visit_boolop(node, s_locals)

        elif isinstance(node, BinaryOp):
            return self.visit_binop(node, s_locals)

        elif isinstance(node, UnaryOp):
            return self.visit_uop(node, s_locals)

        elif isinstance(node, Assign):
            return self.visit_assign(node, s_locals)

        elif isinstance(node, List):
            return self.visit_list(node, s_locals)

        elif isinstance(node, GetItem):
            return self.visit_getitem(node, s_locals)

        # else:
        #     print(node)

    def visit_getitem(self, node, s_locals):
        target = node.target
        t_type = self.visit(target, s_locals)

        if not isinstance(t_type, LyraArrayType):
            self.error(f"Expected an array but got `{t_type.str_rep()}`")
        return t_type.elem

    def visit_list(self, node, s_locals):
        items = node.arglist

        i_type = None
        for i in items:
            if i_type is None:
                i_type = self.visit(i, s_locals)
            else:
                _i_type = self.visit(i, s_locals)

                if i_type != _i_type:
                    self.error(f"Expected element of type `{i_type.str_rep()}` but got `{_i_type.str_rep()}`", i)

        return LyraArrayType(i_type, len(items))

    def visit_assign(self, node, s_locals):
        target = node.target
        val = node.value
        t_type = None

        if isinstance(target, Name) or isinstance(target, GetItem):
            t_type = self.visit(target, s_locals)
        else:
            self.error("Invalid assignment", target)

        v_type = self.visit(val, s_locals)

        if not(t_type == v_type):
            self.error(f"Expected type `{t_type.str_rep()}` but got `{v_type.str_rep()}`", val)

        return t_type

    def visit_comp(self, node, s_locals):
        lhs = node.lhs
        rhs = node.rhs

        lhs_type = self.visit(lhs, s_locals)
        rhs_type = self.visit(rhs, s_locals)

        if not (lhs_type == rhs_type):
            self.error("Operation on different types", lhs)

        typ = LyraBoolType()
        return LyraBoolType()

    def visit_boolop(self, node, s_locals):
        return self.visit_comp(node, s_locals)

    def visit_uop(self, node, s_locals):
        lhs = node.lhs
        lhs_type = self.visit(lhs, s_locals)

        if node.op not in lhs_type.bin_ops + lhs_type.bit_ops:
            self.error(f"Invalid operator `{node.op}` on type `{lhs_type.str_rep()}`", lhs)

        return lhs_type

    def visit_binop(self, node, s_locals):
        
        lhs = node.lhs
        rhs = node.rhs

        lhs_type = self.visit(lhs, s_locals)
        rhs_type = self.visit(rhs, s_locals)

        if not (lhs_type == rhs_type):
            self.error("Operation on different types", lhs)

        if node.op not in lhs_type.bin_ops + lhs_type.bit_ops:
            self.error(f"Invalid operator `{node.op}` on type `{lhs_type.str_rep()}`", lhs)

        return lhs_type

    def visit_number(self, node):
        _type = node.type

        if _type in ["DEC_NUMBER", "HEX_NUMBER", "OCT_NUMBER", "BIN_NUMBER"]:
            typ = self.types_def["i32"]
        elif _type == "FLOAT_NUMBER":
            typ = self.types_def["f32"]

        return typ

    def visit_name(self, node, s_locals):
        n_str = node.value
        v_type = s_locals.get(n_str)

        if v_type is None:
            self.error(f"Identifier `{n_str}` is undefined", node)
        return v_type


    def visit_declaration(self, node, s_locals):
        target = node.target.value
        value = node.value

        type = self._type_exists(node.type)

        if target in s_locals:
            self.error(f"Identifier `{target}` is already defined", node.target)

        if value is None:
            s_locals[target] = type
            return type

        val_type = self.visit(value, s_locals)

        if not (type == val_type):
            self.error(f"Expected type `{type.str_rep()}` but got `{val_type.str_rep()}`", value)

        s_locals[target] = type
        return type

    def visit_call(self, node, s_locals):
        target = node.target
        arglist = node.arglist or []

        _lyra_args = []

        for n in arglist:
            _lyra_args.append(self.visit(n, s_locals))
        
        if isinstance(target, Name):
            _args = ",".join(arg.str_rep() for arg in _lyra_args)
            func_sig = f"{target.value}({_args})"

            if func_sig not in self.func_def:
                self.error(f"Unknown function with signature `{func_sig}`", target)

        func = self.func_def[func_sig]
        return func.return_type

    def visit_function(self, node):
        return_type = node.type
        arglist = node.arglist or []
        func_name = node.target.value
        body = node.body

        exists = []
        _lyra_ret = self._type_exists(return_type)
        _lyra_params = []
        
        func_locals = {}

        for name, typ in arglist:
            name_str = name.value

            if name_str in exists:
                self.error(f"Arguement `{name_str}` appears more than once", name)
            else:
                exists.append(name_str)
            
            v_type = self._type_exists(typ)
            _lyra_params.append(v_type)
            func_locals[name_str] = v_type

        func_typ =  LyraFunctionType(_lyra_ret, *_lyra_params)
        _params = ",".join(p.str_rep() for p in _lyra_params)
        func_sig = f"{func_name}({_params})"

        self.func_def[func_sig] = func_typ

        for node in body:
            self.visit(node, func_locals)

        return func_typ

    def visit_cond_block(self, node, s_locals):
        cond = node.expr

        cond_type = self.visit(cond, s_locals)

        if cond_type != LyraBoolType():
            self.error(f"Expected a boolean but got `{cond_type.str_rep()}`", cond)

        body = node.body
        _locals = dict(s_locals) # copying previous locals
        for n in body:
            self.visit(n, _locals)


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
            index = node.index
            if not isinstance(index, Number):
                self.error("Expected an integer constant", index)

            count = int(index.value)
            arr_type = LyraArrayType(n_type, count)
            return arr_type


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
