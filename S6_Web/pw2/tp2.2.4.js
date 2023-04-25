/*
 * By Killian Blain :)
 */

"use strict";

function Album(o) {
  Object.assign(this, o);
}

Album.prototype.getTitle = function () {
  return this.title;
};

Album.prototype.getArtist = function () {
  return this.artist;
};

Album.prototype.getYear = function () {
  return this.year;
};

const album = new Album({ title: "Fresh Cream", artist: "Cream", year: 1966 });
console.log(album.getTitle());
console.log(album.getArtist());
console.log(album.getYear());
