function toggleMenu() {
    var menu = document.getElementById("menu");
    menu.classList.toggle("show");
    if (document.body.style.overflow == "hidden") {
      document.body.style.overflow = "";
    } else {
      document.body.style.overflow = "hidden";
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    const openBtn = document.querySelectorAll(".open-btn");
    let expandedContainer = null;
    let expandedDesc = null;
    let expandedNombre = null;
    let expandedButton = null;

    openBtn.forEach((button) => {
      // Al hacer clic en un cuadrado
      button.addEventListener("click", function () {
        const container_servicio = this.nextElementSibling;
        // Si ya hay un cuadrado expandido y no es el mismo que el actual
        const desc_servicio = this.previousElementSibling;
        const nombre_servicio = desc_servicio.previousElementSibling;
        const button_servicio = button;
        if (expandedContainer && expandedContainer !== container_servicio) {
          expandedContainer.classList.remove("expanded_div");
          expandedDesc.classList.remove("expanded_desc");
          expandedNombre.classList.remove("expanded_nombre");
          expandedButton.classList.remove("expanded_button");
        }

        // Verificar si el cuadrado ya está expandido
        if (container_servicio.classList.contains("expanded_div")) {
          container_servicio.classList.remove("expanded_div"); // Contraer si ya está abierto
          desc_servicio.classList.remove("expanded_desc");
          nombre_servicio.classList.remove("expanded_nombre");
          button_servicio.classList.remove("expanded_button");
          expandedContainer = null;
          setTimeout(function () {
            expandedNombre = null;
            expandedDesc = null;
            expandedButton = null;
          }, 900);
        } else {
          container_servicio.classList.add("expanded_div"); // Expandir si está cerrado
          desc_servicio.classList.add("expanded_desc");
          nombre_servicio.classList.add("expanded_nombre");
          button_servicio.classList.add("expanded_button");
          expandedContainer = container_servicio;
          expandedDesc = desc_servicio;
          expandedNombre = nombre_servicio;
          expandedButton = button_servicio;
        }
      });

      // Cerrar el cuadrado cuando se hace clic en el botón "Close"
      const desc_servicio = button.previousElementSibling;
      const container_servicio = button.nextElementSibling;
      const nombre_servicio = desc_servicio.previousElementSibling;
      const closeBtn = container_servicio.querySelector(".close-btn");
      const button_servicio = button;

      closeBtn.addEventListener("click", function (event) {
        event.stopPropagation(); // Evitar que el clic en el botón cierre inmediatamente después el cuadrado
        setTimeout(function () {
          desc_servicio.classList.remove("expanded_desc");
          button_servicio.classList.remove("expanded_button");
        }, 900);
        nombre_servicio.classList.remove("expanded_nombre");
        container_servicio.classList.remove("expanded_div");
        expandedServicio = null;
        expandedNombre = null;
        expandedDesc = null;
        expandedButton = null; 
        expandedContainer = null;
      });
    });
  });
const textContainer = document.getElementById('textContainer');
const highlightTexts = [
  document.getElementById('highlightText1'),
  document.getElementById('highlightText2'),
  document.getElementById('highlightText3'),
];

let currentIndex = 0;
const totalTexts = highlightTexts.length;

// Función para ajustar la altura del contenedor basado en la frase actual
function adjustHeight(index) {
  let currentHeight = highlightTexts[index].offsetHeight;
  textContainer.style.height = currentHeight + 'px';
}

// Ajustar la altura al cargar la página
adjustHeight(currentIndex);

// Llamar a la función cada vez que cambia la frase
setInterval(() => {
  currentIndex = (currentIndex + 1) % totalTexts; // Mover al siguiente texto
  adjustHeight(currentIndex);
}, 4332); // AJUSTA ESTE VALOR: Sincronizado con la animación 