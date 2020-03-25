# main_handler.py --- 
# Filename: main_handler.py
# Description: 
# Author: Amritendu Mondal
# Email:  amritoit@gmail.com
# Organization:  IIT Madras
# Created: Wed Mar 11 00:21:25 2020 (+0530)
# Last-Updated: Wed Mar 11 03:45:07 2020 (+0530)
#           By: Amritendu Mondal
#     Update #: 15
# 

import json
from numbers import Number
import logging
import tornado.web
import json
from covid.api import CovId19Data
from decimal import *
from covid import Covid


class HistoryHandler(tornado.web.RequestHandler):

    api = CovId19Data(force=False)

    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', "GET, OPTIONS")
        self.set_header("Access-Control-Allow-Headers", "access-control-allow-origin,authorization,content-type") 

    def get(self):
        country = self.get_argument('country', 'india');
        logging.info("recieved request for get stat, country-{}".format(country))
        data = self.api.get_history_by_country(country)
        self.set_default_headers()
        self.write(json.dumps(data))
         
    def options(self):
        # no body
        self.set_status(204)
        self.finish()


class CountryListHandler(tornado.web.RequestHandler):

    api = CovId19Data(force=False)

    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', "GET, OPTIONS")
        self.set_header("Access-Control-Allow-Headers", "access-control-allow-origin,authorization,content-type") 

    def get(self):
        data = self.api.show_available_countries()
        self.set_default_headers()
        self.write(json.dumps(data))
        
    def options(self):
        # no body
        self.set_status(204)
        self.finish()



class CountryStatHandler(tornado.web.RequestHandler):

    api = Covid(source="worldometers")

    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', "GET, OPTIONS")
        self.set_header("Access-Control-Allow-Headers", "access-control-allow-origin,authorization,content-type") 

    def get(self):
        country = self.get_argument('country', 'india');
        logging.info("recieved request for get stat, country-{}".format(country))
        data = self.api.get_status_by_country_name(country)
        for key in data:
            if isinstance(data[key], Number):
                data[key] = str(eval(str(data[key])))
        self.set_default_headers()
        self.write(json.dumps(data))
        
    def options(self):
        # no body
        self.set_status(204)
        self.finish()
