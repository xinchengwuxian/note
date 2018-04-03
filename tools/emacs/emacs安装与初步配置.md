### 安装步骤：
1. 下载[emacs](http://ftp.gnu.org/gnu/emacs/windows/)安装包
2. 将下载的文件放到一个具体的目录下解压
3. 解压文件后进入软件根目录/bin下面执行addpm.exe（安装emacs并且添加到开始菜单）
4. 修改C:\Users\<username>\AppData\Roaming\.emacs（需要自己手动创建，windows不能创建 . 文件，可以打开emacs后修改配置后点击save options后会自动生成）配置文件，修改内容为 (load-file "D:/emacs-23.2/.emacs") ，这步主要是将配置文件映射到安装包路径。
5. 在.emacs中添加如下配置（添加环境变量，路径为安装包解压路径）
```
(setenv "HOME" "D:/emacs-23.2")
(setenv "PATH" "D:/emacs-23.2")
;;set the default file path
(setq default-directory "~/")
```
6. 修改emacs的包的源，让他使用国内镜像：
```
(setq package-archives '(("gnu"   . "http://elpa.emacs-china.org/gnu/")
                         ("melpa" . "http://elpa.emacs-china.org/melpa/")))
```
7. 在windows下面打开中文文档会很卡，这是由于在MS Windows下Emacs错误的使用BatangChe这个韩文字体来显示中文，而这个韩文字体包含的中文肯定不全，于是会不停的fallback，就很卡。添加如下配置：
```
;; -*- lexical-binding: t; -*-
;; Font settings.
;; Setting English Font
(add-to-list 'default-frame-alist '(height . 35))
(add-to-list 'default-frame-alist '(width . 100))
;; (add-to-list 'default-frame-alist
;;              (if (string-equal system-type "windows-nt")
;; 		 '(font . "Inconsolata-18")
;; 	       '(font . "Inconsolata-14")))
;; 微软雅黑
;; 冬青黑体简体中文 W3
;; Hiragino Sans GB W3
;; 思源黑体 CN Regular
;; Source Han Sans
(defun my--set-font (&optional frame)
  (with-selected-frame (or frame (selected-frame))
    (if (string-equal system-type "windows-nt")
    (progn
      (set-face-attribute
       'default nil :font "Inconsolata 18")
      ;; (set-fontset-font t
      ;; 		      'unicode (font-spec :family "Inconsolata" :size 18))
      ;; Chinese Font
      ;; cjk-misc gb18030 chinese-gbk chinese-gb2312
      (dolist (charset '(han cjk-misc chinese-gbk))
        (set-fontset-font "fontset-default"
                  charset (font-spec :family "冬青黑体简体中文 W3")))
      (set-fontset-font "fontset-default"
                'unicode "Segoe UI Symbol" nil 'append)
      (set-fontset-font "fontset-default"
                '(#x1F600 . #x1F64F) "Segoe UI Symbol") ; Emoji
      (set-fontset-font "fontset-default"
                '(#xE000 . #xF8FF) "STIX") ; Private Use Areas
      )
      (progn
    (set-face-attribute
     'default nil :font "Inconsolata 14")
    ;; (set-fontset-font t
    ;; 		    'unicode (font-spec :name "Inconsolata" :size 28))
    (dolist (charset '(kana han cjk-misc bopomofo))
      (set-fontset-font "fontset-default"
                charset (font-spec :name "Hiragino Sans GB")))))
    (set-fontset-font "fontset-default" ?– "Symbola")
    (set-fontset-font "fontset-default" ?′ "Symbola")
    (set-fontset-font "fontset-default" ?″ "Symbola"))
  )
(my--set-font)
(add-hook 'after-make-frame-functions 'my--set-font)
(defface strike-through
  '((t :strike-through t))
  "Basic strike through face."
  :group 'basic-faces)
```

### 参考文章：
- http://blog.csdn.net/jackieban/article/details/
- https://chriszheng.science/2015/04/26/Emacs-font-settings/
