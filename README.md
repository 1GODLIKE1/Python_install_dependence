# INSTALLING DEPENDENCIES ON UBUNTU 20.04 LTS
- Terraform
- GitLab CI/CD
- Ansible
- Visual Studio Code
- Docker
## RUN
To run, you need to run main.py 
After installation, you need to edit the GitLab configuration file. 
```bash
nano /etc/gitlab/gitlab.rb
```

After that, run the setup using the command:gitlab-ctl
```bash
sudo gitlab-ctl reconfigure
```
