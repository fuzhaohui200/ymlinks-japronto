# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib


def wechat_server_audit(request):
    signature = request.query["signature"]
    timestamp = request.query["timestamp"]
    nonce = request.query["nonce"]
    echostr = request.query["echostr"]
    token = "YM1708231200wh@"  # 请按照公众平台官网\基本配置中信息填写

    params = [token, timestamp, nonce]
    params.sort()
    sha1 = hashlib.sha1()
    map(sha1.update, params)
    hashcode = sha1.hexdigest()
    if hashcode == signature:
        return request.Response(echostr)
    else:
        return request.Response("")
