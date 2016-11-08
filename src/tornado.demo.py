import tornado.ioloop
import tornado.web
import tornado.gen as gen

from app.internals import logger


_logger = logger(__name__)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        _logger.info('MainHandler.get')
        self.write('Tornado {} says, "Hello!"'.format(tornado.version))


class ApiHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        _logger.info('ApiHandler.get')
        result = yield do_api_get()
        self.write(result)


@gen.coroutine
def do_api_get():
    _logger.info('somewhere inside a coroutine...')
    raise gen.Return('gotten')


if __name__ == '__main__':
    application = tornado.web.Application([
        (r'/', MainHandler),
        (r'/api', ApiHandler),
    ])
    application.listen(8888)

    _logger.info('The Tornado party is about to start...')
    tornado.ioloop.IOLoop.current().start()
