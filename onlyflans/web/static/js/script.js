//modal
document.addEventListener("DOMContentLoaded", function() {
    var modalElement = document.getElementById('exampleModalCenter');
    var modal = new bootstrap.Modal(modalElement);

    var hasMoved = false;

    function openModal() {
        modal.show();
    }

    document.body.onmousemove = function() {
        if (!hasMoved) {
            hasMoved = true;
            openModal();
        }
    }
});




//cards

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.card').forEach(function(card, index) {
        card.addEventListener('click', function() {
            var cardText = this.querySelector('.card-text');
            var cardButton = this.querySelector(`#btn-card-${index + 1}`);
            var isHidden = cardText.style.display === 'none' || cardText.style.display === '';

            // Ocultar los textos y botones y eliminar la clase expanded de todas las tarjetas
            document.querySelectorAll('.card-text').forEach(function(text) {
                text.style.display = 'none';
            });
            document.querySelectorAll('button[id^="btn-card"]').forEach(function(button) {
                button.style.display = 'none';
            });
            document.querySelectorAll('.card').forEach(function(c) {
                c.classList.remove('expanded');
            });

            // Si el texto está oculto, mostramos el texto y el botón y expandimos la tarjeta
            if (isHidden) {
                cardText.style.display = 'block';
                cardButton.style.display = 'block';
                this.classList.add('expanded');
            }
        });
    });
});







