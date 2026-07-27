from __future__ import annotations
from typing import List
from collections import defaultdict
import re

class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        eval_map = dict(zip(evalvars, evalints))
        
        class Poly:
            def __init__(self, terms=None):
                self.terms = defaultdict(int)
                if terms:
                    for key, val in terms.items():
                        if val != 0:
                            self.terms[key] = val
            
            def __add__(self, other):
                result = Poly(self.terms.copy())
                for key, val in other.terms.items():
                    result.terms[key] += val
                    if result.terms[key] == 0:
                        del result.terms[key]
                return result
            
            def __sub__(self, other):
                result = Poly(self.terms.copy())
                for key, val in other.terms.items():
                    result.terms[key] -= val
                    if result.terms[key] == 0:
                        del result.terms[key]
                return result
            
            def __mul__(self, other):
                result = Poly()
                for k1, v1 in self.terms.items():
                    for k2, v2 in other.terms.items():
                        new_key = tuple(sorted(k1 + k2))
                        result.terms[new_key] += v1 * v2
                        if result.terms[new_key] == 0:
                            del result.terms[new_key]
                return result
            
            def to_list(self):
                items = []
                for key, val in self.terms.items():
                    if val != 0:
                        degree = len(key)
                        items.append((degree, key, val))
                
                items.sort(key=lambda x: (-x[0], x[1]))
                
                result = []
                for _, key, val in items:
                    if key:
                        result.append(f"{val}*{'*'.join(key)}")
                    else:
                        result.append(str(val))
                return result
        
        def tokenize(expr):
            tokens = []
            i = 0
            while i < len(expr):
                if expr[i].isspace():
                    i += 1
                elif expr[i] in '()+-*':
                    tokens.append(expr[i])
                    i += 1
                elif expr[i].isdigit():
                    j = i
                    while j < len(expr) and expr[j].isdigit():
                        j += 1
                    tokens.append(expr[i:j])
                    i = j
                elif expr[i].isalpha():
                    j = i
                    while j < len(expr) and expr[j].isalnum():
                        j += 1
                    tokens.append(expr[i:j])
                    i = j
                else:
                    i += 1
            return tokens
        
        def parse_token(token):
            if token.lstrip('-').isdigit():
                return Poly({(): int(token)})
            elif token in eval_map:
                return Poly({(): eval_map[token]})
            else:
                return Poly({(token,): 1})
        
        def parse_expr(tokens, idx):
            left, idx = parse_term(tokens, idx)
            while idx < len(tokens) and tokens[idx] in ['+', '-']:
                op = tokens[idx]
                idx += 1
                right, idx = parse_term(tokens, idx)
                if op == '+':
                    left = left + right
                else:
                    left = left - right
            return left, idx
        
        def parse_term(tokens, idx):
            left, idx = parse_factor(tokens, idx)
            while idx < len(tokens) and tokens[idx] == '*':
                idx += 1
                right, idx = parse_factor(tokens, idx)
                left = left * right
            return left, idx
        
        def parse_factor(tokens, idx):
            if tokens[idx] == '(':
                idx += 1
                result, idx = parse_expr(tokens, idx)
                idx += 1  # skip ')'
                return result, idx
            else:
                return parse_token(tokens[idx]), idx + 1
        
        tokens = tokenize(expression)
        poly, _ = parse_expr(tokens, 0)
        return poly.to_list()