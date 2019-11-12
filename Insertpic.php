<?php
   // $received; = file_get_contents('http://203.150.37.159/opashome/Insertpic.php');
    date_default_timezone_set("Asia/Bangkok");
	$received = file_get_contents("php://input");
	$fileToWrite = "upload - ".time().".jpg";
    //echo $received;
     
	 file_put_contents($fileToWrite, $received);
	 
	$fn = 'opashome2.jpg';
	
	 if(unlink($fn))
	 {
      echo sprintf("The file %s deleted successfully",$fileToWrite);	 
	 }
	$currentTime= date('H', time()); 
	echo $currentTime;
	
	$fn = 'opashomeH'.$currentTime.'.jpg';
	
	$fn = 'opashomeCAM.jpg';
	copy($fileToWrite, $fn);
	 if(unlink($fileToWrite))
	 {
      echo sprintf("The file %s deleted successfully",$fileToWrite);	 
	 }
	 
	 $mod_time=date("H", filemtime($fn));
	 
	$fx='wimarcH'.$mod_time.'.jpg'; 
	copy($fn, $fx); 
	 
	//$fileToWrite='/var/www/html/LORAx/test.jpg';
	
  // copy($fn, $fileToWrite);
	//sleep(3);
	  
//	  $fh = fopen( $fn, 'w' );
//fclose($fh);
	//file_put_contents($fileToWrite, $received);
	//echo $homepage;
//	$fn = 'opashome2.jpg';
/*
use CV\CascadeClassifier, CV\Scalar, CV\Point;
use function CV\{imread, imwrite, cvtColor, equalizeHist, rectangleByRect};
use const CV\{COLOR_BGR2GRAY};
//$filename = $fileToWrite;


$src = imread($fn);

//$src = imread("/var/www/html/".$fn);

echo 'opasclass.jpg';

// face by lbpcascade_frontalface
date_default_timezone_set("Asia/Bangkok"); 
$text = $filename;
$time =strtotime('now');
$date= strval(date('d-m-Y', $time));
$time= strval(date('H:i', $time));

 $timestamp=$date.' '.$time;
echo $timestamp;

 \CV\rectangle($src, 0, 450, 640, 480, new Scalar(255,255,255), -2);
    \CV\putText($src, "$text", new Point(2, 472), 0, 1, new Scalar(), 2);
    \CV\putText($src, "$timestamp", new Point(300, 472), 0, 1, new Scalar(), 2); 

	
imwrite("/var/www/html/".$fn, $src);   

*/	 	
	
	?>
