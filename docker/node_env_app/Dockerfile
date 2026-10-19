FROM node:alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
ENV APP_MODE=development
EXPOSE 3000
CMD ["node", "app.js"]
