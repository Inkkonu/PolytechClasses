/*
 * By Killian Blain :)
 */

"use strict";

const albums = {
  "Fresh Cream": {
    artist: "Cream",
    year: 1966,
    title: "Fresh Cream",
  },
  "Hot Rats": {
    artist: "Frank Zappa",
    year: 1969,
    title: "Hot Rats",
  },
  "Space Oddity": {
    artist: "David Bowie",
    year: 1969,
    title: "Space Oddity",
  },
  "Merry Christmas": {
    artist: "Mariah Carey",
    year: 1994,
    title: "Merry Christmas",
  },
  "Songs from a Room": {
    artist: "Leonard Cohen",
    year: 1969,
    title: "Songs from a Room",
  },
  Ummagumma: {
    artist: "Pink Floyd",
    year: 1969,
    title: "Ummagumma",
  },
  "Camembert Electrique": {
    artist: "Gong",
    year: 1971,
    title: "Camembert Electrique",
  },
  "The Piper at the Gates of Dawn": {
    artist: "Pink Floyd",
    year: 1967,
    title: "The Piper at the Gates of Dawn",
  },
};

function albumTitle(album) {
  return album["title"];
}

function albumArtist(album) {
  return album["artist"];
}

function albumYear(album) {
  return album["year"];
}

console.log(albumArtist(albums["Ummagumma"]));
console.log(albumTitle(albums["Ummagumma"]));
console.log(albumYear(albums["Ummagumma"]));

//To put data into the JSON file
//console.log(JSON.stringify(albums, null, 4));
