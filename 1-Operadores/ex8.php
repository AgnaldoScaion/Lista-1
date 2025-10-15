<?php
echo "== Operadores Relacionais e Lógicos ==\n";

echo "Digite o valor de x: ";
$x = (float)trim(fgets(STDIN));

echo "Digite o valor de y: ";
$y = (float)trim(fgets(STDIN));

echo "Digite o valor de z: ";
$z = (float)trim(fgets(STDIN));

echo "x > y and y > z: " . (($x > $y) && ($y > $z) ? "True" : "False") . "\n";
echo "x > y or y > z: " . (($x > $y) || ($y > $z) ? "True" : "False") . "\n";
echo "x == y or x == z: " . (($x == $y) || ($x == $z) ? "True" : "False") . "\n";
echo "x != y and y != z: " . (($x != $y) && ($y != $z) ? "True" : "False") . "\n";
echo "not (x > y) and z > y: " . ((!($x > $y)) && ($z > $y) ? "True" : "False") . "\n";
echo "(x > y and y > z) or (x == z): " . ((($x > $y) && ($y > $z)) || ($x == $z) ? "True" : "False") . "\n";
?>
