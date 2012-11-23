#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tclh123'

def frange(start, end=None, inc=1.0):
    "A faster range-like function that does accept float increments..."
    if end == None:
        end = start + 0.0
        start = 0.0
    else: start += 0.0 # force it to be a float

    count = int((end - start) / inc)
    if start + count * inc != end:
        # Need to adjust the count. AFAICT, it always comes up one short.
        count += 1

    L = [start] * count
    for i in xrange(1, count):
        L[i] = start + i * inc

    return L