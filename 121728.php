<?php
function sayHello(array $words, int $reverseIndex): void
{
     $words[$reverseIndex]= strrev($words[$reverseIndex]);
     echo implode(" ", $words);
     echo "\n";
}