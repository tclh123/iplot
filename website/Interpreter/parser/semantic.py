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

def draw_loop(param, start, end, step, x_exp, y_exp, scale_x, scale_y, rot_angle, origin_x, origin_y):
    for i in common.frange(start, end+step, step):
        param['T'] = i
        x, y = calc_coord(x_exp, y_exp, scale_x, scale_y, rot_angle, origin_x, origin_y)
        draw_pixel(x, y)
#        print 'var is %f' % var
    pass

def draw_pixel(x, y):
    pass