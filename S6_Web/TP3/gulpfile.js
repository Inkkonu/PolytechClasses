'use strict';

/* eslint-env node */
/*
 * Lancement dans un terminal dédié (laisser le tourner indéfiniment) :
 * node_modules/.bin/gulp
 *
 * la tâche 'lint' vérifie la syntaxe des fichiers js au lancement et à chaque
 * modification d'un fichier.
 *
 */

const gulp = require('gulp'),
    cache = require('gulp-cached'),
    colors = require('ansi-colors'),
    map = require('map-stream'),
    eslint = require('gulp-eslint'),
    cssvalidate = require('gulp-w3c-css'),
    htmlvalidate = require('gulp-html'),
    bs = require('browser-sync').create();

const inputPaths = {
    JavaScript: 'js/*.js',
    Css: 'css/*.css',
    Html: '*.html',
};

gulp.task('lint', function () {
    return gulp
        .src(inputPaths.JavaScript)
        .pipe(cache('lint'))
        .pipe(eslint({
            'extends': 'eslint:recommended',
            'envs': [
                'node',
            ],
            parserOptions: {   // https://eslint.org/docs/user-guide/configuring
                ecmaVersion: 9, // spread operator 2018
            },
            // documentation des règles eslint :
            // http://eslint.org/docs/rules
            'rules': {
                'no-warning-comments': ['warn', {terms: ['todo', 'fixme', 'xxx'], location: 'anywhere'}],

                'no-console': 'off',

                'strict': ['error', 'global'],

                'indent': ['error', 4, {'SwitchCase': 1, 'flatTernaryExpressions': true, 'MemberExpression': 1}],

                'brace-style': ['error', 'stroustrup'],

                'semi': ['error', 'always'],
                'no-extra-semi': 'error',
                'semi-spacing': ['error', {'before': false, 'after': true}],

                'keyword-spacing': ['error', {'before': true, 'after': true}],

                'no-trailing-spaces': 'error',

                'no-lonely-if': 'error',
                'key-spacing': 'error',
                'comma-spacing': 'error',
                'comma-dangle': ['error', {'arrays': 'always-multiline', 'objects': 'always-multiline', 'functions': 'never'}],
                'space-infix-ops': ['error', {'int32Hint': true}],
                'array-bracket-spacing': ['error', 'never'],
                'object-curly-spacing': 'error',
                'space-before-function-paren': ['error', {'anonymous': 'always', 'named': 'never'}],
                'no-sparse-arrays': 'off',
                'prefer-rest-params': 'error',

                'wrap-iife': ['error', 'outside'],
                'no-implied-eval': 'error',
                'quotes': ['error', 'single', {'avoidEscape': true}],

                'prefer-const': 'error',
                'no-var': 'error',
                'no-undef': 'error',
                'no-unused-vars': 'error',

                'eqeqeq': 'error',
                'no-plusplus': 'error',
                'no-constant-condition': ['error', {'checkLoops': false}],
                'no-eval': 'error',
                'no-extra-bind': 'error',
            },
        }))
        .pipe(eslint.format());
});

gulp.task('validatecss', function (done) {
    bs.reload();
    gulp.src(inputPaths.Css)
        .pipe(cssvalidate())
        .pipe(map(function (file, done) {
            console.log('============== CSS ==================');
            if (file.contents.length === 0) {
                console.log('Success: ' + file.path);
                console.log(colors.green('No errors or warnings\n'));
            }
            else {
                const results = JSON.parse(file.contents.toString());
                results.errors.forEach(function (error) {
                    console.log('Error: ' + file.path + ': line ' + error.line);
                    console.log(colors.red(error.message) + '\n');
                });
                results.warnings.forEach(function (warning) {
                    console.log('Warning: ' + file.path + ': line ' + warning.line);
                    console.log(colors.yellow(warning.message) + '\n');
                });
                console.log(results.errors.length + ' error - ' + results.warnings.length + ' warnings\n');
            }
            done(null, file);
        }));
    done();
});

gulp.task('validatehtml', function (done) {
    let status = true;
    bs.reload();
    gulp.src(inputPaths.Html)
        .pipe(htmlvalidate({'Werror': true}))
        .on('error', function (error){
            status = false;
            console.log('============== HTML ==================');
            let nbErrors = 0;
            let nbWarnings = 0;
            const lines = error.message.split('\n');
            lines.forEach(function (line) {
                const parts = line.split(':');
                if (parts.length >= 4) {
                    if (parts[3].trim() === 'error') {
                        console.log(colors.red(line));
                        nbErrors += 1;
                    }
                    else if (parts[3].trim() === 'info warning') {
                        console.log(colors.yellow(line));
                        nbWarnings += 1;
                    }
                    else
                        console.log(line);
                }
            });
            console.log(nbErrors + ' error - ' + nbWarnings + ' warnings\n');
        })
        .on('end', function () {
            if (status === true) {
                console.log(colors.green('No errors or warnings\n'));
            }
        })
        .pipe(map(function (file, done) {
            console.log('============== HTML ==================');
            done(null, file);
        }));
    done();
});

gulp.task('browser-sync', function () {
    bs.init({
        server: {
            baseDir: './',
        },
        files: ['css/style.css', 'js/*.js', '*.html'],
        port: 3002,
    });
});

gulp.task('watchjs', function (done) {
    gulp.watch(inputPaths.JavaScript, gulp.series('lint'));
    done();
});

gulp.task('watchcss', function (done) {
    gulp.watch(inputPaths.Css, gulp.series('validatecss'));
    done();
});

gulp.task('watchhtml', function (done) {
    gulp.watch(inputPaths.Html, gulp.series('validatehtml'));
    done();
});

gulp.task('validate', gulp.series('validatehtml', 'validatecss'));

gulp.task('default', gulp.series('lint', 'validate', 'watchjs', 'watchcss', 'watchhtml', 'browser-sync'));

// vim:set et sw=4:
