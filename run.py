from src.ast import parse_lyra_source
import sys


if len(sys.argv) < 2:
    print("lyra file required!")
    exit(0)

target = sys.argv[1]

with open(target, "r") as fp:
    print(parse_lyra_source(fp.read()))
