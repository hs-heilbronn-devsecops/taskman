FROM gitpod/workspace-full:latest

USER gitpod

ADD requirements.txt .
ADD requirements-dev.txt .

RUN pyenv install 3.9 \
        && pyenv global 3.9

RUN pip3 install -r requirements.txt
RUN pip3 install -r requirements-dev.txt