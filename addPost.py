#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
###########
Tool Description

Usage:
python addPost.py blog.md csdn_login

'''

from selenium import webdriver
import time
import write
import sys

def pause(length=1):
    time.sleep(length)

USERNAME = 'DuinoDu'
PASSWORD = '8460637duyuan'

def setLogin(filename):
    """Set user and password

    :filename: TODO
    :returns: TODO
    """
    with open(filename,'r') as fid:
        lines = fid.readlines()
        USERNAME = lines[0].split('\n')
        PASSWORD = lines[1].split('\n')

def addPost(title, content, abstract, groups):
    b = webdriver.Firefox()
    pause(1)
    
    b.get("http://blog.csdn.net/duinodu")
    pause(2)
    
    b.find_element_by_link_text('登录').click()
    pause(5)
    
    b.find_element_by_id('username').send_keys(USERNAME)
    pause(1)
    
    b.find_element_by_id('password').send_keys(PASSWORD)
    pause(1)
    
    b.find_element_by_class_name('logging').click()
    pause(5)
    
    b.find_element_by_link_text('写新文章').click()
    pause(5)
    
    write.writeContent(title, content)
    b.find_element_by_link_text('发表博客').click()
    pause(3)
    
    write.writeAbstract(abstract)
    b.find_element_by_link_text('下一步').click()
    pause(3)
    
    write.addSetting(groups)
    b.find_element_by_link_text('发布').click()
    pause(3)

    b.find_element_by_link_text('查看博客').click()
    pause(2)

    b.close()

def readBlog(filename):
    with open(filename, 'r') as fid:
        lines = fid.readlines()
        title = lines[0].split('\n')[0]
        groups = lines[1].split('\n')[0].split(' ')
        abstract = lines[2].split('\n')[0]
        content = ""
        for line in lines[4:]:
            content += line
        return title, groups, abstract,  content

def main(argv):
    assert(len(argv) == 3)
    setLogin(argv[2])
    print USERNAME
    print PASSWORD
    #title, groups, abstract,  content = readBlog(argv[1])
    #addPost(title, content, abstract, groups)

if __name__ == "__main__":
    print(__doc__)
    import sys
    main(sys.argv)
