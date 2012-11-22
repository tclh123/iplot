#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tclh123'

import math

def calc_coord(x_exp, y_exp, scale_x, scale_y, rot_angle, origin_x, origin_y):
    """
    compute value from expression.
    """
    x = x_exp.eval()
    y = y_exp.eval()
    x *= scale_x
    y *= scale_y
    x = x*math.cos(rot_angle) + y*math.sin(rot_angle)
    y = y*math.cos(rot_angle) - y*math.sin(rot_angle)
    x += origin_x
    y += origin_y

    return x, y

def draw_loop(start, end, step, x_exp, y_exp):
    # for()

    # TODO python 怎么实现 浮点 步长？
    pass

#void DrawLoop(double Start,
#                     double End,
#                            double Step,
#                                   struct ExprNode * HorPtr,
#                                          struct ExprNode * VerPtr)
#{	extern double Parameter;
#double x, y;
#for(Parameter = Start; Parameter <= End; Parameter += Step)
#{	CalcCoord(HorPtr, VerPtr, x, y);
#DrawPixel((unsigned long)x, (unsigned long)y);
#}
#}