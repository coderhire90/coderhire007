# -*- coding: utf-8 -*-
#!/bin/env python
#
"""
This module provide configure file management service in i18n environment.

# File   : index.py
# Author : zhuangsidai
# Date   : 2015-12-11 20:44:53
"""

import tornado.ioloop
import tornado.web
import tornado.autoreload
import base

class indexHandler(base.baseHandler):
    @tornado.web.authenticated
    def get(self):
        self.render(self.settings["tpl_path"] + "index.html")

