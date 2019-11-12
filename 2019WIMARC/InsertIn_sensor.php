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
                	$A=$_POST['Temp'];
                        $B=$_POST['Humid'];
                        $C=$_POST['Rain'];
                        $D=$_POST['WindD'];
                        $E=$_POST['WindS'];
                        $F=$_POST['Lux'];
                        $G=$_POST['M1'];
                        $H=$_POST['M2'];
       // echo "result is $date $time $A $B $C $D"; 
   include "dblink.php";
 
   $sql = "Insert into sensor (date,time,Temp,Humid,Rain,WindD,WindS,Lux,M1,M2) values ('$date', '$time', '$A','$B', '$C', '$D', '$E','$F', '$G', '$H');";
   
if ($conn->query($sql) === TRUE) {
echo "New record created successfully";
} else {
echo "Error: " . $sql . "<br>" . $conn->error;
}$conn->close();

      echo " POST in database ";// POST request received
      break;
  }
?>