from flask import Flask
app=Flask(__name__)

@app.route("/")
def hello():
	return "Hello World"
#app.run() #5000


import tornado.ioloop
import tornado.web
class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('Hello,World')
def make_app():
	return tornado.web.Application([
		(r"/",MainHandler),])
if __name__=='__main__':
	app2=make_app()
	app2.listen(8888)
	tornado.ioloop.IOLoop.current().start()