from lark import Lark, ast_utils

def lyra_grammar():
    with open("./src/ast/grammar.lark", "r") as fp:
        lyra_parser = Lark(fp.read(), start="module", parser='lalr')

    return lyra_parser

def parse_lyra_source(code):
    return lyra_grammar().parse(code + "\n")


