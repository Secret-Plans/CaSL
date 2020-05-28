

class Lexer:
    def __init__(self, keyword_defs: dict, symbol_defs: dict):
        self.keyword_defs = keyword_defs
        self.symbol_defs = symbol_defs
        
        self.tokens = []
    

    def keyword_lookup(self, keyword : str) -> bool:
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
            pass
        
        return []


class LexerError(Exception):
    def __init__(self, character_pos = 0, character = "?"):
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