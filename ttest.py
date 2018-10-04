import tornado.ioloop
import tornado.web
import tornado.options
from tornado.web import Application, url


class AjaxHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('ajax.html')

    def post(self):
        word = self.get_argument('w')
        print('SUBMITTED: ', word)
        msg = '<p>Output: ' + word + '<p>'
        print('RETURNED: ', msg)
        self.write(msg)


if __name__ == "__main__":
    app = Application([
        url(r"/", AjaxHandler)],
        debug=True)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
