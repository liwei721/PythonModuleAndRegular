## poetry 依赖包管理工具
- 官方地址：https://python-poetry.org/docs/
- 推荐安装方式：
```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
``` 
### 常用命令：
- python get-poetry.py --uninstall 卸载poetry
- poetry self update 更新poetry
- poetry new projectName  创建一个工程（认识其目录结构及配置文件）
- poetry version 查看poetry版本
- poetry add moduleName  往项目中增加依赖包同时安装他们
- poetry search moduleName  从仓库中搜索对应的module
- poetry remove moduleName  从项目中移除依赖包
- poetry install 安装所有的依赖包
- poetry build 打包python程序
- poetry publish 将打包的程序发布到仓库中
- poetry run python  cmd  执行python的命令
- poetry shell 进入virtualenv，如果不存在，则创建一个

### 其他
- poetry check  可以对poetry的配置文件进行校验。
- lock  锁定依赖包，但是不更新。
其他更多命令，可以参考官方文档

## pyenv版本管理工具
- pyenv commands  列出所有的pyenv命令
- pyenv install -l 查看所有可用的python版本
- pyenv install x.x.x  安装对应版本的python
- pyenv uninstall x.x.x 卸载对应版本的python
- pyenv versions  查看所有可用的python版本
- pyenv global x.x.x  设置全局的python版本
- pyenv local x.x.x  设置某个目录的python版本
- pyenv shell x.x.x  设置shell窗口的python版本
- pyenv version 显示当前的python版本
- pyenv rehash  将可执行文件同步到shims目录中


