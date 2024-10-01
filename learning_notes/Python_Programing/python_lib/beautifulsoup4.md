# Beautiful Soup

- [官方文档](http://beautifulsoup.readthedocs.io/zh_CN/latest/)

## 安装

```bash
pip install beautifulsoup4
pip install lxml
pip install html5lib
```

解析器

| 解析器           | 使用方法                               | 优势 | 劣势 |
| ---------------- | -------------------------------------- | ---- | ---- |
| Python标准库     | BeautifulSoup(markup, “html.parser”) |      |      |
| lxml HTML 解析器 | BeautifulSoup(markup, “lxml”)`       |      |      |
| lxml XML 解析器  | BeautifulSoup(markup, “xml”)`        |      |      |
| html5lib         | BeautifulSoup(markup, “html5lib”)    |      |      |


## Hello bs4

```python
from bs4 import BeautifulSoup
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html, "html5lib")
# soup = BeautifulSoup(open('index.html'))
print(soup.prettify())
```

## 四大对象种类

- Tag
- NavigableString
- BeautifulSoup
- Comment

### Tag

soup加标签名获取第一个符合要求的标签

```python
soup.title
soup.head
soup.a
```

Tag，它有两个重要的属性，是 name 和 attrs

`soup.p.attrs`我们把 p 标签的所有属性打印输出了出来，得到的类型是一个字典

`soup.p.get('class')`利用get方法，传入属性的名称

`soup.p.string` 获取标签内部的文字
