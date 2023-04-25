"use strict";

const http = require("http");

const server = http.createServer((request, response) => {
  if (request.method !== "GET") {
    response.writeHead(405);
  } else {
    const [url, requestChain] = request.url.split("?");
    const html =
      "<!DOCTYPE html>" +
      "<html lang='fr'>" +
      "<head>" +
      "<title>Bonjour</title>" +
      '<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">' +
      "</head>" +
      "<body>" +
      "<p>Analyse de votre requête:</p>" +
      "<p>Vous accédez à l'url : " +
      url +
      "</p>" +
      "<p>La chaine de requête est : " +
      requestChain +
      "</p>" +
      "</body>" +
      "</html>";

    response.writeHead(200, {
      "Content-Length": Buffer.byteLength(html),
      "Content-Type": "text/html; charset=utf-8",
    });
    response.write(html);
  }
  response.end();
});

server.listen(8080);
