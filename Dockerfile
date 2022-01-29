FROM python:3.8-slim

# Update and install
RUN apt update && apt install sudo

# Package
RUN mkdir -p /python/
RUN mkdir -p /python/package/

# Packages
ADD /package/ansible.py /python/package/
ADD /package/docker.py /python/package/
ADD /package/gitlab.py /python/package/
ADD /package/terraform.py /python/package/
ADD /package/vsCode.py /python/package/

# Main python
ADD dependence.py /python/
ADD main.py /python/

ENTRYPOINT ["python3", "/python/main.py"]
