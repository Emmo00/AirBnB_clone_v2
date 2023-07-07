#!/usr/bin/python3
""" generate .tgz file form the contents of web_static folder in
the AirBnB repo"""
from fabric.api import local, env
from datetime import datetime

env.hosts = ['localhost']
env.user = 'root'


def do_pack():
    """ do the actual packing"""
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_" + time + ".tgz"
    local("mkdir -p versions")
    local("tar -czvfa versions/" + archive_name + " web_static/")
