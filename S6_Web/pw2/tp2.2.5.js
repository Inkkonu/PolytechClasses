/*
 * By Killian Blain :)
 */

"use strict";

const albums = require("./albums.json");

function Album(o) {
  Object.assign(this, o);
}

const l = Object.entries(albums)
  .map(([title, album]) => [title, new Album(album)])
  .map(([title, album]) => ({ [title]: album }));

const end = {};
Object.assign(end, ...l);
console.log(end);
