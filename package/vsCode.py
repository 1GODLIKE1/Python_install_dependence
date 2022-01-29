import os
def install_vscode():
    os.system("echo '======INSTALL VISUAL STUDIO CODE======'")
    os.system("wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg && sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/ && sudo sh -c 'echo 'deb [arch=amd64,arm64,armhf signed-by=/etc/apt/trusted.gpg.d/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main' > /etc/apt/sources.list.d/vscode.list' && rm -f packages.microsoft.gpg")
    os.system("sudo apt update -y")
    os.system("sudo apt install code -y")