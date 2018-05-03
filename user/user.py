from base.mongodb_cli import *
from base.redis_cli import *


def open_auth(request):
    user = request.json["user"]
    collection = client.get_default_database().get_collection('sys_user')
    user.createDate = datetime.datetime.utcnow()
    collection.save(user)
    r.set('111', '111')
    print
    r.get('111')
    return request.Response(json={"result": user})


def chain_users(request):
    chainId = request.query["chainId"]
    compId = request.query["compId"]
    collection = client.get_default_database().get_collection('sys_user', chainId, compId)
    users = collection.find()
    return request.Response(json={"result": users})
