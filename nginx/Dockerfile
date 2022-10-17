FROM nginx

RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/
RUN rm /etc/nginx/conf.d/default.conf
COPY conf.d/default.conf /etc/nginx/conf.d/

CMD ["nginx", "-g","daemon off;"]

EXPOSE 80