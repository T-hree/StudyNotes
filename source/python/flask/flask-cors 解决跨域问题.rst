flask-cors 解决跨域问题
=======================

CORS的全称是\ `Cross-Origin Resource
Sharing <https://www.w3.org/TR/cors/>`__
，有w3c组织制定的，现在这个规范，已经被大多数浏览器支持，处理跨域的需求。

CORS需要后端应用进行配置，因此，这是一种后端跨域的配置方式，这种方式很容易理解，一个陌生的请求来访问你的服务器，自然需要进行授权。。。

.. _1安装flask-cors-包:

1、安装flask-cors 包
--------------------

.. code:: shell

   pip install flask-cors 

.. _2从flaskcors模块中引入类-cors-:

2、从flask_cors模块中引入类 CORS ：
-----------------------------------

.. code:: python

   from flask_cors import CORS

.. _3flask-配置跨域-cors有两种方式还有一种方式最后讲）:

3、flask 配置跨域 Cors有两种方式（还有一种方式最后讲）：
--------------------------------------------------------

**（1）使用CORS类**
**（适用于全局的api接口配置，也就是所有的路由都支持跨域了）**

.. code:: python

   from flask import Flask
   from flask_cors import CORS, cross_origin
   app = Flask(__name__)
   cors = CORS(app)

**下边是CORS类可配置的参数：**

.. code:: python

   DEFAULT_OPTIONS = dict(
        origins='*', # 配置允许跨域访问的源，*表示全部允许 Access-Control-Allow-Origin
        methods=ALL_METHODS,  # ALL_METHODS=['GET', 'HEAD', 'POST', 'OPTIONS', 'PUT', 'PATCH', 'DELETE']   Access-Control-Allow-Methods
        allow_headers='*',  # 配置允许跨域的请求头 Access-Control-Request-Headers
        expose_headers=None, # 自定义请求响应的Head信息 Access-Control-Expose-Headers
        supports_credentials=False, # 是否允许请求发送cookie，false是不允许 Access-Control-Allow-Credentials
        max_age=None, # 	预检请求的有效时长 Access-Control-Max-Age
        send_wildcard=False,
        automatic_options=True,
        vary_header=True,
        resources=r'/*',  # 	全局配置允许跨域的API接口 
        intercept_exceptions=True,
        always_send=True) # 默认配置

**（2）使用@cross_origin装饰器\***\ \*（适用于配置特定的api接口）*\*

.. code:: python

   from flask import Flask
   from flask_cors import CORS, cross_origin
   app = Flask(__name__)
    
   # 只允许路径为'/login'跨域！
   @app.route('/login')
   @cross_origin()
   def data():
       return jsonify({'name':'lxc'})

装饰器的参数大致与类相同

.. _4将cors与cookie一起使用:

4、将CORS与Cookie一起使用：
---------------------------

**默认情况下，不允许跨站点提交Cookie，如果你希望服务器允许用户跨源发出Cookie或经过身份验证的请求，那只需把supports_credentials**
**设置为True即可。。。**

.. code:: python

   from flask import Flask, session
   from flask_cors import CORS
    
   app = Flask(__name__)
   CORS(app, supports_credentials=True)
    
   @app.route("/")
   def helloWorld():
     return "Hello, %s" % session['username']

.. _5将cors与蓝图blueprint一起使用:

5、将CORS与蓝图blueprint一起使用：
----------------------------------

flask-cors同样也支持蓝图，只需要将一个蓝图实例传递给CORS类即可

.. code:: python

   from flask import Blueprint
   from flask import render_template
   from flask_cors import CORS, cross_origin
   blue = Blueprint('user',__name__)
   cors = CORS(blue)
    
   @blue.route('/')
   def fn():
       return render_template('html.html')

.. _6配置access-control-allow-origin响应头添加header）:

6、配置\ **Access-Control-Allow-Origin（响应头添加header）**\ ：
----------------------------------------------------------------

.. code:: python

    
   @app.after_request
   def after(resp):
       '''
       被after_request钩子函数装饰过的视图函数 
       ，会在请求得到响应后返回给用户前调用，也就是说，这个时候，
       请求已经被app.route装饰的函数响应过了，已经形成了response，这个时
       候我们可以对response进行一些列操作，我们在这个钩子函数中添加headers，所有的url跨域请求都会允许！！！
       '''
       resp = make_response(resp)
       resp.headers['Access-Control-Allow-Origin'] = '*'
       resp.headers['Access-Control-Allow-Methods'] = 'GET,POST'
       resp.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
       return resp

**也可以在普通视图函数中添加headers，根据自己的需求来。**
