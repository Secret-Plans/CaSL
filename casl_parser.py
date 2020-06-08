import json


class Parser:
    def __init__(self, types : list, settings : dict):
        
        self.types = types
        
        self.settings = settings

        self.ast = {}


    def get_token_type(self, token):
        return token.split(":", 1)[0]


    def get_token_value(self, token):
        return token.split(":", 1)[1]


    def process_line(self, line : list, line_num : int) -> dict:
        statement = {}
        statement["type"] = ""
        if "assign" in line:
            if line[0] in self.types:
                statement["type"] = "Variable Declaration"
                statement["declaration"] = {
                    "type": line[0],
                    "id": self.get_token_value(line[1]),
                    "value": {
                        "type": "",
                        "data": ""
                    }
                }
                if self.get_token_type(line[3]) == statement["declaration"]["type"]:
                    statement["declaration"]["value"]["type"] = "literal"
                    statement["declaration"]["value"]["data"] = self.get_token_value(line[3])
                elif self.get_token_type(line[3]) == "id":
                    statement["declaration"]["value"]["type"] = "id"
                    statement["declaration"]["value"]["data"] = self.get_token_value(line[3])
                else:
                    raise UnexpectedTokenError(line[0], line_num)
            
            elif self.get_token_type(line[0]) == "id":
                statement["type"] = "Variable Assignment"
                statement["assignment"] = {
                    "id": self.get_token_value(line[0]),
                    "value": {
                        "type": "",
                        "data": ""
                    }
                }
                if self.get_token_type(line[2]) in self.types:
                    statement["assignment"]["value"]["type"] = "literal"
                    statement["assignment"]["value"]["data"] = self.get_token_value(line[2])
                elif self.get_token_type(line[2]) == "id":
                    statement["assignment"]["value"]["type"] = "id"
                    statement["assignment"]["value"]["data"] = self.get_token_value(line[2])
                else:
                    raise UnexpectedTokenError(line[0], line_num)
                
            else:
                raise UnexpectedTokenError(line[0], line_num)
        
        return statement



    def parse(self, tokens : list) -> dict:
        self.ast["program"] = {}
        self.ast["program"]["body"] = []
        line = []
        line_counter = 0

        for token in tokens:
            if token == "newline":
                if len(line) > 0:
                    self.ast["program"]["body"].append(self.process_line(line, line_counter))
                    line = []
                line_counter += 1
            else:
                print(f"appended {token}")
                line.append(token)

        if self.settings["Print AST"]:
            print(f"AST: {self.ast}")

        return self.ast


class UnexpectedTokenError(Exception):


    def __init__(self, token : str, line : int):
        self.token = token
        self.line = line
    
    
    def __str__(self):
        return f"Unexpected token {self.token} at line {self.line}"