from lark import Lark, ast_utils
from .transformer import LyraTransformer, transformer_module

def lyra_grammar():
    with open("./src/ast/grammar.lark", "r") as fp:
        lyra_parser = Lark(fp.read(), start="module", parser='lalr')

    return lyra_parser

def parse_lyra_source(code):
    return lyra_grammar().parse(code + "\n")

def parse_lyra_tree(code):
    transformer = ast_utils.create_transformer(transformer_module, LyraTransformer())
    return transformer.transform(parse_lyra_source(code))
