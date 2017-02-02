#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import pyperclip
import time

m = PyMouse()
k = PyKeyboard()

def writeContent(title, content):
    m.click(300, 180, 1, 3)
    time.sleep(1)
    k.type_string(title)
    
    m.click(300, 300, 1, 2)
    time.sleep(1)
    k.press_key(k.alt_key)
    k.tap_key('a')
    k.release_key(k.alt_key)
    k.tap_key(k.delete_key)
 
    #k.type_string(content)
    pyperclip.copy(content)
    m.click(300, 300, 1, 2)
    time.sleep(0.5)
    k.press_key(k.control_key)
    k.tap_key('v')
    k.release_key(k.control_key)


def writeAbstract(abstract):
    m.click(m.screen_size()[0]/2, m.screen_size()[1]/2, 1, 3)
    time.sleep(1)
    k.press_key(k.alt_key)
    k.tap_key('a')
    k.release_key(k.alt_key)
    k.tap_key('space')

    k.type_string(abstract)

def addSetting(groups):
    assert len(groups) < 5 and len(groups) > 0

    # set 原创 
    pos = [621, 346]
    m.click(pos[0], pos[1], 1, 3)
    time.sleep(1)
    
    pos = [621, 411]
    m.click(pos[0], pos[1], 1, 1)
    time.sleep(1)
   
    # set article type
    pos = [621, 390]
    m.click(pos[0], pos[1], 1, 2)
    time.sleep(0.5)
    for g in groups:
        k.type_string(g)
        k.tap_key(k.enter_key)
    time.sleep(1)

    # set 综合
    pos = [621, 674]
    m.click(pos[0], pos[1], 1, 1)
    time.sleep(1)

    pos = [621, 640]
    m.click(pos[0], pos[1], 1, 1)
    time.sleep(1)


if __name__ == "__main__":
    #title="hello, csdn"
    #content="test"
    #writeContent(title, content)

    addSetting(['linux','apple'])
