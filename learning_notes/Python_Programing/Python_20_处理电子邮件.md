# 电子邮件

请务必先理解: [邮件发送的基本过程与概念](https://zhuanlan.zhihu.com/p/306569650)

## POP3的例子

```python
# -*- coding: utf-8 -*-
import poplib,email,time

# 基本設定
server    = "mail.white-azalea.net"
port      = 110
user_id   = "white-azalea"
user_pass = "zzzzzzzzzzzzzz"

# サーバに接続
pop3 = poplib.POP3(server,port)
pop3.apop(user_id,user_pass)

# メール一覧の取得
mail_list = pop3.list()

# メールのリストは要素1に入ってるから
for mail_id in mail_list[1]:
    (no,msg_size) = mail_id.split(" ")
    # メッセージ番号指定で取り出し
    mail_data = pop3.retr(no)
    msg = email.message_from_string("\n".join(mail_data[1]))
```

## IMAP的例子

IMAP[源代码](https://github.com/python/cpython/blob/3.7/Lib/imaplib.py),
[API](https://docs.python.org/3/library/imaplib.html):

```python
# coding: utf-8

import imaplib

server = 'imap.mail.yahoo.co.jp'

m = imaplib.IMAP4_SSL(server)

account = raw_input('account >>> ')
password = raw_input('password >>> ')

k, login = m.login(account,password)
print(login[0])
```

## 对邮件的解析

务必使用专门的第三方工具!! 例如: [pip install mail-parser](https://github.com/SpamScope/mail-parser)

```python
mail = mailparser.parse_from_bytes(byte_mail)
mail.from_
# [('Yahoo!ダイ', 'directoffer-master@mail.yahoo.co.jp')]

mail.subject
mail.text_plain: only text plain mail parts in a list
```
