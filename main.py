from casl_lexer import Lexer
from casl_parser import Parser
import json
import os

keyword_defs = {}
_dir = "Data/KeywordDefs"
for filename in os.listdir(_dir):
    with open(os.path.join(_dir, filename), "r") as f:
        keyword_defs = {**keyword_defs, **json.load(f)}

symbol_defs = {}
_dir = "Data/SymbolDefs"
for filename in os.listdir(_dir):
    with open(os.path.join(_dir, filename), "r") as f:
        symbol_defs = {**symbol_defs, **json.load(f)}

print(keyword_defs)
print(symbol_defs)

l = Lexer(keyword_defs, symbol_defs)