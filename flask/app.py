from flask import Flask,request
from resp import *
import mysql_conf  as sqlconf
from mySQL import MysqlDB
from enums import *
import datetime
import logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/hello/<string:name>/<int:age>/<float:weight>',methods=['GET','POST'])
def hello_world(name,age,weight):
    data = {
        "name":name,
        "age":age,
        "weight":weight,
    }
    return Response(SUCCESS,data)

@app.route('/jsondata')
def get_jsondata():
    data = request.get_json()
    return Response(SUCCESS,data)

@app.route('/growup/<string:method>/<int:userId>/<int:flag>')
def update_user_growup(method,userId,flag):
    logging.info(f"method:{method},userId:{userId},flag:{flag}")
    try:
        session = MysqlDB(sqlconf.host,sqlconf.user,sqlconf.password,sqlconf.database)
        session.start_transaction()
        
        select_sql = 'select email,growup from users where id = %s'
        res = session.select(select_sql,userId)
        print(f"select result:{res}")
        if res == False:
           return Response(USER_NOT_EXIST)

        if flag not in FlagsValueMap:
            return Response(WRONG_PARAMS)
        
        if method == 'add':  
            growup_value = res[1] + FlagsValueMap[flag]
        elif method == 'sub' and res[1] >= FlagsValueMap[flag]:
            growup_value = res[1] - FlagsValueMap[flag]
        else:
            return Response(WRONG_PARAMS)

        update_sql = 'update users set growup = %d where email = %s'
        update_values = (growup_value,res[0])
        update_ok = session.update(update_sql,update_values)
        print(f"update result:{update_ok}")
        if update_ok == False:
            return Response(SQL_ERROR)
        
        insert_sql = 'inset into growup_details (user,flag,value,method,created_at) values(%s,%d,%d,%s,%s)'
        nowtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        insert_values = (res[0],flag,FlagsValueMap[flag],method,nowtime)
        insert_ok = session.insert(insert_sql,insert_values)
        print(f"insert result:{insert_ok}")
        if insert_ok == False:
            return Response(SQL_ERROR)

        session.commit()
        return Response(SUCCESS,insert_ok)
    except Exception as e:
        print(f"update_user_growup error:{e}")
        return Response(SQL_ERROR,e)
    finally:
        session.close()

if __name__ == '__main__':
    app.run(port=8010)
