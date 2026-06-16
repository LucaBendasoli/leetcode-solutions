class Fancy:

    def __init__(self):
        self.MOD = 10**9 + 7
        self.seq = []
        self.mult = 1
        self.add = 0
    
    def append(self, val: int) -> None:
        # Store value with current transformation state
        # We need to "undo" current transformations to get base value
        # base = (val - add) / mult
        base = (val - self.add) * self.mod_inverse(self.mult) % self.MOD
        self.seq.append((base, self.mult, self.add))
    
    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD
    
    def multAll(self, m: int) -> None:
        self.mult = (self.mult * m) % self.MOD
        self.add = (self.add * m) % self.MOD
    
    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        base, old_mult, old_add = self.seq[idx]
        # Apply transformations: first undo old state, then apply current
        # Actually base is already the "neutral" value
        # Current value = base * mult + add
        result = (base * self.mult + self.add) % self.MOD
        return result
    
    def mod_inverse(self, a: int) -> int:
        # Fermat's little theorem: a^(p-1) ≡ 1 (mod p) for prime p
        # So a^(-1) ≡ a^(p-2) (mod p)
        return pow(a, self.MOD - 2, self.MOD)