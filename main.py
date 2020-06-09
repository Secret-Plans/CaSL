from casl_lexer import Lexer
from casl_parser import Parser
import json
import os


# Loads settings
settings = {}
with open("Data/Config.json") as f:
    settings = json.load(f)

if settings["File Loading"]["Print Settings"]:
    print(f"Settings: {settings}\n\n")


# Loads keywords
keyword_defs = []
_dir = "Data/KeywordDefs"
for filename in os.listdir(_dir):
    with open(os.path.join(_dir, filename), "r") as f:
        keyword_defs += json.load(f)["root"]

if settings["File Loading"]["Print Keywords"]:
    print(f"Keyword Definitions: {keyword_defs}\n\n")


# Loads symbols
symbol_defs = {}
_dir = "Data/SymbolDefs"
for filename in os.listdir(_dir):
    with open(os.path.join(_dir, filename), "r") as f:
        symbol_defs = {**symbol_defs, **json.load(f)}

if settings["File Loading"]["Print Symbols"]:
    print(f"Symbol Definitions: {symbol_defs}\n\n")


# Loads statements
statement_defs = {}
_dir = "Data/StatementDefs"
for filename in os.listdir(_dir):
    with open(os.path.join(_dir, filename), "r") as f:
        statement_defs = {**statement_defs, **json.load(f)}

if settings["File Loading"]["Print Statements"]:
    print(f"Statement Definitions: {statement_defs}\n\n")


print("\n\n")


# Loads file to be compiled
with open("Data/Test Files/Test 1.casl", "r") as f:
    data = f.read()


# Lexical Analysis
l = Lexer(keyword_defs, symbol_defs, settings["Lexer"])
tokens = l.tokenize(data)


# Parsing
p = Parser(["num", "string", "bool", "list", "matrix"], settings["Parser"])
ast = p.parse(tokens)

with open("Output/ast.json", "w+") as f:
    f.write(json.dumps(ast, indent=4))


# Compilation