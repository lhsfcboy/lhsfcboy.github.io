# requests

## Hello, requests

```python
import requests

r = requests.get('https://baidu.com')
print(r.text)

# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
# r = requests.get('https://baidu.com', headers = headers)

```

## 通过requests来下载

```python
url = "http://craphound.com/images/1006884_2adf8fc7.jpg"
response = requests.get(url)
if response.status_code == 200:
    with open("/Users/apple/Desktop/sample.jpg", 'wb') as f:
        f.write(response.content)
```