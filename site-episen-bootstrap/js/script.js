
document.addEventListener('DOMContentLoaded', function() {
    console.log("Le script EPISEN est bien chargé !");

    const contactForm = document.querySelector('form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(event) {

            alert("Merci ! Votre message a bien été envoyé à l'administration de l'EPISEN.");
        });
    }
});
