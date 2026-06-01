class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        self.idx = 0
        self.expr = expression
        
        def parse():
            ch = self.expr[self.idx]
            self.idx += 1
            
            if ch == 't':
                return True
            elif ch == 'f':
                return False
            elif ch in '!&|':
                self.idx += 1  # skip '('
                values = []
                
                while self.expr[self.idx] != ')':
                    if self.expr[self.idx] == ',':
                        self.idx += 1
                    else:
                        values.append(parse())
                
                self.idx += 1  # skip ')'
                
                if ch == '!':
                    return not values[0]
                elif ch == '&':
                    return all(values)
                else:  # ch == '|'
                    return any(values)
        
        return parse()