import os
def other_install():
    os.system("echo '======INSTALL OTHER======'")
    os.system("sudo apt install curl -y")
    os.system("sudo apt-get install ca-certificates -y")
    os.system("sudo apt-get install gnupg -y")
    os.system("sudo apt-get install lsb-release -y")      
    os.system("sudo apt install openssh-server -y")
    os.system("sudo apt install software-properties-common -y")
    os.system("sudo apt install apt-transport-https -y")

    # Update && Upgrade
    os.system("sudo apt-get update -y")
    os.system("sudo apt-get upgrade -y")