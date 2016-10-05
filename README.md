# 4704-Capstone
Creating a website to display information on airplane components.

Startup Guide
  1. Install both VirtualBox and Vagrant on your machine.
  2. Clone the repository
  3. Call the commant 'vagrant up' which will boot up your VM in a headless mode and install the necessary packages to create our virtual environment.
  4. Once the spawnup has finished, call the command 'vagrant ssh' to ssh into your virtual environment.
  5. Now once inside the headless vm, we need to activate out virtual environment. Let's edit the ~/.bashrc file so we only need to call these once.
        1. Add the following to the end of the ~/.bashrc file.
             cd /vagrant
             source env/bin/activate
             alias manage="python manage.py"
             alias runserver="manage runserver 0.0.0.0:8000"
        2. Now exit the vm, and reconnect and you should see your virtual environment activated, and you should be inside the vagrant environemnt.
