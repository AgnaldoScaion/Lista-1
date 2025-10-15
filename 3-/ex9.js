let pares = 0;
let impares = 0;
let soma = 0;

for (let i = 1; i <= 10; i++) {
    let num = parseInt(prompt(`Digite o ${i}º número:`));
    soma += num;
    if (num % 2 === 0) {
        pares++;
    } else {
        impares++;
    }
}

console.log("Pares:", pares);
console.log("Ímpares:", impares);
console.log("Soma total:", soma);
