# Site vitrine EPISEN (Bootstrap)

## Français

**Ce que fait le site :** un site statique et responsive de 5 pages qui présente l'EPISEN, l'école d'ingénieurs de l'UPEC.

- `index.html` : page d'accueil.
- `formations.html` : 3 cartes pour les formations ITS, ISBS et SI, avec effet au survol. Les boutons ouvrent le site officiel [episen.u-pec.fr](https://episen.u-pec.fr).
- `enseignants.html` : 4 fiches de profil (avatar, poste, spécialité).
- `apropos.html` : chiffres clés, mission et valeurs de l'école.
- `contact.html` : adresse, téléphone et e-mail.

Toutes les pages partagent la même barre de navigation, la même image de fond et la feuille de style `css/style.css`.

**Technologies :** HTML5, CSS3, Bootstrap 5.3 (chargé par CDN : grille, navbar, cartes, badges, boutons), JavaScript.

**Lancer le site :** ouvrir `index.html` dans un navigateur. Une connexion Internet est nécessaire pour charger Bootstrap.

**Retiré pour la publication :**
- les copies des pages du site officiel de l'EPISEN (`its.html`, `ISBS_*.html`, `SI_*.html` et leurs dossiers `_files`) : les boutons renvoient maintenant vers le site officiel ;
- la vidéo de présentation de la page d'accueil (fichier de 59 Mo) et sa balise `<video>` ;
- les photos et les noms des enseignants, remplacés par un avatar neutre et « Enseignant·e 1 » à « Enseignant·e 4 » ;
- les images en double.

Autres changements : le CSS, qui était répété dans chaque page, est regroupé dans `css/style.css`, et l'image de fond est renommée sans accent (`presentation_episen.jpg`).

## English

**What it does:** a static, responsive 5-page website presenting EPISEN, the engineering school of UPEC (Université Paris-Est Créteil).

- `index.html`: home page.
- `formations.html`: 3 cards for the ITS, ISBS and SI degrees, with a hover effect. The buttons open the official website [episen.u-pec.fr](https://episen.u-pec.fr).
- `enseignants.html`: 4 teacher profile cards (avatar, position, field).
- `apropos.html`: key figures, mission and values of the school.
- `contact.html`: address, phone and email.

All pages share the same navigation bar, background image and stylesheet `css/style.css`.

**Technologies:** HTML5, CSS3, Bootstrap 5.3 (loaded from a CDN: grid, navbar, cards, badges, buttons), JavaScript.

**How to run:** open `index.html` in a browser. An Internet connection is needed to load Bootstrap.

**Removed for publication:**
- the copies of pages from the official EPISEN website (`its.html`, `ISBS_*.html`, `SI_*.html` and their `_files` folders): the buttons now link to the official website;
- the home page presentation video (a 59 MB file) and its `<video>` tag;
- the teachers' photos and names, replaced by a neutral avatar and "Enseignant·e 1" to "Enseignant·e 4";
- duplicate images.

Other changes: the CSS, previously repeated in every page, now lives in `css/style.css`, and the background image was renamed without an accent (`presentation_episen.jpg`).
