<?php
echo "Digite a primeira nota: ";
$nota1 = (float)trim(fgets(STDIN));

echo "Digite a segunda nota: ";
$nota2 = (float)trim(fgets(STDIN));

$media = ($nota1 + $nota2) / 2;
echo "Média: $media\n";

if ($media >= 7) {
    echo "Situação: Aprovado\n";
} elseif ($media >= 5) {
    echo "Situação: Recuperação\n";
} else {
    echo "Situação: Reprovado\n";
}
?>
