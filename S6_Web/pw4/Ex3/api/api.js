"use strict";

// import du module Express
let express = require("express");
let app = express();

const fetch = require("node-fetch");
const { DOMParser } = require("xmldom");
const xpath = require("xpath");
const urlencode = require("urlencode");

app.get("/genres", (request, response) => {
  fetch(
    "http://ws.audioscrobbler.com/2.0/?method=tag.getTopTags&api_key=2c08f218f45c6f367a0f4d2b350bbffc"
  )
    .then((response) => {
      if (!response.ok) {
        console.error("Response not OK");
      } else {
        return response.text();
      }
    })
    .then((xml) => {
      const dom = new DOMParser().parseFromString(xml);
      const tags = xpath.select("//tag/name/text()", dom);
      const promises = tags.map(async (genre) => {
        const xml = await (
          await fetch(
            "http://ws.audioscrobbler.com/2.0/?method=tag.getinfo&tag=" +
              urlencode(genre.toString()) +
              "&api_key=2c08f218f45c6f367a0f4d2b350bbffc"
          )
        ).text();
        const doc = new DOMParser().parseFromString(xml);
        const description = xpath.select("/lfm/tag/wiki/content/text()", doc);
        return Promise.resolve({
          name: genre.toString(),
          id: genre.toString(),
          description: description.toString(),
        });
      });
      Promise.all(promises).then((values) => {
        response.json(values);
      });
    });
});

// export de notre application vers le serveur principal
module.exports = app;
