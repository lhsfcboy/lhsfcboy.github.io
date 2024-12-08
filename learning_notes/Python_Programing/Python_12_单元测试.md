# Python 测试

## Python 单元测试

### 什么是单元测试？

单元测试（又称为模块测试，Unit Testing）是针对程序模块（软件设计的最小单位）来进行正确性检验的测试工作。
单元是应用的最小可测试部件：

- 在过程化编程中，一个单元是单个程序、函数、过程等；
- 对于面向对象编程，最小单元是方法，包括基类（超类）、抽象类或派生类（子类）中的方法。

### 为什么要进行单元测试？

单元测试的主要目的包括：

- 确保代码质量：发现并修复问题，减少 bug 的数量。
- 改善代码设计：难以测试的代码通常是设计不够优雅的代码。
- 为重构提供保障：通过单元测试可以验证重构后的代码是否引入了问题。

引用：“编写单元测试的难易程度能够直接反映代码的设计水平。”

### Python 测试相关库

- unittest：内置库，模仿 PyUnit，简洁但较为繁琐。
- nose：测试发现与运行。
- pytest：广泛使用的第三方库，功能强大且简洁。
- mock：用于替换网络调用或 RPC 请求。

### 使用 `pytest` 进行单元测试

与 `unittest` 相比，`pytest` 更加简洁：

- 使用 `assert` 语句即可进行断言；
- 支持与 `unittest` 兼容。

示例代码：

```python
def add(a, b):
    """返回 a + b
    Args:
        a (int): 第一个整数
        b (int): 第二个整数
    Returns:
        int: a + b 的结果
    Raises:
        AssertionError: 如果 a 或 b 不是整数
    """
    assert all([isinstance(a, int), isinstance(b, int)])
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert isinstance(add(1, 2), int)
    with pytest.raises(Exception):  # 测试抛出异常
        add('1', 2)
```

常用命令：

- 运行某个模块中的测试：
  ```bash
  py.test test_mod.py
  ```
- 运行指定路径下的所有测试：
  ```bash
  py.test somepath
  ```
- 运行指定的测试函数或方法：
  ```bash
  py.test test_mod.py::test_func
  py.test test_mod.py::TestClass::test_method
  ```

### 测试驱动开发（TDD）的流程

采用 TDD（Test-Driven Development）的基本法则：

1. 编写失败的单元测试之前，不编写任何产品代码；
2. 仅当有一个单元测试失败时，编写新的测试代码；
3. 仅编写能够通过当前单元测试的产品代码。

优点：

- 提高确定性；
- 减少缺陷；
- 增加重构的信心；
- 单元测试可作为文档；
- 改善设计。

### 数据库与网络请求的处理

#### 数据库请求的处理

1. 使用 `fixture` 类装饰器，在 `TestCase` 运行前插入数据：

    ```python
    @fixture('table.sql')
    class SomeTestCase:
        pass
    ```

2. 在 `TestCase` 的 `setUp` 方法中插入数据，并在 `tearDown` 方法中销毁：

    ```python
    class SomeTestCase:
        def setUp(self):
            # 插入数据
            pass

        def tearDown(self):
            # 销毁数据
            pass
    ```

#### 网络请求的处理

1. 使用 `stub` 处理通用请求：

    ```python
    @registry.stub
    class ZoneSeqStub(BaseStub):
        @stub('Seq.get_id')
        def get_id(self, **kwargs):
            return random.randint(1, 100)
    ```

2. 使用 `mock` 模拟网络请求：

    ```python
    @mock.patch('somemodule.request')
    def test_function(self, mock_request):
        mock_request.return_value = {}  # 模拟返回值
    ```
