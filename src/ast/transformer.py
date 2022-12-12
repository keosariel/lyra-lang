import sys
from lark import Transformer, Tree, Token
from .nodes import *

transformer_module = sys.modules[__name__]


class LyraTransformer(Transformer):

    def module(self, node):
        print(node)

    def function_sig(self, node):
        fname, fparams, fret = node
        return (fname, fparams, fret)
    
    def function_def(self, node):
        sig, body = node
        target, arglist, _type = sig
        
        return self.init_node(
            FunctionDef,
            target,
            type=_type,
            arglist=arglist,
            target=target,
            body=body
        )

    def parameters(self, nodes):
        return nodes
    
    def parameter(self, node):
        return node
    
    def type(self, node):
        return node[0]
    
    def variable(self, node):
        return node

    def declaration(self, node):
        (target, _type), expr = node
        return self.init_node(
            Declaration,
            target,
            target=target,
            type=_type,
            expr=expr
        )

    def body(self, node):
        return list(filter(None, node))

    def stmt(self, node):
        return node[0]

    def assign(self, node):
        target, val = node
        return self.init_node(
                Assign,
                target,
                target=target,
                expr=val
        )

    def expr(self, node):
        return node[0]
    
    def get_var(self, node):
        return node[0]

    def number(self, node):
        n = node[0]
        return self.init_node(Number, n, value=n.value)
    
    def NAME(self, node):
        return self.init_node(Name, node, value=node.value)

    def init_node(self, node_type, node, **kwargs):
        kwargs.update(dict(
                line=node.line,
                column=node.column,
                end_column=node.end_column,
        ))
        return node_type(**kwargs)
