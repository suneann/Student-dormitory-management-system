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

Windows环境搭建：

1. 下载python3最新的安装包进行安装（点下一步的时候注意，除了debug相关的都勾上，千万要把pip的勾上，还有加入PATH路径的选项也勾上）
2.   打开管理员权限的命令行，pip install django

Linux环境搭建：

1. 一般发行版都有自带python，但是较老的发行版自带的是python2，所以需要安装python3，各个发行版的包管理工具（比如yum、dnf、apt-get、emerge、pacman等）都不同，根据情况决定，实在不行了到官方下源码包编译。
2.  sudo pip install django 

注意：

由于pip命令需要到国外网站下载包，可能会失败，所以要么翻墙之后执行，要么失败之后再多执行几次。

以下所有命令都需要在命令行中切换到Student_Dormitory目录执行。

cd Student_Dormitory

开启测试服务器：

切换到Student_Dormitory目录下，执行命令python manage.py runserver，然后不要关闭命令窗口。

![标题: fig:](https://s2.loli.net/2022/03/02/ltWfe6nCsOzF3D2.png)

进入管理界面：

在浏览器中输入http://localhost/admin/，进入管理员登录界面。

![img](https://s2.loli.net/2022/03/02/CY3cSh1x7KwbMAz.png)

 

用户名为admin，密码是123456。

可以执行python manage.py changepassword root来修改密码，也可以执行python manage.py createsuperuser来新增一个管理员帐号。

登录后管理员页面如下：

![img](https://s2.loli.net/2022/03/02/wbGZIe5svqfa9WC.png)

在浏览器中输入http://localhost/login.html，进入业务系统界面。输入刚才查看的用户名和密码登录，系统会自动识别用户身份对应到学生，宿舍管理员。之后便可进行操作。

退出系统：

在命令行中按Ctrl+C即可退出。