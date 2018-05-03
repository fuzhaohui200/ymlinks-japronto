from base.mysql_cli import *


def add_todo(request):
    shop = request.json["shop"]
    db.execute("""INSERT INTO sys_comp (id,chainId,`name`) VALUES (?,?,?)""", (shop.id, shop.chainId, shop.name))
    db.connection.commit()
    return request.Response(json={"shop": shop})


def list_todos(request):
    db.execute("""SELECT id, chainId, `name` FROM sys_comp""")
    todos = [{"id": id, "todo": todo} for id, todo in db]

    return request.Response(json={"results": todos})


def show_todo(request):
    cur = request.cursor
    id = int(request.match_dict['id'])
    cur.execute("""SELECT id, todo FROM todos WHERE id = ?""", (id,))
    todo = cur.fetchone()
    if not todo:
        return request.Response(code=404, json={"error": "not found"})
    todo = {"id": todo[0], "todo": todo[1]}

    return request.Response(json=todo)


def delete_todo(request):
    cur = request.cursor
    id = int(request.match_dict['id'])
    cur.execute("""DELETE FROM todos WHERE id = ?""", (id,))
    if not cur.rowcount:
        return request.Response(code=404, json={"error": "not found"})
    cur.connection.commit()

    return request.Response(json={})


def cursor(request):
    def done_cb(request):
        request.extra['conn'].close()

    if 'conn' not in request.extra:
        request.extra['conn'] = db_connect()
        request.add_done_callback(done_cb)

    return request.extra['conn'].cursor()
