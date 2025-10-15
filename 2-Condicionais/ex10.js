let usuario = prompt("Usuário: ");
let senha = prompt("Senha: ");

if (usuario === "admin" && senha === "1234") {
    console.log("Acesso permitido!");
} else {
    console.log("Acesso negado!");
}
