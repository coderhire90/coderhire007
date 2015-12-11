# -*- coding: utf-8 -*-
#!/bin/env python
#
"""
This module provide configure file management service in i18n environment.

# File   : server.py
# Author : zhuangsidai
# Date   : 2015-12-11 20:25:00
"""

import tornado.ioloop
import tornado.web
import tornado.autoreload
import sys 
import os
from utils import log 
from utils import conf
from actions import index

def init():
    log.init_log(conf.log_path, conf.log_level)

init()

settings = { 
"static_path": os.path.join(conf.base_path, "webroot/static/"),
"tpl_path": os.path.join(conf.base_path, "webroot/tpl/"),
"debug": True,
"conf": conf,
"login_url": conf.login_service,
}

application = tornado.web.Application([
    (r"/", index.indexHandler),
],**settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

