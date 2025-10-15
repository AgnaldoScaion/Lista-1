<?php
$pares = 0;
$impares = 0;
$soma = 0;

for ($i = 1; $i <= 10; $i++) {
    echo "Digite o {$i}º número: ";
    $num = (int)trim(fgets(STDIN));
    $soma += $num;
    if ($num % 2 == 0) {
        $pares++;
    } else {
        $impares++;
    }
}

echo "Pares: $pares\n";
echo "Ímpares: $impares\n";
echo "Soma total: $soma\n";
?>
