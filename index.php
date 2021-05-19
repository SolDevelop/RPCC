<?php
if (isset($_GET['run'])){
	if (strtoupper(substr(PHP_OS, 0, 3)) === 'WIN'){
		$V = $_GET['run'];
	    $E = shell_exec("python main.py -load " . $V);
		echo $E;
    }else{
		$V = $_GET['run'];
	    $E = shell_exec("python3 main.py -load " . $V);
		echo $E;
	}
}elseif (isset($_GET['command'])){
       if (strtoupper(substr(PHP_OS, 0, 3)) === 'LINUX'){
       echo "you cannot use command because linux is already commands, use run";
       }else{
	   $C = $_GET['command'];
	   $E = shell_exec("python main.py -load command" . $C);
	   $E;
	   echo "Done";
	   }

}elseif (isset($_GET['screenshot'])){
if (strtoupper(substr(PHP_OS, 0, 3)) === 'WIN'){
$E = shell_exec("python main.py -load sc");
if ($E == "SCNT"){
echo "Screenshots are Not Allowed In Your PC";
}else{
$file = $E;
echo "<img src=\"$file\"/>";
}}else{
echo "Your OS Dont Support That Yet";
}
}
?>