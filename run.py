from src.ast import parse_lyra_source, parse_lyra_tree
import sys


if len(sys.argv) < 2:
    print("lyra file required!")
    exit(0)

target = sys.argv[1]

with open(target, "r") as fp:
    code = fp.read()
    # print(parse_lyra_source(code))
    print(parse_lyra_tree(code))
