# tools_py
pyhton的一些简单的工具库 大部分是用来处理时间的


如果要发布自己的包，需要先到 pypi 上注册账号。然后创建 ~/.pypirc 文件，
此文件中配置 PyPI 访问地址和账号。如的.pypirc文件内容请根据自己的账号来修改。
```ini
[distutils]
index-servers = pypi

[pypi]
username = xxx
password = xxx
```
#### 发布源码包:
``` python
python setup.py register
python setup.py sdist upload
```   