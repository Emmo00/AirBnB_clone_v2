#!/usr/bin/env bash
# sets up web server for the deployment of web_static

# install nginx if not installed
apt upgrade -y
apt install -y nginx

# create folders and files
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" >  /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/

config_file="/etc/nginx/sites-available/default"

# backup config file
cp "$config_file" "$config_file.bak"

# new location
location="location \/hbnb_static {\n    alias \/data\/web_static\/current\/;\n}"

sudo sed -i "/^\s*server\s*{/,/^\s*}/ s|^\s*}|\t$location_block\n\n&|" $config_file

nginx -t

service nginx restart
