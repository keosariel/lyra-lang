NODE_DEFAULT_FIELDS = {
    "source",
    "line",
    "column",
    "end_column"
}

class LyraNode:
    """
    Base class for Lyra AST nodes
    """

    __fields__ = NODE_DEFAULT_FIELDS

    def __init__(self, **kwargs):
        self._fields = set(self.__fields__).union(NODE_DEFAULT_FIELDS)

        for field in self._fields:
            if field in kwargs:
                setattr(self, field, kwargs[field])
            else:
                setattr(self, field, None)

    def __repr__(self):
        props = ", ".join([f"{k}={getattr(self, k, None)}" for k in self.__fields__ ])
        return f"{self.__class__.__name__}({props})"



class Module(LyraNode):
    __fields__ = ("body",)

class StructDef(LyraNode):
    __fields__ = ("name", "members")

class FunctionDef(LyraNode):
    __fields__ = ("type", "arglist", "target", "body")

class Statement(LyraNode):
    pass

class BreakStatement(Statement):
    __fields__ = ()

class ContinueStatement(Statement):
    __fields__ = ()

class ContinueStatement(Statement):
    __fields__ = ()

class ReturnStatement(Statement):
    __fields__ = ("expr",)

class BreakStatement(Statement):
    __fields__ = ()

class Declaration(Statement):
    __fields__ = ("target", "type", "expr")

class Assign(Statement):
    __fields__ = ("target", "expr")

class Block(LyraNode):
    __fields__ = ("expr", "body")

class IfBlock(Block):
    __fields__ = ("expr", "body", "orelse")

class WhileBlock(Block):
    pass

class UntilBlock(Block):
    pass

class Expression(LyraNode):
    pass

class GetAttribute(Expression):
    __fields__ = ("value", "attr")

class Call(Expression):
    __fields__ = ("target", "arglist")

class Name(Expression):
    __fields__ = ("value",)

class Constant(Expression):
    __fields__ = ("value",)

class Operation(Expression):
    __fields__ = ("op", "lhs", "rhs")

class UnaryOp(Operation):
    pass

class BinaryOp(Operation):
    pass

class BooleanOp(Operation):
    pass

class CompareOp(BooleanOp):
    pass

class Number(Constant):
    __fields__ = ("value", "type")

class String(Constant):
    __fields__ = ("value", "type")

class Boolean(Constant):
    __fields__ = ("value",)

