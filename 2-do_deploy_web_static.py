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
    """deploy files"""
    archive_filename = os.path.basename(archive_path)
    archive_name = os.path.splitext(archive_filename)[0]
    # check of archive path exists, return false
    if not os.path.exists(archive_path):
        return False
    try:
        # put archive to /tmp/
        put(archive_path, '/tmp/')
        # uncompres to /data/...
        target_dir = "/data/web_static/releases/" + archive_name
        run("mkdir -p " + target_dir)

        run("tar -xzf /tmp/" + archive_filename + " -C " + target_dir)
        # delete the archive
        run("rm /tmp/" + archive_filename)
        # Move the contents of the extracted folder
        run("mv " + target_dir + "/web_static/* " + target_dir)
        # Remove the extracted folder
        run("rm -rf " + target_dir + "/web_static")
        # delete sym link /data/../durent
        run("rm -rf /data/web_static/current")
        # create new to link to archive extract
        run("ln -s " + target_dir + " /data/web_static/current")
        return True
    except Exception as e:
        print(e)
        return False
