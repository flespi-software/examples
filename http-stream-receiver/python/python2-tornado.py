from __future__ import print_function
import tornado.web
import tornado.ioloop


# incoming HTTP POST request handler
class MainHandler(tornado.web.RequestHandler):
    def post(self):
        # read all data in request as str
        json_str = self.request.body

        # now json_str will be something like this:
        # [{"channel.id":94,"ident":"1234","peer":"127.0.0.1:57632","protocol.id":19,
        # "server.timestamp":1554357439.356658,"timestamp":1554357439.356658}]

        # you may use json_str to parse json, using json.loads(json_str)

        # but in this example we are just storing it in a file
        # please note that it will be overwritten on each new request
        with open("messages.json", "wb") as f:
            f.write(json_str)

        # NOTE: it's important to send HTTP 200 OK status
        # to acknowledge successful messages delivering
        self.set_status(200)


if __name__ == "__main__":
    app = tornado.web.Application([
        # setup corrent path for your handler ("/" string)
        (r"/", MainHandler),
    ])

    # setup correct host and port to listen for your HTTP server
    app.listen(7777, address="localhost")
    tornado.ioloop.IOLoop.current().start()
