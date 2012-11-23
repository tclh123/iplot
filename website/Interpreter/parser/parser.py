#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    import os
    instance_path = os.path.abspath(os.path.dirname(__file__))
    print instance_path
    import sys
    sys.path.insert(0, '..')
    from lexer import lexer, token
else:
    from lexer import lexer, token

__author__ = 'tclh123'

import semantic
from expression import *

class Parser:
    def __init__(self, source):
        self.lexer = lexer.Lexer(source)
        self.tokens = []
        self.nodes = [] # stack holding the AST nodes

        # vars used by semantic
        self.param = { 'T' : 0.0 }

        # coord
        self.origin_x = 0.0
        self.origin_y = 0.0
        self.scale_x = 0.0
        self.scale_y = 0.0
        self.rot_angle = 0.0

    def parse(self):
        """
        Parse the input stream into an AST.
        """
        self.next_token()   # fetch first token
        self._sub_program() #loop

    def next_token(self):
        if self.lexer._eof:
            return

        try:
            self.next = self.lexer.next()
        except StopIteration:
            pass

        # Error 1
        if self.next.type ==  token.Token_Type.UNKNOWN:
            self._syntax_error(1)

#        if self.next:
#            self.tokens.append(self.next)
        return self.next

    def _syntax_error(self, error_id):
        """
        print syntax error
        """
#        print "error_id: %d" % error_id

    ######################################
    def _match_token(self, expect_token):
        if self.next.type != expect_token:
            self._syntax_error(2)
        self.next_token()   # move!

    def _sub_program(self):
        while not self.lexer._eof and self.next.type != token.Token_Type.UNKNOWN:
            self._sub_statement()
            self._match_token(token.Token_Type.SEMICOLON)

    def _sub_statement(self):
        if self.next.type == token.Token_Type.ORIGIN:
            self._sub_origin_statement()
        elif self.next.type == token.Token_Type.SCALE:
            self._sub_scale_statement()
        elif self.next.type == token.Token_Type.ROT:
            self._sub_rot_statement()
        elif self.next.type == token.Token_Type.FOR:
            self._sub_for_statement()
        else:
            self._syntax_error(2)

    def _sub_origin_statement(self):
        self._match_token(token.Token_Type.ORIGIN)
        self._match_token(token.Token_Type.IS)
        self._match_token(token.Token_Type.BRACKET_L)

        tmp1 = self.expression()    # expression tree
        self.origin_x = tmp1.eval()

        self._match_token(token.Token_Type.COMMA)

        tmp2 = self.expression()
        self.origin_y = tmp2.eval()

        self._match_token(token.Token_Type.BRACKET_R)

        print "origin is (%f, %f);" % (self.origin_x, self.origin_y)

    def _sub_scale_statement(self):
        self._match_token(token.Token_Type.SCALE)
        self._match_token(token.Token_Type.IS)
        self._match_token(token.Token_Type.BRACKET_L)

        tmp = self.expression()
        self.scale_x = tmp.eval()

        self._match_token(token.Token_Type.COMMA)

        tmp2 = self.expression()
        self.scale_y = tmp2.eval()

        self._match_token(token.Token_Type.BRACKET_R)
        print "scale is (%f, %f);" % (self.scale_x, self.scale_y)

    def _sub_rot_statement(self):
        self._match_token(token.Token_Type.ROT)
        self._match_token(token.Token_Type.IS)
        tmp = self.expression()

        self.rot_angle = tmp.eval()
        print "rot is %f;" % self.rot_angle

    def _sub_for_statement(self):
        self.param['T'] = 0.0

        self._match_token(token.Token_Type.FOR)
        self._match_token(token.Token_Type.VAR)
        self._match_token(token.Token_Type.FROM)

        start_node = self.expression()

        start = start_node.eval()

        self._match_token(token.Token_Type.TO)

        end_node = self.expression()

        end = end_node.eval()

        self._match_token(token.Token_Type.STEP)

        step_node = self.expression()

        step = step_node.eval()

        self._match_token(token.Token_Type.DRAW)
        self._match_token(token.Token_Type.BRACKET_L)

        x_exp = self.expression()   # the expression will be used in loop
        x = x_exp.eval()

        self._match_token(token.Token_Type.COMMA)

        y_exp = self.expression()
        y = y_exp.eval()

        self._match_token(token.Token_Type.BRACKET_R)

        semantic.draw_loop(self.param, start, end, step, x_exp, y_exp,      #TODO 绘图！
            self.scale_x, self.scale_y, self.rot_angle, self.origin_x, self.origin_y)
        x2 = x_exp.eval()
        y2 = y_exp.eval()
        print "for T from %f to %f step %f draw (%f, %f)->(%f, %f);" % (start, end, step, x, y, x2, y2) # debug msg(data before origin/rot/scale)

    ###############################

    def expression(self):
        left = self.term()
        while self.next.type == token.Token_Type.PLUS or self.next.type == token.Token_Type.MINUS:
            t = self.next
            self._match_token(t.type)
            right = self.term()
            left = BinaryOp(t.value, left, right)    #TODO
        return left

    def term(self):
        left = self.factor()
        while self.next.type == token.Token_Type.MUL or self.next.type == token.Token_Type.DIV:
            t = self.next
            self._match_token(t.type)
            right = self.factor()
            left = BinaryOp(t.value, left, right)    #TODO
        return left

    def factor(self):
        if self.next.type == token.Token_Type.PLUS:
            self._match_token(token.Token_Type.PLUS)
            right = self.factor()
        elif self.next.type == token.Token_Type.MINUS:
            self._match_token(token.Token_Type.MINUS)
            right = self.factor()
            left = Const(0.0)                           #TODO
            right = BinaryOp('-', left, right)       #TODO
        else:
            right = self.component()
        return right

    def component(self):
        left = self.atom()
        if self.next.type == token.Token_Type.POWER:
            self._match_token(token.Token_Type.POWER)
            right = self.component()
            left = BinaryOp('**', left, right)      #TODO
        return left

    def atom(self):
        address = None
        t = self.next
        if self.next.type == token.Token_Type.CONSTANT or self.next.type == token.Token_Type.NUMBERS:
            self._match_token(t.type)
            address = Const(t.value)   #TODO
        elif self.next.type == token.Token_Type.VAR:
            self._match_token(token.Token_Type.VAR)
            address = Parameter(self.param)          # pass by reference using dict #TODO
        elif self.next.type == token.Token_Type.FUNC:
            self._match_token(token.Token_Type.FUNC)
            self._match_token(token.Token_Type.BRACKET_L)

            tmp = self.expression()
            address = Func(t,tmp)             #TODO
            self._match_token(token.Token_Type.BRACKET_R)

        elif self.next.type == token.Token_Type.BRACKET_L:
            self._match_token(token.Token_Type.BRACKET_L)
            address = self.expression()
            self._match_token(token.Token_Type.BRACKET_R)
        else:
            self._syntax_error(2)

        return address

if __name__ == '__main__':
    case = 4
    p = Parser(
        ["""
        //test1
--------------- 函数f(t)=t的图形
-- origin is (200, 300);						-- 设置原点的偏移量
-- rot is pi/6;								-- 设置旋转角度
-- scale is (2, 1);							-- 设置横坐标和纵坐标的比例
for T from 0 to 200 step 1 draw (t, 0);		-- 横坐标的轨迹
for T from 0 to 180 step 1 draw (0, t);	-- 纵坐标的轨迹
for T from 0 to 150 step 1 draw (t, t);	-- 函数f(t)=t的轨迹
        """,
        """
        //test2
--------------- 图形1：
origin is (20, 200);									-- 设置原点的偏移量
rot is 0;												-- 不旋转
scale is (40, 40);										-- 设置比例
for T from 0 to 2*pi step pi/50 draw (t, -sin(t));		-- 画T的轨迹
origin is (20, 240);									-- 下移40单位
for T from 0 to 2*pi step pi/50 draw (t, -sin(t));		-- 画T的轨迹
origin is (20, 280);									-- 再下移40单位
for T from 0 to 2*pi step pi/50 draw (t, -sin(t));		-- 画T的轨迹

--------------- 图形2：
origin is (380, 240);									-- 右移
scale is (80, 80/3);									-- y方向压缩为三分之一
rot is pi/2+0*pi/3 ;									-- 旋转初值设置
for T from -pi to pi step pi/50 draw (cos(t), sin(t));	-- 画T的轨迹
rot is pi/2+2*pi/3;										-- 旋转2/3*pi
for T from -pi to pi step pi/50 draw (cos(t), sin(t));	-- 画T的轨迹
rot is pi/2-2*pi/3;										-- 再旋转2/3*pi
for T from -pi to pi step pi/50 draw (cos(t), sin(t));	-- 画T的轨迹

--------------- 图形3：
origin is(580, 240);									-- 再右移
scale is (80, 80);										-- 恢复原比例
rot is 0;												-- 不旋转
for t from 0 to 2*pi step pi/50 draw(cos(t),sin(t));	-- 画T的轨迹
for t from 0 to Pi*20 step Pi/50 draw					-- 画T的轨迹
   ((1-1/(10/7))*Cos(T)+1/(10/7)*Cos(-T*((10/7)-1)),
	(1-1/(10/7))*Sin(T)+1/(10/7)*Sin(-T*((10/7)-1)));
        """,
        """
        //test3
--------------- 函数复杂度图形：
rot is 0;										-- 不旋转
origin is (50, 400);							-- 设置新原点（距系统默认原点的偏移量）

scale is (2, 1);								-- 设置比例
for T from 0 to 300 step 1 draw (t, 0);			-- 横坐标
for T from 0 to 300 step 1 draw (0, -t);		-- 纵坐标

scale is (2, 1);								-- 设置比例
for T from 0 to 300 step 1 draw (t, -t);		-- 函数f(t)=t的轨迹

scale is (2, 0.1);								-- 设置比例
for T from 0 to 55 step 1 draw (t, -(t*t));		-- 函数f(t)=t*t的轨迹

scale is (10, 5);								-- 设置比例
for T from 0 to 60 step 1 draw (t, -sqrt(t));	-- 函数f(t)=sqrt(t)的轨迹

scale is (20, 0.1);								-- 设置比例
for T from 0 to 8 step 0.1 draw (t, -exp(t));	-- 函数f(t)=exp(t)的轨迹

scale is (2, 20);								-- 设置比例
//for T from 0 to 300 step 1 draw (t, -ln(t));	-- 函数f(t)=ln(t)的轨迹          //ln 函数暂时没实现。
        """,
        """
        //test4
origin is (350, 220);					-- 原点位置
rot is 0;						-- 旋转角度为零
scale is (100, 100);					-- 横、纵坐标比例因子
for t from 0 to 2*pi step pi/100 draw(cos(t), sin(t));	-- 画园
scale is (150, 150);  				        -- 横、纵坐标比例因子
for t from 0 to 2*pi step pi/150 draw(cos(t), sin(t));	-- 画园
scale is (200, 200);					-- 横、纵坐标比例因子
for t from 0 to 2*pi step pi/200 draw(cos(t), sin(t));	-- 画园
        """,
        """
        //test5
--------------- 测试f(t)=t*t与f(t)=t**2的图形：
rot is 0;										-- 不旋转
origin is (50, 400);							-- 设置新原点（距系统默认原点的偏移量）
scale is (1, 1);								-- 设置比例

for T from 0 to 300 step 1 draw (t, 0);			-- 横坐标
for T from 0 to 300 step 1 draw (0, -t);		-- 纵坐标

scale is (2, 0.1);								-- 设置比例
for T from 0 to 55 step 1 draw (t, -(t*t));		-- 函数f(t)=t*t的轨迹

origin is (150, 400);							-- 设置新原点（横坐标右移100）
for T from 0 to 55 step 1 draw (t, -(t**2));	-- 函数f(t)=t**2的轨迹
        """][case])
    p.parse()