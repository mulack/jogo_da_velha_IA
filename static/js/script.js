let jogador = "X";

function fazerJogada(posicao) {
    fetch('/move', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ jogador, posicao })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("tabuleiro").innerText = data.tabuleiro.join(" ");
        if (data.resultado) alert(`${jogador} venceu!`);
        jogador = jogador === "X" ? "O" : "X";
    });
}
