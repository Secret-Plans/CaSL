import json


class Parser:
    def __init__(self, types : list, settings : dict):
        
        self.types = types
        
        self.settings = settings

        self.ast = {}


    def process_line(self, line : list) -> dict:
        statement_type = ""
        if "assign" in line:
            if line[0] in self.types:
                statement_type = "Variable Declaration"
            elif line[0].split(":", 1)[0] == "id"
                statement_type = "Variable Assignment"
            else:
                raise UnexpectedTokenError(line[0])


    def parse(self, tokens : list) -> dict:
        self.ast["program"] = {}
        self.ast["program"]["body"] = []
        line = []
        line_counter = 0

        for token in tokens:
            if token == "\n":
                if len(line) > 0:
                    self.ast["program"]["body"].append(self.process_line(line))
                line_counter += 1
            else:
                line.append(token)

        if settings["Print AST"]:
            print(f"AST: {self.ast}")

        return {}


class UnexpectedTokenError(Exception):


    def __init__(self, token : str):
        self.token = token
    
    
    def __str__(self):
        return f"Unexpected token {self.token} at line "