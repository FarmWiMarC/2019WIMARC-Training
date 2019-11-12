<?php
 

$parent_category = $_GET['TestVar'];
 

 
$dateBegin = $_GET['dateBegin'];
$dateEnd = $_GET['dateEnd'];

//echo $dateBegin.":".$dateEnd;

 if(( $dateBegin ==0 )&&( $dateEnd==0))
{

// $date_begin  = date("Y-m-d"); 
//date('d M Y H:i:s',$strtotime);

$dateBegin=strtotime('today')+$dateoffset;

$dateBegin=strtotime("-3 days ",$t0); 

$dateBegin= date("Y-m-d",$dateBegin);
$dateEnd= date("Y-m-d",$dateEnd);
}


//echo $date_begin.":"$date_end;


 
$filename= 'ReportFrom'.$dateBegin.'To'.$dateEnd;
//echo $filename;

/*

             
//$dateBegin = $_GET['dateBegin'];
//$dateEnd = $_GET['dateEnd'];


//$dateBegin = "2017-11-16";//$_GET['dateBegin'];
//$dateEnd = "2017-11-20";//$_GET['dateEnd'];

*/
$dateBegin=strtotime($dateBegin);
$dateEnd=strtotime($dateEnd);
$conn = mysqli_connect("localhost","root","opastrith","mpibmPV2");
//$conn = mysqli_connect("localhost","root","feedtech","warehouse");   

 ////////////////////////////////////////////////////////////////////////////           

 
 $tablename1 = 'sensor';
 $tablename2 = 'volt';
 $tablename3 = 'a';
 $tablename4 = 'b';
 $tablename5 = 'd';
 //  echo $tablename1;
 $moistureoffset =55;
 $moisturesense=0.02; 
              
         
// $db = mysql_select_db($database,$connection) or die  ("Could not select database.".mysql_error());  
        
                $query1 = "SELECT * FROM $tablename1";
			if(	$result1 = mysqli_query($conn,$query1))
			{
				
			
                //$result1 = mysql_query($query1)or ("Could not query ".mysql_error());  
     
	           $query2 = "SELECT * FROM $tablename2";
				 
               $lasttimetoday=0;$i=0;//$timetoday=1;
               $fileoutput='';
			   $fileoutput =  "date".","."time".","."Temp".","."Humid".","."Rain".","."M30cm".","."M50cm".","."A30cm".","."A50cm".","."B30cm".","."B50cm"."\n";
				
			   $output='';
			   $data1[]=array("date","time","Temp","Humid","Rain","M30cm","M50cm","A30cm","A50cm","B30cm","B50cm");
	
			 			   
			   while($row1 = mysqli_fetch_assoc($result1))
                    {
					              
                    $last_date=$row1['date'];
					
					 $timestampdate = strtotime($row1['date']);
					
					$timestampbegin=$timestampdate;
  if (($timestampbegin >= $dateBegin)&&($timestampbegin <= $dateEnd))
  {	   
                    
					$last_time=$row1['time'];
				//	echo $last_time.":".$last_date;
				//	$fileoutput =  $fileoutput.$row1['date'].",".$row1['time'].",".$row1['A'].",".$row1['B'].",".$row1['C'].",".$row1['D'].",";
				$output1 =   $row1['F'].",".$row1['G'].",";//.$row1[4].",".$row1[5].",";     
              // echo $output1;                
				$row12=$row1['Temp'];
					  $row13=$row1['Humid'];
					   $row14=$row1['Rain'];
					   // $row25=$row2[5];

				 $query2 = "SELECT * FROM $tablename2 WHERE date = '$last_date' AND time = '$last_time'";
                  
				                  
				 if( $result2 = mysqli_query($conn,$query2))
				  {
				   while($row2 = mysqli_fetch_row($result2))
				   {  $output2 =   $row2[2].",".$row2[3].",".$row2[4].",".$row2[5].",";
                   if ($row2[6]>400)
				   {
      			   $row22=$moistureoffset-$moisturesense*$row2[6];
				   }
				   else
					$row22 = '-';   
                   if ($row2[7]>400)
				   {  
					$row23=$moistureoffset-$moisturesense*$row2[7];
				   }
				   else
					$row22 = '-'; 
					 //  $row24=$row2['D'];
					 //   $row25=$row2[5];
				   }
				  }
				  mysqli_free_result($result2);
				//////////////////////////////////////////////////////////////////////  
				 
                 $query3 = "SELECT * FROM $tablename3 WHERE date = '$last_date' AND time = '$last_time'";
                 
				 
				  if( $result3 = mysqli_query($conn,$query3))
				  {
				   while($row3 = mysqli_fetch_row($result3))
				   {  $output3 =   $row3[2].",".$row3[3].",".$row3[4].",".$row3[5].",";
				   // $row32=$row3[2];
				   //	  $row33=$row3[4];
					  // $row34=$row3[4];
					  //  $row35=$row3[5];
					//echo ','.$row3[3].','.$row3[5];  
				   if ($row3[3]>400)
				   {
      			   $row32=$moistureoffset-$moisturesense*$row3[3];
				   }
				   else
					$row32 = '-';   
                   if ($row3[5]>400)
				   {  
					$row33=$moistureoffset-$moisturesense*$row3[5];
				   }
				   else
					$row33 = '-'; 
				   
				   
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
					  $row43=$row4[4];
					   //$row44=$row4[4];
					   // $row45=$row4[5];
					 //  echo ','.$row4[3].','.$row4[5]; 
				    if ($row4[3]>400)
				   {
      			   $row42=$moistureoffset-$moisturesense*$row4[3];
				   }
				   else
					$row42 = '-';   
                   if ($row4[5]>400)
				   {  
					$row43=$moistureoffset-$moisturesense*$row4[5];
				   }
				   else
					$row43 = '-'; 
				   
				   
				   
				   
				   
				   
				   }
				  }
				  mysqli_free_result($result4);
					$row22 = '-';  
				  $row23 = '-';  

				$fileoutput =  $fileoutput.$row1['date'].",".$row1['time'].",".$row12.",".$row13.",".$row14.",".$row22.",".$row23.",".$row32.",".$row33.",".$row42.",".$row43;
				
				//$fileoutput =  $fileoutput.$row1['date'].",".$row1['time'].","." ".","."R2R107".","."R2R151".","."R2H101".","."Outsid WH"."\n";
					
				//$fileoutput =  $fileoutput." ".","." ".","."1".",".$row22.",".$row32.",".$row42.",".$row1['C']."\n";
				//$fileoutput =  $fileoutput." ".","." ".","."2".",".$row23.",".$row33.",".$row43.","." "."\n";
				//$fileoutput =  $fileoutput." ".","." ".","."3".",".$row24.",".$row34.",".$row44.","." "."\n";
				//$fileoutput =  $fileoutput." ".","." ".","."Humidity".",".$row25.",".$row35.",".$row45.",".$row1['D']."\n";
				$data1[]=array(($row1['date']),$row1['time'],($row12),($row13),($row14),($row22),($row23),($row32),($row33),($row42),($row43));
				
                 $fileoutput = $fileoutput."\n"; 
					
               
			
                  }    

	}
				
			}
        //echo $fileoutput;
			echo json_encode($data1);
         // $filename = $filename.".csv";
         //  header('Content-type: application/csv');
         // header('Content-Disposition: attachment; filename='.$filename);

		 
		//	echo $fileoutput;
		//	echo $output;
		//	echo $data1[];
			exit;
   
   


   
 ///////////////////////////////////////////////////////////////////////////////////////////////////////////          
			   

					
					
					
					
            
 
            
 
              
                     ?>       
              
 