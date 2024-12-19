# WIP

<https://www.zhihu.com/question/45773200/answer/3422102765>

## Python项目结构样例

<https://pythonguidecn.readthedocs.io/zh/latest/writing/structure.html#id5>

```text
README.md
LICENSE
Makefile
setup.py
requirements.txt    # pip requirements file工程的所有依赖包: 测试, 编译和文档生成
sample/__init__.py
sample/core.py
sample/helpers.py
docs/conf.py
docs/index.rst
tests/test_basic.py
tests/test_advanced.py
```

- <https://github.com/navdeep-G/samplemod/tree/master>
- <https://github.com/universuen/python_template>

```make
init:
    pip install -r requirements.txt

test:
    py.test tests

PHONY: init test
```

## import兄弟目录

- 小型项目或临时场景：可以使用 sys.path.append。
- 开发环境：推荐使用 PYTHONPATH 或相对导入。
- 生产代码或分发项目：建议使用包安装方式。
