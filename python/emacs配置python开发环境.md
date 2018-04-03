### 配置流程
1. 修改emacs获取包的源（emacs的配置文件当中，比如说.emacs或者自定义的配置文件），这样下载会快一点
```
(setq package-archives '(("gnu"   . "http://elpa.emacs-china.org/gnu/")
                         ("melpa" . "http://elpa.emacs-china.org/melpa/")))
```
2. 打开emacs，通过M-X package-list-packages查看可安装的包目录，可通过点击来安装需要的包
3. 修改配置让安装的包可以启动，在配置文件中需要添加一下代码可以让emacs能找到对应的包
```
(require 'package)
```
4. 比如说我要安装一个主题（metarial-theme）
    1. 执行M-X package-list-packages,找到对应的metarial-theme的包，然后点击install
    2. 修改.emacs文件，添加代码(load-theme 'material t)，然后重新启动（注意，记得添加require）
5. 安装python编辑环境的时候先安装flake8,jedi(代码语法检查和自动补齐的包)
    1. 可通过打开cmd，然后执行python -m pip install flake8来安装
    2. jedi类似
6. 通过M-x package-list-packages 找到elpy包进行安装，elpy（Emacs Lisp Python Environment）插件可以说为我们提供了Python开发环境所需要的几乎全部功能，包括：
    - 自动缩进
    - 语法高亮
    - 自动补全
    - 语法检查
    - REPL集成
    - 虚拟环境支持，以及
    - 更多其他功能
7. 在配置文件中添加(elpy enable),然后重新启动就行了


### 参考文章
- http://codingpy.com/article/emacs-the-best-python-editor/
