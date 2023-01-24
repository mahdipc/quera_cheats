<?php

$file = fopen('input.txt', 'r');
$line = fgets($file);

$line = lcfirst( str_replace(' ', '', ucwords(strtolower(trim($line)), ' ')));

echo $line;
?>