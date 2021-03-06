const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const morgan = require('morgan');
const config = require('./src/configs/api.config');
//project-imports

const server = express();
server.use(cors());
server.use(bodyParser.json());
server.use(morgan('dev'));
//defile-routes

server.listen(config.port, () =>
  console.log('API-ENDPOINT are running (:' + config.port + ')')
);
