// script.js
const textElement = document.querySelector('.color-changing-text');
const button = document.getElementById('toggleButton');

// Alternar la clase que cambia la posición del gradiente
button.addEventListener('click', () => {
    textElement.classList.toggle('active'); // Alterna entre azul y rojo
});
