# 学生寝室管理系统 (django+sqlite)

记录一下第一次接触django写的一个管理系统。

### 功能描述

​	针对中小型学生公寓的运营模式，有三类核心成员：学生、公寓管理员和系统管理员，分别有五个核心模块需要实现， 系统管理模块，学生信息管理模块，寝室管理模块，财产管理模块以及出入管理模块。

![image-20220302231758355](https://s2.loli.net/2022/03/02/OpAIiukPhFdCTyr.png)

基本功能如下：

![image-20220302231902116](https://s2.loli.net/2022/03/02/5oZuQBpCz624VGU.png)

### 运行环境

开发环境：python3.7.4、pychar2019.3.3、django3

数据库：Microsoft SQL Server、sqlite

python依赖库：

详见文档filename.txt

### 配置说明


1、开启测试服务器：

切换到Student_Dormitory目录下，执行命令python manage.py runserver，然后不要关闭命令窗口。

![标题: fig:](https://s2.loli.net/2022/03/02/ltWfe6nCsOzF3D2.png)

2、进入管理界面：

在浏览器中输入http://localhost/admin/ ，进入管理员登录界面。

![img](https://s2.loli.net/2022/03/02/CY3cSh1x7KwbMAz.png)

 

用户名为admin，密码是123456。

可以执行python manage.py changepassword root来修改密码，也可以执行python manage.py createsuperuser来新增一个管理员帐号。

登录后管理员页面如下：

![img](https://s2.loli.net/2022/03/02/wbGZIe5svqfa9WC.png)

在浏览器中输入http://localhost/login.html ，进入业务系统界面。输入刚才查看的用户名和密码登录，系统会自动识别用户身份对应到学生，宿舍管理员。之后便可进行操作。

3、退出系统：

在命令行中按Ctrl+C即可退出。
