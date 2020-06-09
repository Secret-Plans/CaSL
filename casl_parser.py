import json


class Parser:
    """A parser for converting a set of tokens into an abstract syntax tree.
    """
    def __init__(self, statement_defs : dict, types : list, settings : dict):
        """Initializes the parser with a set of pre-defined statements and types
        
        Arguments:
            statement_defs {dict} -- Statement definitions.
            types {list} -- List of different types handled by the language.
            settings {dict} -- Parser settings. Change at Data/Config.json
        """

        self.statement_defs = statement_defs

        self.types = types
        
        self.settings = settings

        self.ast = {}


    def get_token_type(self, token : str) -> str:
        return token.split(":", 1)[0]


    def get_token_value(self, token : str) -> str:
        return token.split(":", 1)[1]


    def create_expression(self, tokens : list, line_counter : int) -> dict:
        expression = {}
        order_of_ops = ["func", ""]
        if len(tokens) > 1:
            pass
        else:
            value = self.statement_defs["Value"]
            _type = self.get_token_type(tokens[0])
            if _type in self.types:
                value["type"] = _type
            else:
                raise UnexpectedTokenError(token[0], line_counter)
            return 


    def process_line(self, line : list, line_num : int) -> dict:
        statement = {}
        statement["type"] = ""
        if "assign" in line:
            # Handles Variable Declarations
            if line[0] in self.types:
                statement = self.statement_defs["Variable Declaration"]
                statement["declaration"]["type"] = line[0]
                statement["declaration"]["id"] = self.get_token_value(line[1])
                
                
            
            # Handles Variable Assignments
            elif self.get_token_type(line[0]) == "id":
                statement = self.statement_defs["Variable Assignment"]
                statement["assignment"]["id"] = self.get_token_value(line[0])
            
            # Handles out of place assignment operators
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
                line.append(token)

        if self.settings["Print AST"]:
            print(f"AST: {self.ast}")

        return self.ast


class ExpressionTreeError(Exception):
    
    
    def __init__(self, line : int):
        self.line = line

    
    def __str__(self):
        return f"Expression tree error on line {self.line}"


class UnexpectedTokenError(Exception):


    def __init__(self, token : str, line : int):
        self.token = token
        self.line = line
    
    
    def __str__(self):
        return f"Unexpected token {self.token} at line {self.line}"