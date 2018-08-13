# HTML转markdown

想写个HTML转markdown的小脚本

## 用法

给定URL,

专栏文章的链接: <http://zhuanlan.zhihu.com/p/28277072>, 或问题答案的链接: <https://www.zhihu.com/question/281185007/answer/420128463>

## 目标文件的组织

```text
中心极限定理的直观理解/
├── data
│   └── 2000.csv
├── images
│   ├── 1.png
│   └── 2.jpg
└── readme.md
```

## 工具

```python
from bs4 import BeautifulSoup
import requests
```

## 参照
