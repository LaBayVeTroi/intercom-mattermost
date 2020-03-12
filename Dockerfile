FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /config
ADD /requirements.txt /config/
RUN pip install -r /config/requirements.txt && pip install gunicorn==19.6.0
RUN mkdir /src;
WORKDIR /src