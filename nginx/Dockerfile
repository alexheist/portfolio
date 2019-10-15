FROM nginx:alpine

COPY localhost.crt /etc/ssl/certs/
COPY localhost.key /etc/ssl/private/

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d

ENTRYPOINT ["nginx","-g","daemon off;"]
