let nota1 = parseFloat(prompt("Digite a primeira nota:"));
let nota2 = parseFloat(prompt("Digite a segunda nota:"));

let media = (nota1 + nota2) / 2;
console.log("Média:", media);

if (media >= 7) {
    console.log("Situação: Aprovado");
} else if (media >= 5) {
    console.log("Situação: Recuperação");
} else {
    console.log("Situação: Reprovado");
}
