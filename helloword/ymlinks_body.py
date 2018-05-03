import random
from http.cookies import SimpleCookie

import qrcode


# Providing just text argument yields a `text/plain` response  # encoded with `utf8` codec (charset set accordingly)
from six import BytesIO


def text(request):
    return request.Response(text='Hello world!')


# You can override encoding by providing `encoding` attribute.
def encoding(request):
    return request.Response(text='您好，世界', encoding='UTF-8')


# You can also set a custom MIME type.
def mime(request):
    return request.Response(
        mime_type="image/svg+xml",
        text="""
          <svg xmlns="http://www.w3.org/2000/svg" version="1.1">
              <line x1="10" y1="10" x2="80" y2="80" stroke="blue" />
          </svg>
          """)


# You can also set a custom MIME type.
def generate_qrcode(request):
    p1 = str(request.match_dict['p1'])
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(p1)
    qr.make(fit=True)

    img = qr.make_image()
    buf = BytesIO()  # 在内存中操作bytes，原因是图片是以二进制存储的
    img.save(buf)
    image_stream = buf.getvalue()  # 获取图片的二进制字节
    return request.Response(
        mime_type="image/png",
        body=image_stream)


# Or serve binary data. `Content-Type` set to `application/octet-stream`
# automatically but you can always provide your own `mime_type`.
def body(request):
    return request.Response(body=b'\xde\xad\xbe\xef')


# There exist a shortcut `json` argument. This automatically encodes the
# provided object as JSON and servers it with `Content-Type` set to
# `application/json; charset=utf8`
def json(request):
    return request.Response(json={'hello': 'world'})


# You can change the default 200 status `code` for another
def code(request):
    return request.Response(code=random.choice([200, 201, 400, 404, 500]))


# And of course you can provide custom `headers`.
def headers(request):
    return request.Response(
        text='headers',
        headers={'X-Header': 'Value',
                 'Refresh': '5; url=https://xkcd.com/353/'})


# Or `cookies` by using Python standard library `http.cookies.SimpleCookie`.
def cookies(request):
    cookies = SimpleCookie()
    cookies['hello'] = 'world'
    cookies['hello']['domain'] = 'localhost'
    cookies['hello']['path'] = '/'
    cookies['hello']['max-age'] = 3600
    cookies['city'] = 'São Paulo'

    return request.Response(text='cookies', cookies=cookies)
