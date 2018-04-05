把本目录下的 pre-commit.py 重命名为 pre-commit 移动至git项目所在目录的隐藏文件夹 .git/hooks/下。适当调整checkstyle.jar 和 checkstyle.xml文件的路径即可。

解决的问题：从客户端杜绝任何没有经过checkstyle检验的代码被提交到主线，防止新增代码引入checkstyle问题，提高团队效率。