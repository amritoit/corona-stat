import tornado.ioloop
import tornado.web
import random
from tornado.options import define, options
import logging
import os
from handlers.main_handler import MainHandler

port = int(os.environ.get("PORT", 5000))
define('port', default=9999, help='run on the given port', type=int)

logging.basicConfig(
    filename="corona-serv.log",
    level=logging.DEBUG
)
logging.getLogger().addHandler(logging.StreamHandler())
formatter = logging.Formatter(
    '[%(levelname)1.1s %(asctime)s.%(msecs)d '
    '%(module)s:%(lineno)d] %(message)s',
    "%Y-%m-%d %H:%M:%S"
)  # creating own format

for handler in logging.getLogger().handlers:  # setting format for all handlers
    handler.setFormatter(formatter)

def main():
    tornado.options.parse_command_line()
    handlers = [
        (r"/api/v1/data", MainHandler)
    ]
    settings = dict(
        autoescape=None,  # tornado 2.1 backward compatibility
        gzip=True,
        xsrf_cookies=False,  # No xsrf cookie used on Android.
    )
    application = tornado.web.Application(handlers, **settings)
    http_server = tornado.httpserver.HTTPServer(application)
    port = int(os.environ.get("PORT", options.port))
    http_server.bind(port)
    http_server.start(1)
    logging.info(random.choice([
        'I won\'t be a rock star. I will be a legend.',
        'I like to be surrounded by splendid things.',
        'I always knew I was a star. And now, the rest of the world seems to agree with me.',
        'The reason we\'re successful, darling? My overall charisma, of course.',
        'My soul has painted like the wings of butterflies, Fairy tales of yesterday will grow but never die, I can fly, my friends...',
        'I was born to love you with every single beat of my heart. I was born to take care of you every single day of my life.'
    ]))
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
