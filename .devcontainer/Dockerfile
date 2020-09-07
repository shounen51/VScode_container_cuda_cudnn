FROM nvidia/cuda:10.2-cudnn7-devel-ubuntu18.04
# ARG VARIANT="3"
# FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# [Option] Install Node.js
# ARG INSTALL_NODE="true"
# ARG NODE_VERSION="lts/*"
# RUN if [ "${INSTALL_NODE}" = "true" ]; then su vscode -c "source /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi 

RUN apt update && apt install curl wget git htop neofetch python3.8 python3.8-dev python3-pip libjpeg-dev cmake cmake-qt-gui p7zip-full gcc g++ ninja-build fonts-noto-cjk-extra -y \
    && pip3 install pipenv \
    && pip3 install opencv-python \
    && apt install libgl1-mesa-glx -y \
    && pip3 install torch torchvision

# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

# [Optional] Uncomment this line to install global node packages.
# RUN su vscode -c "source /usr/local/share/nvm/nvm.sh && npm install -g <your-package-here>" 2>&1