from base.mysql_cli import *
from base.redis_cli import *


def admin_login(request):
    employee = request.json["employee"]
    db.query("""select id,chainId,compId from sys_comp where (username=%s or mobile=%s) and status>-1 limit 1""",
             (employee.username, employee.username))
    d = db.store_result()
    print
    d
    r.set('111', '111')
    print
    r.get('111')
    db.connection.commit()
    return request.Response(json={"employee": employee})
