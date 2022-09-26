FROM ubuntu:latest

RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -qq -y python3 sqlite3 python3-pip

COPY app/ /var/www/html
RUN chown -R www-data:www-data /var/www/html

WORKDIR /var/www/html

#install requirements as root
RUN python3 -m pip install -r requirements.txt

USER www-data

#run flask
EXPOSE 5000

#best practice is to have this as non-readable but doing this as quick fix
RUN chmod +x /var/www/html entrypoint.sh

ENTRYPOINT ./entrypoint.sh