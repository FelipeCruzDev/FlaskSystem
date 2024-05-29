// Obtém a lista de itens
var ulItems = document.querySelectorAll("#departamentos");

// Adiciona evento de clique para cada item da lista
ulItems.forEach(function (item) {
    item.addEventListener("click", function () {
        // Obtém o nome do setor
        var setor = this.innerText.trim();

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
    });
});
