'use strict';

const express = require('express');

const app = express();

app.use('/', express.static('public'));
app.listen(8080);

const api = require('./api/api');
app.use('/api', api);