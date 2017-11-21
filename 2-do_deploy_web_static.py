#!/usr/bin/python3
'''
script (based on the file 1-pack_web_static.py) that distributes an archive
to your web servers, using the function do_deploy
'''
from fabric.api import *
from fabric.operations import run, put, sudo
import os.path
env.hosts = ['142.44.167.24', '144.217.246.211']


def do_deploy(archive_path):
    '''
    script that uploads the archive to /tmp/, uncompresses the folder,
    deletes the archive, deletes the symbolic link, and creates a new
    symbolic link
    '''
    if (os.path.isfile(archive_path) is False):
        return False
    try:
        put(archive_path, '/tmp/')
        name = archive_path.split('/')[-1]
        new_dir = ('/data/web_static/releases/' + name.split('.')[0])
        run('sudo mkdir -p {}'.format(new_dir))
        run('sudo tar -xzf /tmp/{} -C {}'.format(name, new_dir))
        run('sudo rm /tmp/{}'.format(name))
        run('sudo mv {}/web_static/* {}/'.format(new_dir, new_dir))
        run('sudo rm -rf {}/web_statuc'.format(new_dir))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {} /data/we_static/current'.format(new_dir))
        return True
    except:
        return False
