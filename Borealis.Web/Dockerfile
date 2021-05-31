# FROM node:10-alpine as build-step
# RUN mkdir -p /app
# WORKDIR /app
# COPY package.json /app
# RUN npm install
# COPY . /app
# RUN npm run
FROM nginx:1.17.1-alpine
COPY /conf/nginx.conf /etc/nginx/nginx.conf 
COPY /dist/borealis /usr/share/nginx/html