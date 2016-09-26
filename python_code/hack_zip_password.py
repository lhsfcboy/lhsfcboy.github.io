# coding: UTF-8


# help('zipfile')
# extractall(path=None, members=None, pwd=None)

# touch 1.txt;	zip -r 1.zip 1.txt -P 123456

# import zipfile 
# try:
#     with zipfile.ZipFile('1.zip') as zFile:     #创建ZipFile对象
#         #解压文件
#         zFile.extractall(path='./',pwd=b'1314')
#         print('Extract the Zip file successfully!')
# except:
#     print('Extract the Zip file failed!')

# help('argparse')

# import argparse
# 
# parser = argparse.ArgumentParser(description='Regards to your name.')
# parser.add_argument('-n', dest='m_name', type=str, help='your name')
# options = parser.parse_args()
# print('Hello',options.m_name)

# python test.py -n testuser


# echo -e "123451\n123454\n123455\n123456" > pwd.txt

# python hack_zip_password.py -f 1.zip -w pwd.txt


import zipfile
import argparse
import os
from os.path import *

def tryZipPwd(zipFile,password,savePath):
    try:
        zipFile.extractall(path=savePath,pwd=password.encode('utf-8'))
        print('[+] Zip File decompression success,password: %s' % (password))
        return True
    except:
        print('[-] Zip File decompression failed,password: %s' % (password))
        return False


def main():
    # 这里用描述创建了ArgumentParser对象
    parser = argparse.ArgumentParser(description='Brute Crack Zip')
    # 添加-H命令dest可以理解为咱们解析时获取-H参数后面值的变量名,help是这个命令的帮助信息
    parser.add_argument('-f', dest='zFile', type=str, help='The zip file path.')
    parser.add_argument('-w', dest='pwdFile', type =str, help='Password dictionary file.')
    zFilePath = None
    pwdFilePath = None
    try:
        options = parser.parse_args()
        zFilePath = options.zFile
        pwdFilePath = options.pwdFile
    except:
        print(parser.parse_args(['-h']))
        exit(0)

    if zFilePath == None or pwdFilePath == None:
        print(parser.parse_args(['-h']))
        exit(0)

    with zipfile.ZipFile(zFilePath) as zFile:
        with open(pwdFilePath) as f:
            for pwd in f.readlines():
                p,f = split(zFilePath)
                dirName = f.split('.')[0]
                dirPath = join(p, dirName)
                try:
                    os.mkdir(dirPath)
                except:
                    pass
                ok = tryZipPwd(zFile, pwd.strip('\n'),dirPath)
                if ok:
                    break
if __name__ == '__main__':
    main()
