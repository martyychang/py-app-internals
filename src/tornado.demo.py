import tornado.ioloop
import tornado.web

from app.internals import logger


_logger = logger(__name__)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Tornado {} says, "Hello!"'.format(tornado.version))


if __name__ == '__main__':
    application = tornado.web.Application([
        (r'/', MainHandler),
    ])
    application.listen(8888)
    _logger.info('The Tornado party is about to start...')
    tornado.ioloop.IOLoop.current().start()
    _logger.info('The Tornado party has started!')
