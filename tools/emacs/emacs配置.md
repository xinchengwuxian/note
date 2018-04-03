
```
;; Added by Package.el.  This must come before configurations of
;; installed packages.  Don't delete this line.  If you don't want it,
;; just comment it out by adding a semicolon to the start of the line.
;; You may delete these explanatory comments.


(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(package-selected-packages (quote (w3m flycheck material-theme elpy better-defaults)))
 '(send-mail-function (quote smtpmail-send-it))
 '(show-paren-mode t))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )

;;设置HOME和PATH
(setenv "HOME" "D:/emacs-25.1-x86_64-w64-mingw32")
(setenv "PATH" "D:/emacs-25.1-x86_64-w64-mingw32")
(setq default-directory "~/")

;;国内包仓库镜像
(setq package-archives '(("gnu"   . "http://elpa.emacs-china.org/gnu/")
                         ("melpa" . "http://elpa.emacs-china.org/melpa/")))						
(package-initialize)

(global-linum-mode t)
;;修改中文字体
(defun my--set-font (&optional frame)
  (with-selected-frame (or frame (selected-frame))
    (if (string-equal system-type "windows-nt")
    (progn
      (set-face-attribute
       'default nil :font "consolas 14")
      (dolist (charset '(han cjk-misc chinese-gbk))
        (set-fontset-font "fontset-default"
                  charset (font-spec :family "微软雅黑" :size 14)))
      (set-fontset-font "fontset-default"
                'unicode "Segoe UI Symbol" nil 'append)
      (set-fontset-font "fontset-default"
                '(#x1F600 . #x1F64F) "Segoe UI Symbol") ; Emoji
      (set-fontset-font "fontset-default"
                '(#xE000 . #xF8FF) "STIX") ; Private Use Areas
      )
      (progn
    (set-face-attribute
     'default nil :font "consolas 14")
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

(require 'package)

(load-theme 'material t)
(elpy-enable)

(when (require 'flycheck nil t)
  (setq elpy-modules (delq 'elpy-module-flymake elpy-modules))
  (add-hook 'elpy-mode-hook 'flycheck-mode))

```
