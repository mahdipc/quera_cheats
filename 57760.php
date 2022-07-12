<?php
$str =  readline();
$values= (explode("/",$str));



if ($values[1]>6) {
	print_r ((12-$values[1])*30+(30-$values[2]));
}
else{
	print_r ((6-$values[1])*31+6*30+(31-$values[2]));
}
?> 