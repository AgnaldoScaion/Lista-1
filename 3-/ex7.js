let quant = parseInt(prompt("Quantas notas você vai informar?"));
let soma = 0;

for (let i = 1; i <= quant; i++) {
    let nota = parseFloat(prompt("Digite a nota " + i + ":"));
    soma += nota;
}

let media = soma / quant;
console.log("Média:", media);

if (media >= 7) {
    console.log("Situação: Aprovado");
} else if (media >= 5) {
    console.log("Situação: Recuperação");
} else {
    console.log("Situação: Reprovado");
}
