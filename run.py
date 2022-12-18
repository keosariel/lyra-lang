from src.ast import parse_lyra_source, parse_lyra_tree
import sys
from pprint import pprint
from src.typechecker import LyraTypeChecker

if len(sys.argv) < 2:
    print("lyra file required!")
    exit(0)

target = sys.argv[1]

with open(target, "r") as fp:
    code = fp.read()
    module = parse_lyra_tree(code)
    # print(parse_lyra_source(code))
    # pprint([i.to_dict() for i in module])
    # pprint(parse_lyra_tree(code))
    LyraTypeChecker(module, code)