var modal = document.getElementById("myModal");

// Obtém o <span> que fecha o modal
var span = document.getElementsByClassName("close")[0];

// Obtém todos os itens da lista
var ulItems = document.querySelectorAll("#categorias_list li div");

// Função para exibir o modal e buscar checklist
function handleItemClick(event) {
    var idTopico = this.querySelector("#id_topico").innerText;
    document.getElementById("idsetor").value = idTopico;

    console.log("ID do usuário:", idUsuario);

    // Configurar a requisição AJAX
    var settings = {
        url: `http://127.0.0.1:5000/checklist/${idTopico}?id_usuario=${idUsuario}`,
        method: "GET",
        timeout: 0,
    };

    // Fazer a requisição AJAX
    $.ajax(settings).done(function (response) {
        console.log(response);
        if (response.checklist) {
            var checklistContainer = document.getElementById("checklist");
            checklistContainer.innerHTML = '';
            response.checklist.forEach(function (item) {
                var li = document.createElement("li");
                li.innerText = item;
                checklistContainer.appendChild(li);
            });
        } else {
            console.log("Nenhum checklist encontrado.");
        }
    }).fail(function (error) {
        console.log("Erro ao buscar checklist:", error);
    });

    // Exibir o modal
    modal.style.display = "block";
}

// Adiciona evento de clique para cada item da lista
ulItems.forEach(function (item) {
    item.addEventListener("click", handleItemClick);
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