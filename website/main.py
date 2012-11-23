#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import json
from Interpreter import *

render = web.template.render('templates')

urls = (
    '/', 'Index',
    '/service', 'Service'
    )

def testlexer():
    s = ''
    for t in lexer.Lexer(
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
        s += str(t)
    return s

def testparser():
    case = 2
    p = parser.Parser(
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
    return p.output

class Index:
    def GET(self):
        """
        """
        form = my_form()
        return render.index(form, "Your text goes here.")
        return 'welcome to wbmsg | code by tclh123'
#    def POST(self):
#        form = my_form()
#        form.validates()
#        s = form.value['textfield']
#        return s

class Service:
    def POST(self):
        form = my_form()
        form.validates()
        source = form.value['textfield']
        p = parser.Parser(source)
        p.parse()
        return json.dumps(p.output)
        return json.dumps(testparser())
        return 'Service'

my_form = web.form.Form(
    web.form.Textarea('', class_='textfield', id='textfield', placeholder="Input your source code here!")
)

app = web.application(urls, globals()).wsgifunc()