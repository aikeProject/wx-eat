#### 吃什么

`微信小程序` + `flask`

```
Flask==0.12.2
python==3.7
```

##### 运行 `eat-flask` 

- 在`eat-flask`目录下，创建虚拟环境

```
 virtualenv venv
```

- 激活虚拟环境

```
venv/scripts/activate
```

- 安装 `requirements.txt`

```
pip install -r requirements.txt
```

- 同步数据库(mysql)

mysql配置

首先需要创建好叫`eatFlask`的数据库

配置 `config.py`

```
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:密码@localhost:3306/eatFlask'
```

- 首次使用 创建迁移仓库

```
 python manage.py db init
```

- 创建迁移脚本

```
python manage.py db migrate 
```

- 同步到数据库

```
python manage.py db upgrade    
```

- 启动项目

```
python manage.py runserver
```
