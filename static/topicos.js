var modal = document.getElementById("myModal");

// Obtém o <span> que fecha o modal
var span = document.getElementsByClassName("close")[0];

// Obtém todos os itens da lista
var ulItems = document.querySelectorAll("#topicos");

// Adiciona evento de clique para cada item da lista
ulItems.forEach(function (item) {
   item.addEventListener("click", function () {
      // Define o nome do setor no modal
      document.getElementById("setor").value = this.innerText.trim();
      // Exibe o modal
      modal.style.display = "block";
   });
});

// Quando o usuário clicar no <span> (x), fecha o modal
span.onclick = function () {
   modal.style.display = "none";
};

// Quando o usuário clicar em qualquer lugar fora do modal, fecha o modal
window.onclick = function (event) {
   if (event.target == modal) {
      modal.style.display = "none";
   }
};
