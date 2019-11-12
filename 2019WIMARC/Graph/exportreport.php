<?php
 
//$connection=mysql_connect("localhost", "791677", "opastrith");
//$connection=mysql_connect("localhost", "root", "1234"); 
 //$database = "GHbangyai";
//  $database = "warehouse";
 //$result = mysql_list_tables($database);
//echo $database;                

$conn = mysqli_connect("localhost","791677","opastrith","warehouse");
   

 ////////////////////////////////////////////////////////////////////////////           

 $tablename1 = 'temp';
 $tablename2 = 'a';
 $tablename3 = 'b';
 $tablename4 = 'c';
 $tablename5 = 'd';
 //  echo $tablename1;
             
              
         
// $db = mysql_select_db($database,$connection) or die  ("Could not select database.".mysql_error());  
        
                $query1 = "SELECT * FROM $tablename1";
			if(	$result1 = mysqli_query($conn,$query1))
			{
				
			
                //$result1 = mysql_query($query1)or ("Could not query ".mysql_error());  
     
	           $query2 = "SELECT * FROM $tablename2";
				 
               $lasttimetoday=0;$i=0;//$timetoday=1;
               $fileoutput='';
			   $output='';
			   
	
			 			   
			   while($row1 = mysqli_fetch_assoc($result1))
                    {
					              
                    $last_date=$row1['date'];
                    
					$last_time=$row1['time'];
				//	echo $last_time.":".$last_date;
				//	$fileoutput =  $fileoutput.$row1['date'].",".$row1['time'].",".$row1['A'].",".$row1['B'].",".$row1['C'].",".$row1['D'].",";
				     
                  $query2 = "SELECT * FROM $tablename2 WHERE date = '$last_date' AND time = '$last_time'";
                  
				                  
				 if( $result2 = mysqli_query($conn,$query2))
				  {
				   while($row2 = mysqli_fetch_row($result2))
				   {  $output2 =   $row2[2].",".$row2[3].",".$row2[4].",".$row2[5].",";
				     $row22=$row2[2];
					  $row23=$row2[3];
					   $row24=$row2[4];
					    $row25=$row2[5];
				   }
				  }
				  mysqli_free_result($result2);
				//////////////////////////////////////////////////////////////////////  
				 
                 $query3 = "SELECT * FROM $tablename3 WHERE date = '$last_date' AND time = '$last_time'";
                 
				 
				  if( $result3 = mysqli_query($conn,$query3))
				  {
				   while($row3 = mysqli_fetch_row($result3))
				   {  $output3 =   $row3[2].",".$row3[3].",".$row3[4].",".$row3[5].",";
				    $row32=$row3[2];
					  $row33=$row3[3];
					   $row34=$row3[4];
					    $row35=$row3[5];
				   }
				  }
				  mysqli_free_result($result3);
				
                //////////////////////////////////////////////////////////////////////  
				 
                 $query4 = "SELECT * FROM $tablename4 WHERE date = '$last_date' AND time = '$last_time'";
                 
				 
				  if( $result4 = mysqli_query($conn,$query4))
				  {
				   while($row4 = mysqli_fetch_row($result4))
				   {  $output4 =   $row4[2].",".$row4[3].",".$row4[4].",".$row4[5].",";
				    $row42=$row4[2];
					  $row43=$row4[3];
					   $row44=$row4[4];
					    $row45=$row4[5];
				   }
				  }
				  mysqli_free_result($result4);


				
				
				$fileoutput =  $fileoutput.$row1['date'].",".$row1['time'].","." ".","."A".","."B".","."C".","."Outsid WH"."\n";
					
				$fileoutput =  $fileoutput." ".","." ".","."1".",".$row22.",".$row32.",".$row42.",".$row1['C']."\n";
				$fileoutput =  $fileoutput." ".","." ".","."2".",".$row23.",".$row33.",".$row43.","." "."\n";
				$fileoutput =  $fileoutput." ".","." ".","."3".",".$row24.",".$row34.",".$row44.","." "."\n";
				$fileoutput =  $fileoutput." ".","." ".","."Humidity".",".$row25.",".$row35.",".$row45.",".$row1['D']."\n";
				
				
                 $fileoutput = $fileoutput."\n"; 
					
               
			
                  }    

					      //   }
				
			}
//echo $fileoutput;
			
          $filename = $tablename1.".csv";
           header('Content-type: application/csv');
          header('Content-Disposition: attachment; filename='.$filename);

			echo $fileoutput;
		//	echo $output;
		//	echo $data1[];
			exit;
   
   


   
 ///////////////////////////////////////////////////////////////////////////////////////////////////////////          
			   

					
					
					
					
            
 
            
 
              
                     ?>       
              
 