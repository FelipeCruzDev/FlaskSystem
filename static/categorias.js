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
