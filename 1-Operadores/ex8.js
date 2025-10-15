console.log("== Operadores Relacionais e Lógicos ==");

let x = parseFloat(prompt("Digite o valor de x:"));
let y = parseFloat(prompt("Digite o valor de y:"));
let z = parseFloat(prompt("Digite o valor de z:"));

console.log("x > y and y > z:", x > y && y > z);
console.log("x > y or y > z:", x > y || y > z);
console.log("x == y or x == z:", x == y || x == z);
console.log("x != y and y != z:", x != y && y != z);
console.log("not (x > y) and z > y:", !(x > y) && z > y);
console.log("(x > y and y > z) or (x == z):", (x > y && y > z) || (x == z));
