// define the dictionary
$.i18n().load({
    'fr': {
        'title': 'TP IHM',
    },
    'en': {
        'title': 'Hello I am under the water, please help me',
    }
})

// set the locale
$.i18n({
    locale: 'en'
    //locale : navigator.language
});


let superController = new SuperController(new ModelActivation(), new ModelActivation());
