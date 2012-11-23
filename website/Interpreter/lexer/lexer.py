#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tclh123'

import string
import token
from token import Token
from token import Token_Type

class Lexer:
    def __init__(self, source):
        self._buffer = source.upper()
        self._pos = 0
        self._lineno = 1
        self._buffersize = len(source)
        self._eof = False

    def __iter__(self):
        return self

    def next(self):
        """
        Return the next token or raise StopIteration
        """
        if not self._eof:
            ret = self.next_token()
            while not ret:
                if self._eof: raise StopIteration
                ret = self.next_token()
            return ret
        else:
            raise StopIteration

    def _advance(self):
        self._pos += 1
        self._eof = True if self._pos >= self._buffersize else False

    def _peek(self):
        return self._buffer[self._pos] if not self._eof else None

    def _skip(self):
        next = self._peek()
        while next and next in string.whitespace:
            if next == '\n':
                self._lineno += 1
            self._advance()
            next = self._peek()

    def _next_char(self):
        c = self._peek()
        if c:
            self._advance() #will check if eof
            return c
        else:
            return None

    def next_token(self):
        """
        Scan the next Token and return it.
        """
        if self._eof:
            return None

        self._skip()

        c = self._next_char()
        if not c:
            return None

        t = None
        if c in string.punctuation:
            t = self._match_punctuation(c)
        if c in string.digits:
            t = self._match_numbers(c)
        if c in string.letters:
            t = self._match_identifier(c)

        if not t:
            return Token(Token_Type.UNKNOWN, c, self._lineno)

        if t.type == Token_Type.COMMENT:    # comments not show
            return None

        return t

    def _match_punctuation(self, c):
        """
        Match an operator.
        """
        if c in token.Dict['delimiter']:
            return Token(token.Dict['delimiter'][c], c, self._lineno, c)

        if c == '+':
            return Token(token.Dict['operator'][c], c, self._lineno, c)

        if c in '-/*':
            next = self._peek()
            if next == c:
                if next == '*':
                    self._advance()
                    return Token(token.Dict['operator']['**'], c+next, self._lineno, c)
                return self._match_comment(c)
            else:
                return Token(token.Dict['operator'][c], c, self._lineno, c)
        else:
            return None

    def _match_comment(self, c):
        """
        Match a single line comment.
        """
        comment = ''
        next = self._peek()
        if not next or next != c:
            return None
        self._advance()

        next = self._peek()
        while next and next != "\n":
            comment += next
            self._advance()
            next = self._peek()
        # self._advance()

        return Token(Token_Type.COMMENT, comment, self._lineno)

    def _match_numbers(self, c):
        s = c
        next = self._peek()
        while next and next in string.digits:
            s += next
            self._advance()
            next = self._peek()
        if next == '.':
            s += next
            self._advance()
            next = self._peek()
            while next and next in string.digits:
                s += next
                self._advance()
                next = self._peek()

        return Token(Token_Type.NUMBERS, s, self._lineno, float(s))

    def _match_identifier(self, c):
        """
        Match an identifier token.
        """
        s = c
        next = self._peek()
        while next and next in string.letters or next in string.digits:
            s += next
            self._advance()
            next = self._peek()

        if s in token.Dict['identifier']:
            value = None
            if token.Dict['identifier'][s] == Token_Type.CONSTANT:
                value = token.Constants[s]
            if token.Dict['identifier'][s] == Token_Type.FUNC:
                value = token.Functions[s]
            return Token(token.Dict['identifier'][s], s, self._lineno, value)
        else:
            return Token(Token_Type.UNKNOWN, s, self._lineno)


def test():
    for t in Lexer(
        """ -- 合法与非法输入的测试

            --  <2> 保留字,  参数
            ORIGIN  SCALE  ROT  IS  TO  STEP  DRAW  FOR  FROM  T

            -- <3> 分隔符和运算符: SEMICO, L_BRACKET, R_BRACKET, COMMA,	PLUS, MINUS, MUL, DIV, POWER,
            ; ( ) , + - * / **

            // <4> 常数：CONST_ID
            pi  e  3 3. 3333.333

            -- <1> 出错记号（非法输入）：ERRTOKEN
            -2 ? 0a orgian form  . $ % ^  & ***

            -- <5> 语句测试，为语法分析做准备
            FOR T FROM 0 TO 2*PI STEP PI/50 DRAW (cos(T),sin(T));

            -- 空记号（源程序结束）：NONTOKEN,
        """):
        print t

if __name__ == '__main__':
    test()