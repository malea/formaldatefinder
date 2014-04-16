#!/usr/bin/env bash

apt-get update

# download database server(s)
apt-get install -y libsqlite3-dev postgresql-9.1
apt-get install -y postgresql-server-dev-9.1

# download apt-add-repository command
apt-get install -y python-software-properties
apt-get update

# download python 3.4 (and pip3)
add-apt-repository -y ppa:fkrull/deadsnakes
apt-get update
apt-get install -y python3.4 python3.4-dev
ln -s /usr/bin/python3.4 /usr/bin/python3
ln -s /usr/bin/python3.4 /usr/local/bin/python
python3 -mensurepip

# allow postgres connections with no auth
echo "local all all ident" >> /etc/postgresql/9.1/main/pg_hba.conf
echo "host all all 127.0.0.1/32 trust" >> /etc/postgresql/9.1/main/pg_hba.conf
echo "host all all ::1/128 trust" >> /etc/postgresql/9.1/main/pg_hba.conf
/etc/init.d/postgresql restart

# create database and users
sudo -u postgres createuser --superuser root
createuser --superuser vagrant
sudo -u postgres createdb formaldatefinder

# add DB url to bash config
echo "export DATABASE_URL=\"postgres://vagrant@localhost/formaldatefinder\"" >> /home/vagrant/.bashrc

# install Python packages
cd /vagrant
pip3 install -r requirements.txt

# install Heroku toolbelt
wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh
