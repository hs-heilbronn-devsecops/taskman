FROM python:3.9

RUN adduser taskman
USER taskman

RUN pip install --upgrade pip
ENV PATH="/home/taskman/.local/bin:${PATH}"

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
RUN pip3 install -r requirements.txt

COPY ./taskman /code/taskman

CMD ["uvicorn", "taskman.main:app", "--host", "0.0.0.0", "--port", "8080"]