// Selecciona todos los elementos con la clase 'box'
const boxes = document.querySelectorAll('.box');

// Función para verificar si un elemento está visible en la ventana
const isElementInViewport = (el) => {
  const rect = el.getBoundingClientRect();
  return (
    rect.top <= window.innerHeight && // Parte superior visible
    rect.bottom >= 0 // Parte inferior visible
  );
};

// Función que activa las animaciones
const handleScroll = () => {
  boxes.forEach(box => {
    if (isElementInViewport(box)) {
      box.classList.add('in-view'); // Agrega la clase para animar
    }
  });
};

// Escuchar los eventos de scroll y carga
window.addEventListener('scroll', handleScroll);
window.addEventListener('load', handleScroll);
