/*
 * By Killian Blain :)
 */

'use strict';

Artist.list = [];

function Artist(name) {
    this.name = name;
    this.albums = [];
    Artist.list.push(this);
}

Artist.withName = function (name) {
    for (const a of Artist.list) {
        if (a.name === name) {
            return a;
        }
    }
    return null;
};

Artist.prototype.addAlbum = function (album) {
    this.albums.push(album);
};

function Album(album) {
    let a = Artist.withName(album.artist);
    if (a === null) {
        a = new Artist(album.artist);
    }
    this.title = album.title;
    this.year = album.year;
    this.artist = a;
    a.addAlbum(album);
}

const album = new Album({title: 'Fresh Cream', artist: 'Cream', year: 1966});
console.log(album);
console.log(album.artist);