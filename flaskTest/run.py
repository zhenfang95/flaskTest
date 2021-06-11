from datetime import datetime
from app import app
from app.utils.logger import Log
from app.controller.auth.user import auth

#注册蓝图
app.register_blueprint(auth)

@app.route('/')
def hello_world():
    log = Log('Hello World')
    log.info('哈哈哈哈啊哈哈')
    now = datetime.now().strftime("%Y-%M-%d %H:%M:%S")
    print(now)
    return now


if __name__ == '__main__':
    #启动web服务
    app.run("0.0.0.0",threaded=True,port=5000)
