<?php
if (isset($_GET['run'])){
$V = $_GET['run'];
if (strtoupper(substr(PHP_OS, 0, 3)) === 'WIN'){
$E = shell_exec("python main.py -load " . $V);
echo $E;
}else {
$E = shell_exec("python3 main.py -load " . $V);
echo $E;
}
}
?>