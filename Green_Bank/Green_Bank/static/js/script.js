let div_vehicule = document.getElementsByClassName('type_vehicule')[0];
let div_energie = document.getElementsByClassName('energie')[0];
let div_kilometrage = document.getElementsByClassName('kilometrage')[0];
let div_annee = document.getElementsByClassName('annee')[0];
let div_passager = document.getElementsByClassName('nombre_passager')[0];
let div_resultat = document.getElementsByClassName('resultat')[0];

let form = document.getElementsByClassName('form_resultat')[0];
let input_list_choix = document.getElementsByName('liste_choix')[0];

let choix = document.getElementsByClassName('choix');
let liste_choix = {};

for (let i = 0; i < choix.length; i++) {
    choix[i].addEventListener('click', function () {
        let value = this.getAttribute('data-value');
        liste_choix[this.getAttribute('data-name')] = value;

        console.log(liste_choix);

        if (this.getAttribute('data-name') == 'car') {
            div_vehicule.classList.remove('show');
            div_vehicule.classList.add('hide');
            div_energie.classList.remove('hide');
            div_energie.classList.add('show');
        }
        if (this.getAttribute('data-name') == 'energie') {
            div_energie.classList.remove('show');
            div_energie.classList.add('hide');
            div_kilometrage.classList.remove('hide');
            div_kilometrage.classList.add('show');
        }
        if (this.getAttribute('data-name') == 'kilometrage') {
            div_kilometrage.classList.remove('show');
            div_kilometrage.classList.add('hide');
            div_annee.classList.remove('hide');
            div_annee.classList.add('show');
        }
        if (this.getAttribute('data-name') == 'annee') {
            div_annee.classList.remove('show');
            div_annee.classList.add('hide');
            div_passager.classList.remove('hide');
            div_passager.classList.add('show');
        }
        if (this.getAttribute('data-name') == 'passager') {
            div_passager.classList.remove('show');
            div_passager.classList.add('hide');
            div_resultat.classList.remove('hide');
            div_resultat.classList.add('show');
            input_list_choix.setAttribute('value', JSON.stringify(liste_choix));
            form.submit();
        }

    });
}
