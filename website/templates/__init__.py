from web.template import CompiledTemplate, ForLoop, TemplateResult


# coding: utf-8
def index (form, text):
    __lineoffset__ = -4
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'<html>\n'])
    extend_([u'\n'])
    extend_([u'<head>\n'])
    extend_([u'    <title>Hello</title>\n'])
    extend_([u'    <link rel="stylesheet" type="text/css" href="/static/site.css" />\n'])
    extend_([u'    <link rel="stylesheet" type="text/css" href="/static/iplot.css" />\n'])
    extend_([u'\n'])
    extend_([u'    <script type="text/javascript" src="/static/jquery-1.8.3.min.js"></script>\n'])
    extend_([u'    <script type="text/javascript" src="/static/jquery.autosize-min.js"></script>\n'])
    extend_([u'\n'])
    extend_([u'    <script type="text/javascript">\n'])
    extend_([u'        (function(doc, win){\n'])
    extend_([u'            var canvas = null;\n'])
    extend_([u'\n'])
    extend_([u'            ', u'$', u'(doc).ready(function() {\n'])
    extend_([u'                ', u'$', u"('#textfield').autosize();\n"])
    extend_([u'                ', u'$', u"('#example').change(function(){\n"])
    extend_([u'                    var list = ["//test1\\n'])
    extend_([u'                        --------------- \u51fd\u6570f(t)=t\u7684\u56fe\u5f62\\n'])
    extend_([u'                        -- origin is (200, 300);                                                -- \u8bbe\u7f6e\u539f\u70b9\u7684\u504f\u79fb\u91cf\\n'])
    extend_([u'                    -- rot is pi/6;                                                             -- \u8bbe\u7f6e\u65cb\u8f6c\u89d2\u5ea6\\n'])
    extend_([u'                    -- scale is (2, 1);                                                 -- \u8bbe\u7f6e\u6a2a\u5750\u6807\u548c\u7eb5\u5750\u6807\u7684\u6bd4\u4f8b\\n'])
    extend_([u'                    for T from 0 to 200 step 1 draw (t, 0);             -- \u6a2a\u5750\u6807\u7684\u8f68\u8ff9\\n'])
    extend_([u'                    for T from 0 to 180 step 1 draw (0, t);     -- \u7eb5\u5750\u6807\u7684\u8f68\u8ff9\\n'])
    extend_([u'                    for T from 0 to 150 step 1 draw (t, t);     -- \u51fd\u6570f(t)=t\u7684\u8f68\u8ff9\\n'])
    extend_([u'                    ",\n'])
    extend_([u'                    "//test2\\n'])
    extend_([u'                    --------------- \u56fe\u5f621\uff1a\\n'])
    extend_([u' origin is (20, 200);                                                                   -- \u8bbe\u7f6e\u539f\u70b9\u7684\u504f\u79fb\u91cf\\n'])
    extend_([u'                    rot is 0;                                                                                           -- \u4e0d\u65cb\u8f6c\\n'])
    extend_([u'                    scale is (40, 40);                                                                          -- \u8bbe\u7f6e\u6bd4\u4f8b\\n'])
    extend_([u'                    for T from 0 to 2*pi step pi/50 draw (t, -sin(t));          -- \u753bT\u7684\u8f68\u8ff9\\n'])
    extend_([u'                    origin is (20, 240);                                                                        -- \u4e0b\u79fb40\u5355\u4f4d\\n'])
    extend_([u'                    for T from 0 to 2*pi step pi/50 draw (t, -sin(t));          -- \u753bT\u7684\u8f68\u8ff9\\n'])
    extend_([u'                    origin is (20, 280);                                                                        -- \u518d\u4e0b\u79fb40\u5355\u4f4d\\n'])
    extend_([u'                    for T from 0 to 2*pi step pi/50 draw (t, -sin(t));          -- \u753bT\u7684\u8f68\u8ff9\\n'])
    extend_([u'\\n'])
    extend_([u'                    --------------- \u56fe\u5f622\uff1a\\n'])
    extend_([u' origin is (380, 240);                                                                  -- \u53f3\u79fb\\n'])
    extend_([u'                    scale is (80, 80/3);                                                                        -- y\u65b9\u5411\u538b\u7f29\u4e3a\u4e09\u5206\u4e4b\u4e00\\n'])
    extend_([u'                    rot is pi/2+0*pi/3 ;                                                                        -- \u65cb\u8f6c\u521d\u503c\u8bbe\u7f6e\\n'])
    extend_([u'                    for T from -pi to pi step pi/50 draw (cos(t), sin(t));      -- \u753bT\u7684\u8f68\u8ff9\\n'])
    extend_([u'                    rot is pi/2+2*pi/3;                                                                         -- \u65cb\u8f6c2/3*pi\\n'])
    extend_([u'                    for T from -pi to pi step pi/50 draw (cos(t), sin(t));      -- \u753bT\u7684\u8f68\u8ff9\\n'])
    extend_([u'                    rot is pi/2-2*pi/3;                                                                         -- \u518d\u65cb\u8f6c2/3*pi\\n'])
    extend_([u'                    for T from -pi to pi step pi/50 draw (cos(t), sin(t));      -- \u753bT\u7684\u8f68\u8ff9\\n'])
    extend_([u'\\n'])
    extend_([u'                    --------------- \u56fe\u5f623\uff1a\\n'])
    extend_([u' origin is(580, 240);                                                                   -- \u518d\u53f3\u79fb\\n'])
    extend_([u'                    scale is (80, 80);                                                                          -- \u6062\u590d\u539f\u6bd4\u4f8b\\n'])
    extend_([u'                    rot is 0;                                                                                           -- \u4e0d\u65cb\u8f6c\\n'])
    extend_([u'                    for t from 0 to 2*pi step pi/50 draw(cos(t),sin(t));        -- \u753bT\u7684\u8f68\u8ff9\\n'])
    extend_([u'                    for t from 0 to Pi*20 step Pi/50 draw                                       -- \u753bT\u7684\u8f68\u8ff9\\n'])
    extend_([u'                            ((1-1/(10/7))*Cos(T)+1/(10/7)*Cos(-T*((10/7)-1)),\\n'])
    extend_([u'                                    (1-1/(10/7))*Sin(T)+1/(10/7)*Sin(-T*((10/7)-1)));\\n'])
    extend_([u'                    ",\n'])
    extend_([u'                    "//test3\\n'])
    extend_([u'                    --------------- \u51fd\u6570\u590d\u6742\u5ea6\u56fe\u5f62\uff1a\\n'])
    extend_([u' rot is 0;                                                                              -- \u4e0d\u65cb\u8f6c\\n'])
    extend_([u'                    origin is (50, 400);                                                        -- \u8bbe\u7f6e\u65b0\u539f\u70b9\uff08\u8ddd\u7cfb\u7edf\u9ed8\u8ba4\u539f\u70b9\u7684\u504f\u79fb\u91cf\uff09\\n'])
    extend_([u'\\n'])
    extend_([u' scale is (2, 1);                                                               -- \u8bbe\u7f6e\u6bd4\u4f8b\\n'])
    extend_([u'                    for T from 0 to 300 step 1 draw (t, 0);                     -- \u6a2a\u5750\u6807\\n'])
    extend_([u'                    for T from 0 to 300 step 1 draw (0, -t);            -- \u7eb5\u5750\u6807\\n'])
    extend_([u'\\n'])
    extend_([u'                    scale is (2, 1);                                                            -- \u8bbe\u7f6e\u6bd4\u4f8b\\n'])
    extend_([u'                    for T from 0 to 300 step 1 draw (t, -t);            -- \u51fd\u6570f(t)=t\u7684\u8f68\u8ff9\\n'])
    extend_([u'\\n'])
    extend_([u'                    scale is (2, 0.1);                                                          -- \u8bbe\u7f6e\u6bd4\u4f8b\\n'])
    extend_([u'                    for T from 0 to 55 step 1 draw (t, -(t*t));         -- \u51fd\u6570f(t)=t*t\u7684\u8f68\u8ff9\\n'])
    extend_([u'\\n'])
    extend_([u'                    scale is (10, 5);                                                           -- \u8bbe\u7f6e\u6bd4\u4f8b\\n'])
    extend_([u'                    for T from 0 to 60 step 1 draw (t, -sqrt(t));       -- \u51fd\u6570f(t)=sqrt(t)\u7684\u8f68\u8ff9\\n'])
    extend_([u'\\n'])
    extend_([u'                    scale is (20, 0.1);                                                         -- \u8bbe\u7f6e\u6bd4\u4f8b\\n'])
    extend_([u'                    for T from 0 to 8 step 0.1 draw (t, -exp(t));       -- \u51fd\u6570f(t)=exp(t)\u7684\u8f68\u8ff9\\n'])
    extend_([u'\\n'])
    extend_([u'                    scale is (2, 20);                                                           -- \u8bbe\u7f6e\u6bd4\u4f8b\\n'])
    extend_([u'                    //for T from 0 to 300 step 1 draw (t, -ln(t));      -- \u51fd\u6570f(t)=ln(t)\u7684\u8f68\u8ff9          //ln \u51fd\u6570\u6682\u65f6\u6ca1\u5b9e\u73b0\u3002\\n'])
    extend_([u'                    ",\n'])
    extend_([u'                    "//test4\\n'])
    extend_([u'                    origin is (350, 220);                                       -- \u539f\u70b9\u4f4d\u7f6e\\n'])
    extend_([u'                    rot is 0;                                           -- \u65cb\u8f6c\u89d2\u5ea6\u4e3a\u96f6\\n'])
    extend_([u'                    scale is (100, 100);                                        -- \u6a2a\u3001\u7eb5\u5750\u6807\u6bd4\u4f8b\u56e0\u5b50\\n'])
    extend_([u'                    for t from 0 to 2*pi step pi/100 draw(cos(t), sin(t));      -- \u753b\u56ed\\n'])
    extend_([u'                    scale is (150, 150);                                        -- \u6a2a\u3001\u7eb5\u5750\u6807\u6bd4\u4f8b\u56e0\u5b50\\n'])
    extend_([u'                    for t from 0 to 2*pi step pi/150 draw(cos(t), sin(t));      -- \u753b\u56ed\\n'])
    extend_([u'                    scale is (200, 200);                                        -- \u6a2a\u3001\u7eb5\u5750\u6807\u6bd4\u4f8b\u56e0\u5b50\\n'])
    extend_([u'                    for t from 0 to 2*pi step pi/200 draw(cos(t), sin(t));      -- \u753b\u56ed\\n'])
    extend_([u'                    ",\n'])
    extend_([u'                    "//test5\\n'])
    extend_([u'                    --------------- \u6d4b\u8bd5f(t)=t*t\u4e0ef(t)=t**2\u7684\u56fe\u5f62\uff1a\\n'])
    extend_([u' rot is 0;                                                                              -- \u4e0d\u65cb\u8f6c\\n'])
    extend_([u'                    origin is (50, 400);                                                        -- \u8bbe\u7f6e\u65b0\u539f\u70b9\uff08\u8ddd\u7cfb\u7edf\u9ed8\u8ba4\u539f\u70b9\u7684\u504f\u79fb\u91cf\uff09\\n'])
    extend_([u' scale is (1, 1);                                                               -- \u8bbe\u7f6e\u6bd4\u4f8b\\n'])
    extend_([u'\\n'])
    extend_([u'                    for T from 0 to 300 step 1 draw (t, 0);                     -- \u6a2a\u5750\u6807\\n'])
    extend_([u'                    for T from 0 to 300 step 1 draw (0, -t);            -- \u7eb5\u5750\u6807\\n'])
    extend_([u'\\n'])
    extend_([u'                    scale is (2, 0.1);                                                          -- \u8bbe\u7f6e\u6bd4\u4f8b\\n'])
    extend_([u'                    for T from 0 to 55 step 1 draw (t, -(t*t));         -- \u51fd\u6570f(t)=t*t\u7684\u8f68\u8ff9\\n'])
    extend_([u'\\n'])
    extend_([u'                    origin is (150, 400);                                                       -- \u8bbe\u7f6e\u65b0\u539f\u70b9\uff08\u6a2a\u5750\u6807\u53f3\u79fb100\uff09\\n'])
    extend_([u' for T from 0 to 55 step 1 draw (t, -(t**2));   -- \u51fd\u6570f(t)=t**2\u7684\u8f68\u8ff9\\n'])
    extend_([u'                    "];\n'])
    extend_([u'                    ', u'$', u'("#textfield").get(0).value = list[', u'$', u'("#example").val()-1];\n'])
    extend_([u'                    work();\n'])
    extend_([u'                });\n'])
    extend_([u'                ', u'$', u"('#debug').live('click', function () //\u56e0\u4e3a\u901a\u8fc7ajax\u52a0\u8f7d\u540e\u7684dom,\u8fd9\u8fb9\u7528live\n"])
    extend_([u'                {\n'])
    extend_([u'                    var div2 = ', u'$', u"('#foo');\n"])
    extend_([u"                    if (div2.is(':visible')) //\u5982\u679cid\u4e3adiv2\u7684\u533a\u57df\u663e\u793a\n"])
    extend_([u'                    {\n'])
    extend_([u'                        div2.hide(); //\u9690\u85cf\n'])
    extend_([u'                    }\n'])
    extend_([u'                    else\n'])
    extend_([u'                    {\n'])
    extend_([u'                        div2.show();\n'])
    extend_([u'                    }\n'])
    extend_([u'                });\n'])
    extend_([u'                ', u'$', u'("#clear").click(function(){\n'])
    extend_([u"                    canvas.getContext('2d').clearRect(0,0,canvas.width,canvas.height);\n"])
    extend_([u'                    ', u'$', u"('#foo').html('');\n"])
    extend_([u'                });\n'])
    extend_([u'\n'])
    extend_([u'                ', u'$', u'("#textfield").keyup(work);\n'])
    extend_([u'                //', u'$', u'("#textfield").onpaste(work);   //no onpaste?\n'])
    extend_([u'                //', u'$', u'(".button").click(work);\n'])
    extend_([u'\n'])
    extend_([u'                canvas = ', u'$', u'("canvas#canvas").get(0);\n'])
    extend_([u'\n'])
    extend_([u'            });//end ready\n'])
    extend_([u'\n'])
    extend_([u'            var work = function() {\n'])
    extend_([u'                var input_string = ', u'$', u'("#textfield").val();\n'])
    extend_([u'                ', u'$', u'.ajax({\n'])
    extend_([u'                    url: "/service",\n'])
    extend_([u'                    type: "POST",\n'])
    extend_([u'                    data: {textfield : input_string},\n'])
    extend_([u'                    success: function(data) {\n'])
    extend_([u'                        ', u'$', u"('#foo').html(data).hide().fadeIn(1500);\n"])
    extend_([u"                        var obj = eval('('+data+')');\n"])
    extend_([u"                        var draw = new Draw(canvas, obj['draw']);\n"])
    extend_([u'                    }\n'])
    extend_([u'                });\n'])
    extend_([u'                return false;\n'])
    extend_([u'            };\n'])
    extend_([u'\n'])
    extend_([u'            function Draw(canvas, arr) {\n'])
    extend_([u'                this.canvas = canvas;\n'])
    extend_([u'                this.init(arr);\n'])
    extend_([u'            }\n'])
    extend_([u'\n'])
    extend_([u'            Draw.prototype = {\n'])
    extend_([u'                init: function(arr) {\n'])
    extend_([u"                    this.context = this.canvas.getContext('2d');\n"])
    extend_([u'                    this.arr = arr;\n'])
    extend_([u'                    this.run();\n'])
    extend_([u'                },\n'])
    extend_([u'                run: function(){\n'])
    extend_([u'                    for(var i=0; i<this.arr.length; i++){\n'])
    extend_([u'                        this.drawing(this.arr[i][0], this.arr[i][1]);\n'])
    extend_([u'                    }\n'])
    extend_([u'                },\n'])
    extend_([u'                drawing: function(x,y) {\n'])
    extend_([u"                    //console.log('drawing('+x+','+y+')');\n"])
    extend_([u'                    this.context.beginPath();\n'])
    extend_([u'                    this.context.moveTo(x,y);\n'])
    extend_([u'                    this.context.lineTo(x+1,y+1);\n'])
    extend_([u'                    this.context.stroke();\n'])
    extend_([u'                }\n'])
    extend_([u'            };\n'])
    extend_([u'        })(document, window)\n'])
    extend_([u'    </script>\n'])
    extend_([u'</head>\n'])
    extend_([u'\n'])
    extend_([u'<body>\n'])
    extend_([u'<div id="container">\n'])
    extend_([u'    <h1><span itemprop="name">iplot</span> <small itemprop="description">A simple plotting language.</small></h1>\n'])
    extend_([u'    <h3>Soucre Code</h3>\n'])
    extend_([u'    <form class="form" method="post">\n'])
    extend_([u'        ', escape_(form.render(), False), u'\n'])
    extend_([u'        <!--<input class="button" type="submit" value="send"/>-->\n'])
    extend_([u'    </form>\n'])
    extend_([u'    <p id="note"><strong>Example</strong>:\n'])
    extend_([u'        <select id="example">\n'])
    extend_([u'            <option value=1>Test - 1</option>\n'])
    extend_([u'            <option value=2>Test - 2</option>\n'])
    extend_([u'            <option value=3>Test - 3</option>\n'])
    extend_([u'            <option value=4>Test - 4</option>\n'])
    extend_([u'            <option value=5>Test - 5</option>\n'])
    extend_([u'        </select>\n'])
    extend_([u'    </p>\n'])
    extend_([u'    <h3>Graph / <a id="clear" href="#">clear</a></h3>\n'])
    extend_([u'    <canvas id="canvas" width="1000" height="500"></canvas>\n'])
    extend_([u'    <h3 id="debug">Json.data</h3>\n'])
    extend_([u'    <p id="foo" style="display: none;">Json data goes here.</p>\n'])
    extend_([u'    <p id="madeby" itemprop="author" itemscope="" itemtype="http://schema.org/Person">Made by \xa9 <a itemprop="url" href="http://tclh123.com/"><strong itemprop="name">tclh123</strong></a>, 2012-2013. / <a href="mailto:tclh123@gmail.com?subject=iplot" id="email"><strong>Email Me</strong></a>. / <a href="https://github.com/tclh123/iplot"><strong>Github</strong></a>.</p>\n'])
    extend_([u'    <div id="clicki_widget_4960" ></div>\n'])
    extend_([u'</div>\n'])
    extend_([u"<script type='text/javascript'>\n"])
    extend_([u'    (function() {\n'])
    extend_([u"        var c = document.createElement('script');\n"])
    extend_([u"        c.type = 'text/javascript';\n"])
    extend_([u'        c.async = true;\n'])
    extend_([u"        c.src = ('https:' == document.location.protocol ? 'https://' : 'http://') + 'www.clicki.cn/boot/47861';\n"])
    extend_([u"        var h = document.getElementsByTagName('script')[0];\n"])
    extend_([u'        h.parentNode.insertBefore(c, h);\n'])
    extend_([u'    })();\n'])
    extend_([u'</script>\n'])
    extend_([u'</body>\n'])
    extend_([u'</html>\n'])

    return self

index = CompiledTemplate(index, '../templates/index.html')
join_ = index._join; escape_ = index._escape

# coding: utf-8
def readme():
    __lineoffset__ = -5
    loop = ForLoop()
    self = TemplateResult(); extend_ = self.extend
    extend_([u'python web/template.py --compile templates\n'])

    return self

readme = CompiledTemplate(readme, '../templates/readme.txt')
join_ = readme._join; escape_ = readme._escape

