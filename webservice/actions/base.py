# -*- coding: utf-8 -*-
#!/bin/env python
#
"""
This module provide configure file management service in i18n environment.

# File   : base.py
# Author : zhuangsidai
# Date   : 2015-12-11 20:45:24
"""

import tornado.ioloop
import tornado.web
import tornado.autoreload
import urllib
import urllib2
import re
from utils import conf

class baseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return "zhuangsidai"
