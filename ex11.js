console.log("== Operadores Aritméticos ==");

let num1 = parseFloat(prompt("Digite o primeiro número:"));
let num2 = parseFloat(prompt("Digite o segundo número:"));

let soma = num1 + num2;
let subtracao = num1 - num2;
let multiplicacao = num1 * num2;
let divisao = num2 !== 0 ? num1 / num2 : "Indefinida (divisão por zero)";
let resto = num2 !== 0 ? num1 % num2 : "Indefinido (divisão por zero)";
let potencia = num1 ** num2;

console.log("A soma dos números foi:", soma);
console.log("A subtração do primeiro pelo segundo é:", subtracao);
console.log("A multiplicação dos números é:", multiplicacao);
console.log("A divisão do primeiro pelo segundo é:", divisao);
console.log("O resto da divisão do primeiro pelo segundo é:", resto);
console.log(num1 + " elevado a " + num2 + " é:", potencia);
