FROM python:3.8-slim

# Update and install
RUN apt update && apt install sudo

# Package
RUN mkdir -p /Python_install_dependence/
RUN mkdir -p /Python_install_dependence/package/

# Packages
ADD /package/ansible.py /Python_install_dependence/package/
ADD /package/docker.py /Python_install_dependence/package/
ADD /package/gitlab.py /Python_install_dependence/package/
ADD /package/terraform.py /Python_install_dependence/package/
ADD /package/vsCode.py /Python_install_dependence/package/

# Main python
ADD dependence.py /Python_install_dependence/
ADD main.py /Python_install_dependence/

ENTRYPOINT ["python3", "/python/main.py"]
