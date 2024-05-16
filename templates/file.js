// JavaScript/jQuery para exibir o modal de erro
        function showErrorModal(message) {
            var modal = document.getElementById("error-modal");
            var errorMessage = document.getElementById("error-message");
            errorMessage.textContent = message;
            modal.style.display = "block";
        }

        // Fechar o modal quando o usuário clicar no botão de fechar
        document.getElementsByClassName("close")[0].onclick = function() {
            var modal = document.getElementById("error-modal");
            modal.style.display = "none";
        }