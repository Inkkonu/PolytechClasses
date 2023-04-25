/*
 * By Killian Blain :)
 *
 * 1. Expliquez la nature du problème.
 * Un undefined apparait dans le tableau après avoir inversé pour la première fois.
 * Cela arrive car dans la fonction findMinIndex(), la variable i est la même que dans sortTable, ce qui casse tout.
 *
 * 2. Expliquez de quelle manière très simple on aurait pu détecter le problème.
 * En n'utilisant pas var.
 *
 * 3. Corrigez ce code défaillant (le code corrigé doit être le plus proche possible du code initial).
 * Voir lignes 30 et 31.
 */

"use strict";

const t = [0, 3, 2, 5];
console.log("Smallest value " + t[findMinIndex(t, 0, t.length)]);
console.log(
  "Smallest value among the last three " + t[findMinIndex(t, 1, t.length)]
);
sortTable(t);
console.log(t);

/**
 * return the index of the minimal value in the array 't' from index
 * 'from' to index 'to' (excluded)
 */
function findMinIndex(t, from, to) {
  let j = from; //Fix
  for (let i = from + 1; i < to; i += 1) {
    //Fix
    if (t[j] > t[i]) {
      j = i;
    }
  }
  return j;
}

/**
 * sort the table 't'
 */
function sortTable(t) {
  let j, s;
  for (let i = 0; i < t.length - 1; i += 1) {
    // Find the index of the minimal value in the unsorted part of
    // the array
    j = findMinIndex(t, i, t.length);
    // Swap the ith minimal value
    s = t[j];
    t[j] = t[i];
    t[i] = s;
  }
}
