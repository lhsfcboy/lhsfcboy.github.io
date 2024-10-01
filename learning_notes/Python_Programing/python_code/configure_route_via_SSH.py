作者：林哲
链接：https://www.zhihu.com/question/50722997/answer/122500314
来源：知乎
著作权归作者所有，转载请联系作者获得授权。

# -*- coding: utf-8 -*-
import paramiko
import time
import os
import logging
PYTHONUNBUFFERED = 1

logging.root.setLevel(level = logging.INFO)

command_list = ['configure',
                'run show conf|display set|no-more',
                'exit',
                'exit']

host_ip = '192.168.88.1'
host_port = 22
host_username = 'root'
host_password = 'root123'

command_file = r''
host_file = r''
# 针对不同设备执行不同查询命令


def main():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh_client.connect(host_ip, host_port,host_username,host_password,timeout=5)
    except:
        logging.warning('尝试登录'+host_ip+'失败')
        return
    stdin, stdout, stderr = ssh_client.exec_command('cli', 10)
    for command_item in command_list:
        stdin.write(command_item+'\n')

    # 有两种方法可以退出，一种是执行exit让服务器断开SSH来退出，一种是判别字符串用客户端断开SSh来退出。
    stdin.flush()
    # 最后需要刷新输入才能退出
    with open(today+'\\'+host_ip+'.txt', 'w') as w_file:
        for line in stdout:
            # print line.strip('\n') #输出本身会带有\n，不去掉会多出很多空行
            w_file.write(line)
    logging.info('登录'+host_ip+'抓取设备完毕，已断开SSH连接')
    return

if __name__ == '__main__':
    today = time.strftime('%Y%m%d',time.localtime(time.time()))
    # 每天创建一个目录
    if not os.path.isdir(today):
        os.mkdir(today)
    this_second = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    logging.info('准备开始登录设备，当前时间：'+this_second)
    main()
    this_second = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    logging.info('执行完毕设备，当前时间：'+this_second)
