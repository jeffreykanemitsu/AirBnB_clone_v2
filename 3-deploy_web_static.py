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


def deploy():
    '''
    creates and distributes archive to web server using func deploy
    '''
    try:
        pack = do_pack()
        dep = deploy(pack)
        return(dep)
    except:
        return(False)
