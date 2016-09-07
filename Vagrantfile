# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "private_network", ip: "192.168.33.10"

  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y python-pip python-dev
    sudo pip install virtualenv
    cd /vagrant
    virtualenv env --always-copy
    source env/bin/activate
    pip install -r requirements/vm.txt

    echo 'cd \\vagrant' >> ~/.bashrc
    echo 'source env/bin/activate' >> ~/.bashrc
    echo "alias manage='python manage.py'" >> ~/.bashrc
    echo "alias runserver='manage runserver 0.0.0.0:8000'" >> ~/.bashrc
  SHELL
end