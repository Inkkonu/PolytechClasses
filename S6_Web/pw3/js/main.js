/*
 * By Killian Blain :)
 */
"use strict";

/* eslint-env browser */
console.log("I loaded correctly :)");

loadGenres();

function loadGenres() {
  fetch("http://localhost:3000/genres")
    .then((response) => {
      if (!response.ok) {
        console.error("Response not OK");
      } else {
        return response.json();
      }
    })
    .then((response) => {
      const select = document.querySelector("select");
      select.addEventListener("change", () => {
        const select = document.querySelector("select");
        loadArtists(
          response.find(
            (elem) => elem["id"] === select.options[select.selectedIndex].value
          )
        );
      });
      for (const g in response) {
        const opt = document.createElement("option");
        opt.value = response[g]["id"];
        opt.innerHTML = response[g]["name"];
        select.appendChild(opt);
      }
      loadArtists(
        response.find(
          (elem) => elem["id"] === select.options[select.selectedIndex].value
        )
      );
    })
    .catch((error) => console.error(error));
}

async function loadArtists(genre) {
  const topArtists = document.getElementById("topArtists");
  topArtists.textContent = "Top " + genre.name + " artists";
  const genreDescription = document.getElementById("genreDescription");
  genreDescription.textContent = genre.description;

  const response = await fetch(
    "http://localhost:3000/genres/" + genre.id + "/artists"
  );
  if (!response.ok) {
    throw new Error("Response not OK");
  }

  const json = await response.json();
  const topAlbumsList = document.getElementById("topAlbums");
  topAlbumsList.innerHTML = "";
  json.forEach((artist) => {
    const li = document.createElement("li");
    const a = document.createElement("a");
    a.id = artist["id"];
    a.href = "#";
    a.addEventListener("click", artistSelected);

    const h3 = document.createElement("h3");
    h3.textContent = artist["name"];
    a.appendChild(h3);
    li.appendChild(a);
    const img = document.createElement("img");
    img.src = artist["photo"];
    li.appendChild(img);
    topAlbumsList.appendChild(li);
  });
}

async function artistSelected(evt) {
  const response = await fetch(
    "http://127.0.0.1:3000/artists/" + evt.target.parentElement.id + "/albums"
  );
  if (!response.ok) {
    throw new Error("Response not OK");
  }

  const json = await response.json();
  const tableBody = document.getElementById("albumsTableBody");
  tableBody.innerHTML = "";
  json.forEach((element) => {
    const line = document.createElement("tr");

    const img_th = document.createElement("th");
    const img = document.createElement("img");
    img.src = element.cover;
    img.alt = element.id;
    img_th.appendChild(img);
    line.appendChild(img_th);

    const title_th = document.createElement("th");
    title_th.textContent = element.title;
    line.appendChild(title_th);

    const year_th = document.createElement("th");
    year_th.textContent = element.year;
    line.appendChild(year_th);

    const label_th = document.createElement("th");
    label_th.textContent = element.label;
    line.appendChild(label_th);

    tableBody.appendChild(line);
  });

  const popup = document.getElementById("albums");
  popup.style.visibility = "visible";
  popup.style.opacity = "1";
  popup.style.transition = "ease-in 1s";
  popup.style.top = `${
    document.body.clientHeight / 2.0 - popup.clientHeight / 2.0
  }px`;
  popup.style.left = `${
    document.body.clientWidth / 2.0 - popup.clientWidth / 2.0
  }px`;

  const button = document.getElementById("okButton");
  button.addEventListener("click", () => {
    popup.style.visibility = "hidden";
    popup.style.opacity = "0";
    popup.style.transition = "ease-out 0.5s";
  });
}
