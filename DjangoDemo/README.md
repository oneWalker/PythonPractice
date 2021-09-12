# Django Demo

## 目录结构

django 以多个应用(app)耦合的形式来组合成一个大的web项目(project)，多个app之间可以相互调用

```shell
|-- project/
    |-- settings.py        # 项目配置
    |-- urls.py            # 项目路由定义
    |-- wsgi.py        # nginx/apache

|-- app/
    |-- templates/
        |-- app/
            |-- base.html    # 模板
            ...
    |-- admin.py        # 配置模型models在django原生后台的管理
    |-- apps.py        # 应用级别的配置
    |-- forms.py        # 表单处理逻辑
    |-- managers.py    # 模型处理逻辑
    |-- models.py        # 模型定义
    |-- urls.py            # 路由设置
    |-- views.py        # 控制层
    |-- tests.py
    ...        
|-- other-app/
    ...                     # 另一个应用
|-- static/
    |-- app/
    |-- other-app/
    |-- admin/ 
```

- 本项目的基本文件说明
  - manage.py 项目管理功能
  - _init_.py 初始化文件
  - settings.py Django的配置文件
  - urls.py Django项目的url声明

## 运行相关程序

- 运行整个程序文件

```shell
python3 manage.py runserver 0.0.0.0:8000
```

- 将models进行统一放置在主目录下面
问题:Django通常一个app只有一个model.py，有时候一个应用会存在多个model
解决方法：
1.在app目录下定义文件夹models
2.在文件夹中定义相应的model文件
3.将models目录下的_init_.py导入相关的model文件如

```python
from appname.models import users
```

- 模型迁移
  - 将定义模型迁移到数据库（正向生成）

  ```shell
  # 记录我们对models.py的所有改动，并且将这个改动迁移到migrations这个文件下生成一个文件
  python manage.py makemigrations #全局
  python manage.py makemigrations appname #局部app
  # 把这些改动作用到数据库也就是执行migrations里面新改动的迁移文件更新数据库
  python manage.py migrate #全局
  python manage.py migrate appname #局部app
  ```

  - 将数据库的表反向生成模型（反向生成Orm）

  ```shell
  python manage.py inspectdb
  #将代码导入到项目中
  python manage.py inspectdb > hello/models.py
  #根据表名生成
  ```

- To Do List
  -[ ] 基本请求和数据解析
  -[ ] 连接数据库
