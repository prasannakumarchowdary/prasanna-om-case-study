FROM node:18-alpine

WORKDIR /app

# Copy dependencies first
COPY package*.json ./
RUN npm install

# Copy app code
COPY . .

EXPOSE 4567

CMD ["node", "express.js"]
