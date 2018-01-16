# -*- coding: utf_8 -*-
import urllib 
import urllib2  
import re
from bs4 import BeautifulSoup

from random import randint
from time import sleep

import types
import datetime
import os
import sys
import os.path


  
url = 'http://book.qidian.com/info/1262627'
 
#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'    
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'    
headers = { 'User-Agent' : user_agent }    
req = urllib2.Request(url)    
req.add_header('User-Agent',user_agent)
response = urllib2.urlopen(req)    
html = response.read()   
soup = BeautifulSoup(html, "html.parser")

session = requests.session()
response_txt = session.get(url).text
soup = BeautifulSoup(response_txt, "html.parser")
