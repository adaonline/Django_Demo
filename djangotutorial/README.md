- `manage.py`: 一个让你用各种方式管理 Django 项目的命令行工具。你可以阅读 [django-admin 和 manage.py](https://docs.djangoproject.com/zh-hans/5.1/ref/django-admin/) 获取所有 `manage.py` 的细节。
- `mysite/`: 一个目录，它是你项目的实际 Python 包。它的名称是你需要用来导入其中任何内容的 Python 包名称（例如 `mysite.urls`）。
- `mysite/__init__.py`：一个空文件，告诉 Python 这个目录应该被认为是一个 Python 包。如果你是 Python 初学者，阅读官方文档中的 [更多关于包的知识](https://docs.python.org/3/tutorial/modules.html#tut-packages)。
- `mysite/settings.py`：Django 项目的配置文件。如果你想知道这个文件是如何工作的，请查看 [Django 配置](https://docs.djangoproject.com/zh-hans/5.1/topics/settings/) 了解细节。
- `mysite/urls.py`：Django 项目的 URL 声明，就像你网站的“目录”。阅读 [URL调度器](https://docs.djangoproject.com/zh-hans/5.1/topics/http/urls/) 文档来获取更多关于 URL 的内容。
- `mysite/asgi.py`：作为你的项目的运行在 ASGI 兼容的 Web 服务器上的入口。阅读 [如何使用 ASGI 来部署](https://docs.djangoproject.com/zh-hans/5.1/howto/deployment/asgi/) 了解更多细节。
- `mysite/wsgi.py`：作为你的项目的运行在 WSGI 兼容的Web服务器上的入口。阅读 [如何使用 WSGI 进行部署](https://docs.djangoproject.com/zh-hans/5.1/howto/deployment/wsgi/) 了解更多细节。

mysite是一个项目

```
django-admin startproject mysite djangotutorial
```

polls是一个应用

```
py manage.py startapp polls
```

## 项目 VS 应用

项目和应用有什么区别？应用是一个专门做某件事的网络应用程序——比如博客系统，或者公共记录的数据库，或者小型的投票程序。项目则是一个网站使用的配置和应用的集合。项目可以包含很多个应用。应用可以被很多个项目使用。





## 数据迁移

首先定义好polls 的models.py文件



### 存储迁移

```
py manage.py makemigrations polls
Migrations for 'polls':
  polls/migrations/0001_initial.py
    + Create model Question
    + Create model Choice
通过运行 makemigrations 命令，Django 会检测你对模型文件的修改（在这种情况下，你已经取得了新的），并且把修改的部分储存为一次 迁移。
```

模型的迁移数据，它被储存在 `polls/migrations/0001_initial.py` 里



### 检查迁移

```
py manage.py sqlmigrate polls 0001
```

这个 [`sqlmigrate`](https://docs.djangoproject.com/zh-hans/5.1/ref/django-admin/#django-admin-sqlmigrate) 命令并没有真正在你的数据库中的执行迁移 - 相反，它只是把命令输出到屏幕上，让你看看 Django 认为需要执行哪些 SQL 语句。



### 执行迁移

运行 [`migrate`](https://docs.djangoproject.com/zh-hans/5.1/ref/django-admin/#django-admin-migrate) 命令，在数据库里创建新定义的模型的数据表：

```
py manage.py migrate
```



### 总结

只需要记住，改变模型需要这三步：

- 编辑 `models.py` 文件，改变模型。
- 运行 [`python manage.py makemigrations`](https://docs.djangoproject.com/zh-hans/5.1/ref/django-admin/#django-admin-makemigrations) 为模型的改变生成迁移文件。
- 运行 [`python manage.py migrate`](https://docs.djangoproject.com/zh-hans/5.1/ref/django-admin/#django-admin-migrate) 来应用数据库迁移。

