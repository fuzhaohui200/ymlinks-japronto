from japronto import Application, RouteNotFoundException

from base.qiniu_cli import *
from helloword.ymlinks_basic import *
from helloword.ymlinks_body import *
from helloword.ymlinks_exception import *
from helloword.ymlinks_html import *
from helloword.ymlinks_req_extend import *
from helloword.ymlinks_todo import *
from wechat.wechat_gate import *

app = Application()
r = app.router
r.add_route('/', hello)
r.add_route('/sync', synchronous)
r.add_route('/async', asynchronous)
r.add_route('/love', get_love, 'GET')
r.add_route('/methods', methods, methods=['POST', 'DELETE'])
r.add_route('/params/{p1}/{p2}', params)
r.add_route('/basic', basic)
r.add_route('/body', body)
r.add_route('/misc', misc)
r.add_route('/text', text)
r.add_route('/encoding', encoding)
r.add_route('/mime', mime)
r.add_route('/qrcode/{p1}', generate_qrcode, method='GET')
r.add_route('/body', body)
r.add_route('/json', json)
r.add_route('/code', code)
r.add_route('/headers', headers)
r.add_route('/cookies', cookies)
r.add_route('/cat', cat)
r.add_route('/dog', dog)
r.add_route('/unhandled', unhandled)
r.add_route('/extended', extended_hello)
r.add_route('/index', index)
r.add_route('/callback', with_callback)
r.add_route('/example', example)

r.add_route('/image/token', get_token)
r.add_route('/cgi-bin/wechat', wechat_server_audit, method='GET')

r.add_route('/todos', list_todos, method='GET')
r.add_route('/todos/{id}', show_todo, method='GET')
r.add_route('/todos/{id}', delete_todo, method='DELETE')
r.add_route('/todos', add_todo, method='POST')

# register all the error handlers so they are actually effective
app.add_error_handler(KittyError, handle_cat)
app.add_error_handler(DoggieError, handle_dog)
app.add_error_handler(RouteNotFoundException, handle_not_found)

# Finally register out custom property and method
# By default the names are taken from function names
# unelss you provide `name` keyword parameter.
app.extend_request(reversed_agent, property=True)
app.extend_request(host_startswith)
app.extend_request(cursor, property=True)

app.run(debug=True)
