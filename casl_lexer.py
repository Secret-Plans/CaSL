

class Lexer:
    def __init__(self, keyword_defs : dict, symbol_defs : dict) -> None:
        self.keyword_defs = keyword_defs
        self.symbol_defs = symbol_defs
        
        self.tokens = []
    

    def add_token(self, token_key : str, token_value : str = None) -> None:
        if token_value == None:
            self.tokens.append(token_key)
        else:
            self.tokens.append(f"{token_key}:{token_value}")


    def is_keyword(self, keyword : str) -> bool:
        try:
            return keyword in list(self.keyword_defs) #Returns true or false based on whether the keyword is in the defs
        except:
            raise LookupError("keyword", keyword)


    def symbol_lookup(self, symbol: str) -> str:
        for key, value in self.symbol_defs.items():
            if symbol == value:
                return key
        raise LookupError("symbol", symbol)


    def tokenize(self, data : str) -> list:
        token_type = ""
        token_value = ""
        for char in data:
            if token_type == "id":
                if char.isalnum():
                    token_value += char
                else:
                    if self.is_keyword(token_value):
                        self.add_token(token_value)
                    else:
                        self.add_token(token_type, token_value)
                    token_type = ""
                    token_value = ""
            
            elif token_type == "number":
                if char.isnumeric or char == ".":
                    token_value += char
                else:
                    self.add_token(token_type, token_value)
                    token_type = ""
                    token_value = ""
            
            elif token_type == "string":
                if char == "\"":
                    self.add_token(token_type, token_value)
                    token_type = ""
                    token_value = ""
                    continue
                else:
                    token_value += char

            elif token_type == ""

            elif token_type == "":
                if char.isalpha():
                    token_type = "id"
                    token_value += char
                elif char.isnumeric():
                    token_type = "number"
                    token_value += char
                elif char == "\"":
                    token_type = "string"
                elif char in "+-*/":
                    token_type = "symbol"
                    token_value += char
                elif char == "\n":
                    token_type == "newline"
        
        return []


class LexerError(Exception):
    def __init__(self, character_pos, character):
        self.character_pos = character_pos
        self.character = character
    
    def __str__(self):
        return f"Lexer Error at {self.character_pos}: character '{self.character}'"


class LookupError(Exception):
    def __init__(self, procedure : str, item : str):
        self.procedure = procedure
        self.item = item
    
    def __str__(self):
        return f"{self.procedure.title()} lookup error with element {self.item}"