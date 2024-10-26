FROM ubuntu:latest

LABEL maintainer="Manian VSS<manianvss@hotmail.com>"

RUN apt -y update \
	&& apt -y upgrade \
	&& apt -y install curl sshpass iputils-ping vim wget netcat net-tools\
	&& apt -y install python3 \
	&& apt -y install python-is-python3 python3-pip\
	&& apt -y install libpq-dev \
	&& rm -rf /var/cache/apt/*

COPY diti_server /diti_server
# COPY webui/build /diti_server/build
COPY scripts/* /diti_server

WORKDIR /diti_server
RUN pip install -r requirements.txt
RUN bash cleandb.sh

# ENV DATABASE__NAME=diti
# ENV DATABASE__USER=ditiadmin
# ENV DATABASE__PASSWORD=ditiadmin@123
# ENV DATABASE__HOST=localhost
# ENV DATABASE__PORT=5432

# ENV mode=production
# ENV DJANGO__bool__DEBUG=False

EXPOSE 8000
ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000","--insecure"]
