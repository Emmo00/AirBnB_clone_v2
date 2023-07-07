#!/usr/bin/python3
""" generate .tgz file form the contents of web_static folder in
the AirBnB repo"""
from fabric.api import local, env
from datetime import datetime
import os

env.hosts = ['localhost']
env.user = 'root'


def do_pack():
    """ do the actual packing"""
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_" + time + ".tgz"
    local("mkdir -p versions")
    local("tar -czvf versions/" + archive_name + " web_static")
    return 'versions/' + archive_name


def do_deploy(archive_path):
    archive_name = archive_path.split('/')[-1]
    # check of archive path exists, return false
    if not os.path.exists(archive_path):
        return False
    # put archive to /tmp/
    result1 = put(archive_path, '/tmp/')
    # uncompres to /data/...
    result2 = run("tar -xzf /tmp/" + archive_name + " -C /data/web_static/releases/" + archive_name.strip('.tgx') + "/")
    # delete the archive
    result3 = run("rm /tmp/" + archive_name)
    # delete sym link /data/../durent
    result4 = run("rm -rf /data/web_static/current")
    # create new to link to archive extract
    result5 = run("ln -s /data/web_static/releases/" + archive_name.strip(".tgz") + "/ /data/web_static/current")
    return True
