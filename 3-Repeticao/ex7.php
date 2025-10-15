<?php
echo "Quantas notas você vai informar? ";
$quant = (int)trim(fgets(STDIN));
$soma = 0;

for ($i = 1; $i <= $quant; $i++) {
    echo "Digite a nota $i: ";
    $nota = (float)trim(fgets(STDIN));
    $soma += $nota;
}

$media = $soma / $quant;
echo "Média: $media\n";

if ($media >= 7) {
    echo "Situação: Aprovado\n";
} elseif ($media >= 5) {
    echo "Situação: Recuperação\n";
} else {
    echo "Situação: Reprovado\n";
}
?>
