'use strict';

// import du module Express
let express = require('express');
let app = express();


const data = require('./data/db.json');

app.get('/genres', (request, response) => {
    const genres = JSON.stringify(data.genres);
    response.set('Content-Type', 'application/json; charset=utf-8');
    response.status(200).send(genres);
});

app.get('/genres/:genre/artists', (request, response) => {
    data.genres.forEach(genre => {
        if (genre.id === request.params.genre) {
            const artists = JSON.stringify(data.artists.filter(element => element.genreId === request.params.genre));
            response.set('Content-Type', 'application/json; charset=utf-8');
            response.status(200).send(artists);
        }
    });
    response.status(404).send('Erreur 404');

});

// export de notre application vers le serveur principal
module.exports = app;

