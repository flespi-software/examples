from aiohttp import web

# incoming HTTP POST request handler
async def handler(request):
    # read all data in request as bytes (not str)
    json_bytes = await request.content.read()

    # now json_bytes will be something like this:
    # b'[{"channel.id":94,"ident":"1234","peer":"127.0.0.1:58606","protocol.id":19,
    # "server.timestamp":1554319739.34234,"timestamp":1554319739.34234}]'

    # more details about available message content:
    # https://flespi.com/kb/messages-basic-information-units

    # you may use json_bytes to parse json, using json.loads(json_bytes)

    # but in this example we are just storing it in a file
    # please note that it will be overwritten on each new request
    with open("messages.json", "wb") as f:
        f.write(json_bytes)

    # NOTE: it's important to send HTTP 200 OK status
    # to acknowledge successful messages delivering
    return web.Response(status=200)


if __name__ == "__main__":
    app = web.Application()

    # setup corrent path for your handler ("/" string)
    app.add_routes([web.post("/", handler)])

    # setup correct host and port to listen for your HTTP server
    web.run_app(app, host="localhost", port=7777)
