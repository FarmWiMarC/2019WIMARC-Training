<?php
   // $received; = file_get_contents('http://203.150.37.159/opashome/Insertpic.php');
    date_default_timezone_set("Asia/Bangkok");
	$received = file_get_contents("php://input");
	$fileToWrite = "upload - ".time().".jpg";
    //echo $received;
     
	 file_put_contents($fileToWrite, $received);
	 
	$fn = 'wimarc.jpg';
	 unlink($fn);
	 
	
	
	copy($fileToWrite, $fn);
	
	 unlink($fileToWrite);
	 
	 echo sprintf("The file %s uploaded successfully",$fn); 

	?>
