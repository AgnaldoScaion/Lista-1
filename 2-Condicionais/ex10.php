<?php
echo "Usuário: ";
$usuario = trim(fgets(STDIN));

echo "Senha: ";
$senha = trim(fgets(STDIN));

if ($usuario == "admin" && $senha == "1234") {
    echo "Acesso permitido!\n";
} else {
    echo "Acesso negado!\n";
}
?>
