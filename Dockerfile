FROM python:3.7
LABEL maintainer="domikus@mail.ru"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8020
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
