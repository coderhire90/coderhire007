# -*- coding: utf-8 -*-
#!/bin/env python
#
"""
This module provide configure file management service in i18n environment.

# File   : dbobj.py
# Author : zhuangsidai
# Date   : 2015-12-11 20:34:50
"""

import os
import sys 
import mysql.connector
import ConfigParser
import log 

class dbConn:
    """ 
    DB connector, provide insert and execute method
    """
    def __init__(self, conf):
        self.conf = conf
        self.conn = None
        self.cursor = None
        self.config = {"host":self.conf["host"],
                "user":self.conf["user"],
                "password":self.conf["password"],
                "port":self.conf["port"],
                "database":self.conf["database"],
                "charset":self.conf["charset"]
                }   
        try:
            self.conn = mysql.connector.connect(**self.config)
            self.cursor = self.conn.cursor()
        except mysql.connector.Error, e:
            raise
            log.logging.error("Error %d: %s" % (e.args[0], e.args[1]))
            self.conn.close()

    def __del__(self):
        if (self.cursor != None):
            self.cursor.close()
        if (self.conn != None):
            self.conn.close()

    def insert(self, table, pattern, values):
        try:
            sql = 'insert into ' + table + ' values(' + pattern + ')'
            self.cursor.execute(sql, tuple(values))
            self.conn.commit()
        except mysql.connector.Error, e:
            log.logging.error("Error %d: %s" % (e.args[0], e.args[1]))

    def execute(self, cmd):
        res = None
        try:
            self.cursor.execute(cmd)
            res = self.cursor.fetchall()
            self.conn.commit()
        except mysql.connector.Error, e:
            log.logging.error("Error %d: %s" % (e.args[0], e.args[1]))
        return res

    def execute_nofetch(self, cmd):
        try:
            self.cursor.execute(cmd)
            self.conn.commit()
        except mysql.connector.Error, e:
            log.logging.error("Error %d: %s" % (e.args[0], e.args[1]))

class dbObj(object):
    """
    DB operator object
    """
    def __init__(self, conf):
        self.conf = conf
        self.db_conn = dbConn(conf)

    def get_progress(self, t, v):
        log.logging.info("entry: %s", sys._getframe().f_code.co_name)
        if type(v) != type({}):
            log.logging.error("records is not a dict")
            return
        sql = 'select progress from ' + t + ' where idkey="' + v["idkey"] + '"'
        return self.db_conn.execute(sql)[0]
