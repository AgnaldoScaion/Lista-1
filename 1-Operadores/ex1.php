<?php
echo "== Operadores Aritméticos ==\n";

echo "Digite o primeiro número: ";
$num1 = trim(fgets(STDIN));

echo "Digite o segundo número: ";
$num2 = trim(fgets(STDIN));

$num1 = (float)$num1;
$num2 = (float)$num2;

$soma = $num1 + $num2;
$subtracao = $num1 - $num2;
$multiplicacao = $num1 * $num2;
$divisao = ($num2 != 0) ? $num1 / $num2 : "Indefinida (divisão por zero)";
$resto = ($num2 != 0) ? $num1 % $num2 : "Indefinido (divisão por zero)";
$potencia = $num1 ** $num2;

echo "A soma dos números foi: $soma\n";
echo "A subtração do primeiro pelo segundo é: $subtracao\n";
echo "A multiplicação dos números é: $multiplicacao\n";
echo "A divisão do primeiro pelo segundo é: $divisao\n";
echo "O resto da divisão do primeiro pelo segundo é: $resto\n";
echo "$num1 elevado a $num2 é: $potencia\n";
?>
