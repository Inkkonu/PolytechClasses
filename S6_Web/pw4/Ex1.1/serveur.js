"use strict";

const http = require("http");

const server = http.createServer(function (request, response) {
  response.writeHead(200);
  response.write("Bonjour tout le monde !");
  response.end();
});
server.listen(8080);
