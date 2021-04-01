<?php
if (isset($_GET['run'])){
$V = $_GET['run'];
$E = shell_exec("python main.py -load " . $V);
echo $E;
}else {
echo "put the launching point"

}
?>
