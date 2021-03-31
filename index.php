<?php
$V = $_GET['run'];
$E = shell_exec("python main.py -load " . $V);
echo $E;
?>