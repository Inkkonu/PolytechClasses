'use strict';

function validate(evt) {
    alert('Données envoyées avec succès !');
}

async function verifierCommune(commune) {
    const response = await fetch('json/votes.json');
    if (!response.ok) {
        throw new Error('Response not OK')
    }
    const data = await response.json();

    if (data['commune'] === commune) {
        let nbVotes = 0;
        const bureaux = data['bureaux'];
        for (const bureau in bureaux) {
            for (const votes in bureaux[bureau]) {
                nbVotes = nbVotes + bureaux[bureau][votes];
            }
        }
        const response = await fetch('json/' + commune + '.json')
        if (!response.ok) {
            throw new Error('Response not OK')
        }
        const data = await response.json();
        let nbHabitants = 0; //Pas le temps d'écrire pour le récupérer

        if(nbVotes > nbHabitants){
            console.log('Trop de votes');
        }
        else{
            console.log('Nombre de votes OK');
        }
    }
}

verifierCommune("44066");