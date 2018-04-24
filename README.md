# YCYY
优易数据协同项目

## Contributors

* [se7en](https://github.com/litt1eseven/Ycyy)
* [唐诚](https://github.com/woxingyiyi/Ycyy)

## deploy（后期加）
**Docker部署**

- `将整个项目克隆，进入ycyy`

- `特别注意：数据库要配置正确`

- `执行 ./build_docker.sh`

- `等待执行完成，运行 http://localhost 查看即可`

## doc(如果不用docker)
**下载对应的库：** 
- `pip install -r requirements.txt`

**进入到目录:**
- `export FLASK_APP=manage.py`
- `export FLASK_DEBUG=1`

**初始化数据库:**
- `flask db init`
- `flask db migrate -m "init database"`
- `flask db upgrade`

**创建管理员:**
```
from flask.models import db,User
user = User(email='shiyanlou@admin.com',username='admin',password='admin123')
db.session.add(user)
db.session.commit()
exit() # 退出
```

**运行项目:**
- `flask run`
>-p port
 -h host

**管理员登录**
- `username: ycyy@admin.com | password: ycyy123`

**使用管理员登录后访问控制台**
>访问后将展示用户列表信息

**演示**
暂时删掉
暂不公开
