FROM node:12.16-alpine
WORKDIR /app
RUN npm install -g @quasar/cli
COPY ./compose/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

