FROM node:10.9.0

WORKDIR /var/www/client
COPY . /var/www/client/
RUN yarn install --production=false
