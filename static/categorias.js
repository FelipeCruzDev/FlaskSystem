console.log("O script categorias.js está sendo executado.");
function getCategorias(categorias) {
    // Limpa a lista de categorias
    var categoriasList = document.getElementById("categorias_list");
    categoriasList.innerHTML = "";

    // Cria e adiciona as categorias à lista
    categorias.forEach(function(categoria) {
        var li = document.createElement("li");  // Cria um elemento <li>
        li.textContent = categoria;             // Define o texto do elemento <li>
        categoriasList.appendChild(li);         // Adiciona o elemento <li> à lista
    });

    // Adiciona um console.log para verificar se a função foi chamada e se recebeu a lista de categorias corretamente
    console.log("getCategorias chamada com as seguintes categorias:", categorias);
}
// Obtém o modal
var modal = document.getElementById("myModal");

// Obtém o <span> que fecha o modal
var span = document.getElementsByClassName("close")[0];

// Obtém todos os itens da lista
var ulItems = document.querySelectorAll("#topicos");
function enviarSetorParaTopicos() {
    var setor = document.getElementById("cklist").value;
    // Cria um objeto FormData e adiciona o setor como um parâmetro
    var formData = new FormData();
    formData.append('setor', setor);


// Adiciona evento de clique para cada item da lista
ulItems.forEach(function (item) {
   item.addEventListener("click", function () {
      // Define o nome do setor no modal

    var setor = document.getElementById("cklist").value = this.innerText.trim();
    // Cria um objeto FormData e adiciona o setor como um parâmetro
    var formData = new FormData();
    formData.append('cklist', setor);

    // Faz uma requisição AJAX usando fetch
    fetch('/topicos', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        // Verifica se a requisição foi bem sucedida
        if (!response.ok) {
            throw new Error('Erro ao enviar dados do setor para /topicos');
        }
        // Se tudo estiver certo, exibe uma mensagem de sucesso
        console.log('Dados do setor enviados com sucesso para /topicos');
    })
    .catch(error => {
        console.error('Erro:', error);
    });
      // Exibe o modal
      modal.style.display = "block";
   });
});
function enviarSetorParaTopicos() {
    var setor = document.getElementById("setor").value;
    // Cria um objeto FormData e adiciona o setor como um parâmetro
    var formData = new FormData();
    formData.append('setor', setor);

    // Faz uma requisição AJAX usando fetch
    fetch('/topicos', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        // Verifica se a requisição foi bem sucedida
        if (!response.ok) {
            throw new Error('Erro ao enviar dados do setor para /topicos');
        }
        // Se tudo estiver certo, exibe uma mensagem de sucesso
        console.log('Dados do setor enviados com sucesso para /topicos');
    })
    .catch(error => {
        console.error('Erro:', error);
    });
}

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
