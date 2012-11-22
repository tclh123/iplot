#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tclh123'

import operator

class Node(object):
    """
    A Node represents a node in an expression(abstract syntax tree).
    """
#    def __init__(self, token):
#        self.value = token.value
#        self.child = None
#        self.sibling = None
#
#    def __iter__(self):
#        return self
#
#    def next(self):
#        """
#        Return the next child Node.
#        """
#        raise StopIteration
#
#    def __str__(self):
#        return "<Node: %s>" % self.value
#
#    def eval(self, env):
#        pass

class BinaryOp(Node):
    """
    Represents a binary expression.
    """
    ops = {
        "+":   operator.add,
        "-":   operator.sub,
        "*":   operator.mul,
        "/":   operator.div,
        "**":  operator.pow
    }

    def __init__(self, value, left, right):
        self.operator = value # 字符串
        self.left = left
        self.right = right

    def __iter__(self):
        return self

    def next(self):
        yield self.left
        yield self.right
        raise StopIteration

    def __str__(self):
        return "<BinaryOp: %s>" % self.operator

    def eval(self):
        return BinaryOp.ops[self.operator](self.left.eval(), self.right.eval())

class Func(Node):
    def __init__(self, token, child):
        self.func = token.value
        self.child = child

    def eval(self):
        return self.func(self.child.eval())

class Const(Node):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

class Parameter(Node):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value   # ParaPtr??