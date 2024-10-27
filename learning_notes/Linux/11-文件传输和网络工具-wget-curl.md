# `wget`和`curl`命令详解

## wget

`wget` 是一个命令行下的网络文件下载工具，适用于下载文档、文件、网页等，但不支持处理复杂重定向的站点。

### 常用参数

```bash
-O, --output-document=FILE     # 把下载内容保存到指定的 FILE 文件中
```

**注意**：`wget` 不支持复杂的重定向。如果目标站点使用了复杂的重定向，建议使用 `curl`。

---

## curl

`curl` 是一个基于 URL 的命令行文件传输工具，支持多种协议（HTTP、HTTPS、FTP等），适用于上传、下载文件。

### 常用参数说明

- `-s` / `--silent`：静音模式，不输出任何信息。
- `-g` / `--globoff`：关闭 URL 解析器，允许 URL 中包含 `{}`, `[]` 等字符（需按 URI 标准进行编码）。
- `-L`：自动跟随重定向。
- `-k` / `--insecure`：在证书文件缺失时忽略证书校验。

---

### 常见操作示例

1. **抓取页面内容到文件**
   ```bash
   curl -o home.html http://www.google.co.jp
   ```

2. **使用 `-O` 保存文件**
   *下载具体文件（URL 必须具体到文件名）*：
   ```bash
   curl -O http://example.com/path/to/file.jpg
   ```

   *使用正则匹配文件名下载（例如：`[0-9][0-9]` 代表任意两位数字）*：
   ```bash
   curl -O http://example.com/path/to/files/[0-9][0-9]/file.jpg
   ```

3. **发送数据（POST 请求）**
   *传递参数 `log=aaaa` 到服务器*：
   ```bash
   curl -d log=aaaa http://example.com/wp-login.php
   ```

4. **忽略 SSL 证书验证**
   *使用 `-k` 或 `--insecure` 跳过 SSL 证书验证*：
   ```bash
   curl -k https://www.example.com/file.txt -o file.txt
   curl --insecure https://www.example.com/file.txt -o file.txt
   ```