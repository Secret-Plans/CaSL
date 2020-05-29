

class Lexer:
    """A lexical analyzer that generates tokens based on some simple rules and a set of reserved keywords and symbols.
    """
    def __init__(self, keyword_defs : dict, symbol_defs : dict) -> None:
        """Initializes the lexer with a set of keyword and symbol definitions.

        Arguments:
            keyword_defs {dict} -- Keyword definitions.
            symbol_defs {dict} -- Symbol definitions.
        """
        self.keyword_defs = keyword_defs
        self.symbol_defs = symbol_defs

        self.starter_symbols = "" #Starter symbols are symbols that operator/symbol tokens can have as their first character
        self.following_symbols = "" #Following symbols are symbols that operator/symbol tokens can contain after their first character
        for item in symbol_defs.values():
            if not(item[0] in self.starter_symbols):
                self.starter_symbols += item[0]
            if len(item) > 1:
                if not(item[1] in self.following_symbols):
                    self.following_symbols += item[1]

        self.tokens = []
    

    def add_token(self, token_key : str, token_value : str = None) -> None:
        """Adds a token to the lexer's token array.

        Arguments:
            token_key {str} -- The key or type of token, e.g: id or string.

        Keyword Arguments:
            token_value {str} -- The value of the token, if needed, e.g: 5 or "Hello World". (default: {None})
        """
        if token_value == None:
            self.tokens.append(token_key)
        else:
            self.tokens.append(f"{token_key}:{token_value}")


    def is_keyword(self, keyword : str) -> bool:
        """Checks if a given identifier is a reserved keyword or not.

        Arguments:
            keyword {str} -- The identifier to lookup in the keyword definitions.

        Raises:
            LookupError: Raises if the keyword lookup fails for whatever reason.

        Returns:
            bool -- Whether or not the identifier is a reserved keyword or not.
        """
        try:
            return keyword in list(self.keyword_defs) #Returns true or false based on whether the keyword is in the defs
        except:
            raise LookupError("keyword", keyword)


    def symbol_lookup(self, symbol: str) -> str:
        """Finds the name of the operator or symbol corresponding to it's notation via the symbol definitions.

        Arguments:
            symbol {str} -- The symbol notation to lookup.

        Raises:
            LookupError: Raised if there is no name in the definitions corresponding to the symbol,

        Returns:
            str -- The name of the symbol.
        """
        for key, value in self.symbol_defs.items():
            if symbol == value:
                return key
        raise LookupError("symbol", symbol)


    def tokenize(self, data : str) -> list:
        """Generates a list of tokens and returns them as a list.

        Arguments:
            data {str} -- The data to be tokenized.

        Returns:
            list -- The generated list of tokens.
        """
        data += " "
        
        token_type = ""
        token_value = ""
        for char in data:

            # Handles token if it's an identifier
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
            
            #Handles token if it's a number
            elif token_type == "number":
                if char.isnumeric():
                    token_value += char
                else:
                    self.add_token(token_type, token_value)
                    token_type = ""
                    token_value = ""
            
            #Handles token if it's a string
            elif token_type == "string":
                if char == "\"":
                    self.add_token(token_type, token_value)
                    token_type = ""
                    token_value = ""
                    continue
                else:
                    token_value += char

            #Handles token if it's a symbol
            elif token_type == "symbol":
                if char in self.following_symbols:
                    token_value += char
                else:
                    self.add_token(self.symbol_lookup(token_value))
                    token_type = ""
                    token_value = ""

            #Handles token if it's a newline
            elif token_type == "newline":
                self.add_token(token_type)
                token_type = ""
                token_value = ""

            #Handles token if a type has not been assigned to it yet
            if token_type == "":
                if char.isalpha():
                    token_type = "id"
                    token_value += char
                elif char.isnumeric():
                    token_type = "number"
                    token_value += char
                elif char == "\"":
                    token_type = "string"
                elif char in self.starter_symbols:
                    token_type = "symbol"
                    token_value += char
                elif char == "\n":
                    token_type = "newline"
        
        return self.tokens


class LexerError(Exception):
    """Error during the tokenizing process
    """
    def __init__(self, character_pos, character):
        self.character_pos = character_pos
        self.character = character
    
    def __str__(self):
        return f"Lexer Error at {self.character_pos}: character '{self.character}'"


class LookupError(Exception):
    """Error during the process of looking up a symbol or checking for a keyword
    """
    def __init__(self, procedure : str, item : str):
        self.procedure = procedure
        self.item = item
    
    def __str__(self):
        return f"{self.procedure.title()} lookup error with element {self.item}"