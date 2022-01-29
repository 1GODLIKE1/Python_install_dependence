import os
def install_gitlab():
    os.system("echo '======INSTALL GITLAB CI/CD======'")
    os.system("sudo apt update -y")
    os.system("sudo apt upgrade -y")
    os.system("curl -s https://packages.gitlab.com/install/repositories/gitlab/gitlab-ce/script.deb.sh | sudo bash")
    os.system("sudo apt update -y")
    os.system("sudo apt install gitlab-ce -y")