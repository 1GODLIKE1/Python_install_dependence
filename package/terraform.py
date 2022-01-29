import os
def install_terraform():
    os.system("echo '======INSTALL TERRAFORM======'")
    os.system("sudo apt-get update -y")
    os.system("curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -")
    os.system("sudo apt-add-repository 'deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main'")
    os.system("sudo apt-get -y update && sudo apt-get install terraform -y")