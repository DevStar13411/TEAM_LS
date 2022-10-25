FROM node as build-stage
WORKDIR /app
COPY /vue/package*.json .
RUN npm install
COPY /vue/ .
RUN npm run build

FROM nginx
RUN rm /etc/nginx/nginx.conf
COPY nginx/nginx.conf /etc/nginx/
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx/conf.d/default.conf /etc/nginx/conf.d/
RUN rm /usr/share/nginx/html/*
COPY --from=build-stage /app/dist /usr/share/nginx/html

CMD ["nginx", "-g","daemon off;"]

EXPOSE 80