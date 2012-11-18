#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tclh123'

import math

class Token_Type:
    (
    # reserved words
    ORIGIN,
    SCALE,
    ROT,
    IS,
    TO,
    STEP,
    DRAW,
    FOR,
    FROM,
    VAR,  # T
#    COLOR, # colors

    # delimiter
    SEMICOLON,
    BRACKET_L,
    BRACKET_R,
    COMMA,

    COMMENT,

    # operator
    PLUS,
    MINUS,
    MUL,
    DIV,
    POWER,

    # functions
    FUNC,

    #datas
    CONSTANT,   # constant vars
    NUMBERS,

    # FLAGS
    UNKNOWN
    ) = range(24)

    name = [
        # reserved words
        'ORIGIN',
        'SCALE',
        'ROT',
        'IS',
        'TO',
        'STEP',
        'DRAW',
        'FOR',
        'FROM',
        'VAR',  # T
        #    COLOR, # colors

        # delimiter
        'SEMICOLON',
        'BRACKET_L',
        'BRACKET_R',
        'COMMA',

        'COMMENT',

        # operator
        'PLUS',
        'MINUS',
        'MUL',
        'DIV',
        'POWER',

        # functions
        'FUNC',

        #datas
        'CONSTANT',   # constant vars
        'NUMBERS',

        # FLAGS
        'UNKNOWN'
    ]
    @staticmethod
    def str(i):
        return Token_Type.name[i]

Dict = {
    'delimiter' :{
        ';'     :   Token_Type.SEMICOLON,
        ','     :   Token_Type.COMMA,
        '('     :   Token_Type.BRACKET_L,
        ')'     :   Token_Type.BRACKET_R,
    },
    'operator'  :{
        '+'     :   Token_Type.PLUS,
        '-'     :   Token_Type.MINUS,
        '*'     :   Token_Type.MUL,
        '/'     :   Token_Type.DIV,
        '**'    :   Token_Type.POWER
    },
    'comment'   :{
        '//'    :   Token_Type.COMMENT,
        '--'    :   Token_Type.COMMENT
    },
    'identifier':{
        'T'     :   Token_Type.VAR,

        'SIN'   :   Token_Type.FUNC,
        'COS'   :   Token_Type.FUNC,
        'TAN'   :   Token_Type.FUNC,
        'LN'    :   Token_Type.FUNC,
        'EXP'   :   Token_Type.FUNC,
        'SQRT'  :   Token_Type.FUNC,

        'ORIGIN':   Token_Type.ORIGIN,
        'SCALE' :   Token_Type.SCALE,
        'ROT'   :   Token_Type.ROT,
        'IS'    :   Token_Type.IS,
        'FOR'   :   Token_Type.FOR,
        'FROM'  :   Token_Type.FROM,
        'TO'    :   Token_Type.TO,
        'STEP'  :   Token_Type.STEP,
        'DRAW'  :   Token_Type.DRAW,

        'PI'    :   Token_Type.CONSTANT,
        'E'     :   Token_Type.CONSTANT
    }
}

Constants = {   # Token_Type.CONSTANT
                'PI'    :   3.1415926,
                'E'     :   2.71828
}

Functions = {
    'SIN'   :   math.sin,
    'COS'   :   math.cos,
    'TAN'   :   math.tan,
    'LN'    :   math.log,   # ???
    'EXP'   :   math.exp,
    'SQRT'  :   math.sqrt,
}

class Token:
    def __init__(self, type, lexeme=None, lineno=None, value=None):
        self.type = type
        self.value = value
        self.lexeme = lexeme
        self.lineno = lineno

    def __str__(self):
        return "(%s, %s, %s, %d)" % (Token_Type.str(self.type), self.lexeme, str(self.value), self.lineno)