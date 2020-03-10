# main_handler.py --- 
# Filename: main_handler.py
# Description: 
# Author: Amritendu Mondal
# Email:  amritoit@gmail.com
# Organization:  IIT Madras
# Created: Wed Mar 11 00:21:25 2020 (+0530)
# Last-Updated: Wed Mar 11 00:32:51 2020 (+0530)
#           By: Amritendu Mondal
#     Update #: 8
# 
import json
import logging
import tornado.web

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        logging.info("recieved request for get stat")
        self.write({
            "id": 1,
            "success": True
        })
