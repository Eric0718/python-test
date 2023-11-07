from flask import jsonify
SUCCESS = 0
UNKONWN_ERROR = 1
USER_NOT_EXIST = 2
SQL_ERROR = 3
WRONG_PARAMS = 4

msg_dict = {}
msg_dict[SUCCESS] = "Success"
msg_dict[UNKONWN_ERROR] = "Unknown error!"
msg_dict[USER_NOT_EXIST] = "User not exist!"
msg_dict[SQL_ERROR] = "sql error!"
msg_dict[WRONG_PARAMS] = "Wrong params!"

def getMsg(code):
    return msg_dict[code]

def Response(code,data=None):
    msg = getMsg(code)
    if msg == '':
        msg = msg_dict[UNKONWN_ERROR]
    data = {
        "code":code,
        "msg":msg,
        "data":data,
    }
    return jsonify(data)

