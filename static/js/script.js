// static/js/script.js

document.addEventListener("DOMContentLoaded", function() {
    const celulas = document.querySelectorAll(".celula");
    const mensagem = document.getElementById("mensagem");
    const reiniciarBtn = document.getElementById("reiniciar");

    celulas.forEach(celula => {
        celula.addEventListener("click", async () => {
            const posicao = celula.dataset.pos;
            const response = await fetch("/jogada", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ posicao, jogador: "X" })
            });
            const data = await response.json();

            // Atualizar o tabuleiro
            atualizarTabuleiro(data.tabuleiro);
            if (data.resultado) mensagem.innerText = `Resultado: ${data.resultado}`;
        });
    });

    reiniciarBtn.addEventListener("click", async () => {
        await fetch("/reiniciar", { method: "POST" });
        mensagem.innerText = "";
        atualizarTabuleiro(["1", "2", "3", "4", "5", "6", "7", "8", "9"]);
    });

    function atualizarTabuleiro(tabuleiro) {
        celulas.forEach((celula, index) => {
            celula.innerText = tabuleiro[index] === "X" || tabuleiro[index] === "O" ? tabuleiro[index] : "";
        });
    }
});
