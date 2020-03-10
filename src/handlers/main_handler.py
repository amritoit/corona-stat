# main_handler.py --- 
# Filename: main_handler.py
# Description: 
# Author: Amritendu Mondal
# Email:  amritoit@gmail.com
# Organization:  IIT Madras
# Created: Wed Mar 11 00:21:25 2020 (+0530)
# Last-Updated: Wed Mar 11 00:49:39 2020 (+0530)
#           By: Amritendu Mondal
#     Update #: 9
# 
import json
import logging
import tornado.web

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        logging.info("recieved request for get stat")
        self.write({
            "name": "Mumpi",
            "current_mood": "Kharus"
        })
