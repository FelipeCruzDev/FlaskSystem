function getCategorias() {
    // Simulação de categorias associadas ao usuário logado
    var categorias = ['Categoria 1', 'Categoria 2', 'Categoria 3'];

    // Limpa a lista de categorias
    var categoriasList = document.getElementById("categorias_list");
    categoriasList.innerHTML = "";

    // Adiciona as categorias à lista
    categorias.forEach(function(categoria) {
        var li = document.createElement("li");
        li.textContent = categoria;
        categoriasList.appendChild(li);
    });
}

