#!/usr/bin/python3
'''
script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack, otherwise
return none.
'''
from fabric.api import *
import time
from datetime import date


def do_pack():
    ymdhms = time.strftime('%Y%m%d%H%M%S')
    try:
        local('mkdir -p versions')
        local('tar -cvzf versions/web_static_{}.tgz web_static'.format(ymdhms))
        return ('versions/web_static_{}.tgz'.format(ymdhms))
    except:
        return None
