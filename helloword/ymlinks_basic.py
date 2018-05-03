import asyncio
from json import JSONDecodeError
from base.redis_cli import r


def synchronous(request):
    return request.Response(text='I am synchronous!')


async def asynchronous(request):
    for i in range(1, 4):
        await asyncio.sleep(1)
        print(i, 'seconds elapsed')

    return request.Response(text='3 seconds elapsed')


def hello(request):
    return request.Response(text='Hello world!')


def get_love(request):
    return request.Response(text='Got some love')


def methods(request):
    return request.Response(text=request.method)


def params(request):
    return request.Response(text=str(request.match_dict))


def basic(request):
    text = """Basic request properties:
        Method: {0.method}
        Path: {0.path}
        HTTP version: {0.version}
        Query string: {0.query_string}
        Query: {0.query}""".format(request)

    if request.headers:
        text += "\nHeaders:\n"
        for name, value in request.headers.items():
            text += "      {0}: {1}\n".format(name, value)

    return request.Response(text=text)


def body(request):
    text = """Body related properties:
        Mime type: {0.mime_type}
        Encoding: {0.encoding}
        Body: {0.body}
        Text: {0.text}
        Form parameters: {0.form}
        Files: {0.files}
      """.format(request)

    try:
        json = request.json
    except JSONDecodeError:
        pass
    else:
        text += "\nJSON:\n"
        text += str(json)

    return request.Response(text=text)


def misc(request):
    text = """Miscellaneous:
        Matched route: {0.route}
        Hostname: {0.hostname}
        Port: {0.port}
        Remote address: {0.remote_addr},
        HTTP Keep alive: {0.keep_alive}
        Match parameters: {0.match_dict}
      """.strip().format(request)

    if request.cookies:
        text += "\nCookies:\n"
        for name, value in request.cookies.items():
            text += "      {0}: {1}\n".format(name, value)

    return request.Response(text=text)
