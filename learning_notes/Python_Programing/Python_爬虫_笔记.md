## 导入需要的包
```
from bs4 import BeautifulSoup
import requests
```

## 伪造UA字符串

```
pip install fake-useragent

from fake_useragent import UserAgent
ua=UserAgent()
print(ua.random)
```

## 访问

```
需要拼接url的时候
>>> r = requests.get('http://httpbin.org/get', params=payload)
>>> print(r.url)
http://httpbin.org/get?key1=value1&key2=value2&key2=value3
```

## 解析HTML

```
 lxml is having trouble parsing invalid HTML.
Use html.parser instead of lxml.

soup = BeautifulSoup(html, 'html.parser')
```

## 获取去除前后空格的标签文本

```
get_text(strip=True)
```
