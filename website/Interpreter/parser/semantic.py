#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tclh123'

import math
import common

def calc_coord(x_exp, y_exp, scale_x, scale_y, rot_angle, origin_x, origin_y):
    """
    (compute value from expression.)
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

def draw_loop(parser, start, end, step, x_exp, y_exp):
    for i in common.frange(start, end+step, step):
        parser.param['T'] = i
        x, y = calc_coord(x_exp, y_exp, parser.scale_x, parser.scale_y, parser.rot_angle, parser.origin_x, parser.origin_y)
        draw_pixel(parser, x, y)

def draw_pixel(parser, x, y):
    parser.out('draw', (x,y))