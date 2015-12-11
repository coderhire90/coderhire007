# -*- coding: utf-8 -*-
#!/bin/env python
#
"""
This module provide configure file management service in i18n environment.

# File   : conf.py
# Author : zhuangsidai
# Date   : 2015-12-11 20:31:00
"""

import ConfigParser
import sys 
import os

base_path = os.path.dirname(os.path.abspath(__file__)) + "/../../"
conffile = base_path + "conf/service.conf"
cf = ConfigParser.ConfigParser()
cf.read(conffile)

log_path = base_path + cf.get("webservice", "log_path")
log_level = cf.getint("webservice", "log_level")

#cas
login_service = cf.get("webservice", "login_service")
validate_service = cf.get("webservice", "validate_service")

#jobmanager

db_conf = {}
db_conf["host"] = cf.get("db", "host")
db_conf["port"] = cf.getint("db", "port")
db_conf["user"] = cf.get("db", "user")
db_conf["password"] = cf.get("db", "password")
db_conf["database"] = cf.get("db", "database")
db_conf["charset"] = cf.get("db", "charset")

