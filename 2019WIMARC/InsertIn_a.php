<?php
        
        
     header('Content-type: text/html');
    header('Access-Control-Allow-Origin: *');
    // $uri = 'http'. ($_SERVER['HTTPS'] ? 's' : null) .'://'. $_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI'];
   // echo('<p>This information has come from <a href="' . $uri . '">' . $uri . '</a></p>');
$uri = 'http'. (isset($_SERVER['HTTPS']) ? 's' : null) .'://'. $_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI'];  
        
        
  $request_method = $_SERVER['REQUEST_METHOD'];
 
  switch($request_method) {
    case 'PUT':
    case 'DELETE':
      // Ignore the PUT and DELETE request =P
      return;
    case 'GET':
       echo "aacc";// GET request received
      break;
    case 'POST':
     	$date=$_POST['date'];
        	$time=$_POST['time'];
                	$A=$_POST['A'];
                        $B=$_POST['B'];
                        $C=$_POST['C'];
                        $D=$_POST['D'];
                         $E=$_POST['E'];
                        $F=$_POST['F'];
                        $G=$_POST['G'];
                        $H=$_POST['H'];
        echo "result is $date $time $A $B $C $D"; 
    
include "dblink.php";
$sql = "Insert into a (date,time,A,B,C,D,E,F,G,H) values ('$date', '$time', '$A','$B', '$C', '$D', '$E','$F', '$G', '$H');";
   
if ($conn->query($sql) === TRUE) {
echo "New record created successfully";
} else {
echo "Error: " . $sql . "<br>" . $conn->error;
}$conn->close();

/*
   

	$result = mysql_query($sql);
	$sql = "Insert into a values('$date', '$time', '$A','$B', '$C', '$D', '$E','$F', '$G', '$H');";
       
	$result = mysql_query($sql);
	if ($result)
	{
		echo"OK";

mysql_close($link);
	}
	else
	{
		
echo "ERROR";
}
 */       
        
      echo " POST in database ";// POST request received
      break;
  }
?>