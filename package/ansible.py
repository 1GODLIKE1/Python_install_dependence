import os
def install_ansible():
    os.system("echo '======INSTALL ANSIBLE======'")        
    os.system("sudo apt install python3-pip -y")
    os.system("sudo pip3 install ansible -y")