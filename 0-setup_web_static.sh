supt-get update
sudo apt-get -y install nginx
sudo service nginx start
sudo mkdir -p /data/web_static/{releases/test,shared}
sudo echo '<html>
<head>
  </head>
  <body>
    Holberton School
  </body>
</html>' | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i '33 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restartdo service nginx restart
