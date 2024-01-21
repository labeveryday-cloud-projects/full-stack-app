FROM node:17-alpine
WORKDIR /app
COPY package*.json /app/

RUN npm i --silent
# This can be found in package.json
RUN npm i -g react-scripts@5.0.1 --silent
RUN npm i axios --silent

COPY . ./

CMD ["npm", "start"]