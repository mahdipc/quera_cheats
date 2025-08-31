<?php

function estimateReadingTime(string $text): int
{
    $clean = str_replace(['.', '?', '!', ',', ';', ':'], ' ', $text);
    $clean = trim($clean);
    if ($clean === '') {
        return 0;
    }

    $words = preg_split('/[ \t\n]+/u', $clean, -1, PREG_SPLIT_NO_EMPTY);
    $count = count($words);

    return (int) ceil($count / 200);
}
?>