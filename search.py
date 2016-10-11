#! /usr/bin/env python
# ! coding=utf-8
# ! author scq000

from pyrailgun import RailGun
import json
import sys
from encodingUtils import EncodingUtils

reload(sys)
sys.setdefaultencoding('utf8')

encodingUtils = EncodingUtils()
railgun = RailGun(encodingUtils)
railgun.setTask(file("sites.json"))
railgun.fire()
nodes = railgun.getShells('default')

file = file("result.txt", "w+")
for item in nodes:
    node = nodes[item]
    # print node
    file.write(node.get('name', [""])[0] + "\r\n")
    file.write(node.get('src', [""])[0] + "\r\n")
    file.write(node.get('size', [""])[0] + "\r\n")
    file.write(node.get('updateTime', [""])[0] + "\r\n====================================\n")