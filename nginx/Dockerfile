# build stage
FROM node:10-alpine as build-stage
WORKDIR /app/

RUN npm cache verify
RUN npm install -g @quasar/cli
COPY frontend/package.json /app/
RUN npm install --progress=false
COPY frontend /app/
RUN npm run build:pwa

# ci stage
FROM nginx:1.13.12-alpine as ci-stage
COPY ./nginx/ci.conf /etc/nginx/nginx.conf
COPY --from=build-stage /app/dist/pwa /dist/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
