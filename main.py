import os
from dependence import other_install
from package.ansible import install_ansible
from package.terraform import install_terraform
from package.vsCode import install_vscode
from package.gitlab import install_gitlab
from package.docker import install_docker

def main():
    
    # Sudo su
    passwd = "442448247qwE"
    command = "sudo su"
    p = os.system('echo %s|sudo -S %s' % (passwd, command))

    # Methods
    other_install()
    install_ansible()
    install_terraform()
    install_vscode()
    install_gitlab()
    install_docker()

if __name__ == "__main__":
    main()