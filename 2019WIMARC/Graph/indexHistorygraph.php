


<?php

 

 
   $conn = mysqli_connect("localhost", "id2125007_sensor", "opas4870","id2125007_sensor");
 $MoisSense=0.02;
 $MoisOffset=55;
 $TempSense=10;
 $TempOffset=500;
 $t0=strtotime('today');
   
   $graph_dateBegin = strtotime("-7 days ",$t0); 
  // $st1 = strftime("%Y-%m-%d",$st0); //เพิ่มเวลา 1 วันตามอายุอ้อย และย้อนหลังไป 1 ปี
	//echo $st1;
 $graph_dateBegin= $graph_dateBegin*1000-18000000;


 if ((isset($_POST['loadTemp']))||(isset($_POST['loadHum']))||
         (isset($_POST['loadRain']))||(isset($_POST['loadWindspeed']))||(isset($_POST['loadPressure']))
          ||(isset($_POST['loadLevel']))
          ||(isset($_POST['loadLux']))
		   ||(isset($_POST['loadMoisture'])) ||(isset($_POST['loadDust']))
         ) 
              {   
             
 	

	 
	 
	 
	 
$date_begin = $_POST['begindate'];  //echo  $date_begin;
     
   $date_end = $_POST['enddate'];  // echo $date_end;
	 
	 
	// echo 
              
           $timeBegin = strtotime($date_begin);
                    
           $timeEnd = strtotime($date_end);       
    
      $dateoffset =10*60*60;         
     
if((isset($_POST['loadMoisture'])))
 {
$date_begin = $_POST['begindate'];  //echo  $date_begin;
     
$date_end = $_POST['enddate'];  // echo $date_end;
$dateoffset =10*60*60;  


//$timeEnd=strtotime('today')+$dateoffset;

//$timeBegin=strtotime("-3 days ",$t0); 

//$date_begin= date("Y-m-d",$timeBegin);
//$date_end= date("Y-m-d",$timeEnd);   
 }

 

 
 if((isset($_POST['loadTemp'])))
 {
//$date_begin = $_POST['begindate'];  //echo  $date_begin;
     
 //  $date_end = $_POST['enddate'];  // echo $date_end;
$dateoffset =10*60*60;  
$timeEnd=strtotime('today')+$dateoffset;

$timeBegin=strtotime("-3 days ",$t0); 

$date_begin= date("Y-m-d",$timeBegin);
$date_end= date("Y-m-d",$timeEnd);   
 }

 if((isset($_POST['loadHum'])))
 {
//$date_begin = $_POST['begindate'];  //echo  $date_begin;
     
 //  $date_end = $_POST['enddate'];  // echo $date_end;
$dateoffset =10*60*60;  
$timeEnd=strtotime('today')+$dateoffset;

$timeBegin=strtotime("-7 days ",$t0); 

$date_begin= date("Y-m-d",$timeBegin);
$date_end= date("Y-m-d",$timeEnd);   
 }
if((isset($_POST['loadRain'])))
 {
//$date_begin = $_POST['begindate'];  //echo  $date_begin;
     
 //  $date_end = $_POST['enddate'];  // echo $date_end;
$dateoffset =10*60*60;  
$timeEnd=strtotime('today')+$dateoffset;

$timeBegin=strtotime("-15 days ",$t0); 

$date_begin= date("Y-m-d",$timeBegin);
$date_end= date("Y-m-d",$timeEnd);   
 }
if((isset($_POST['loadLux'])))
 {
//$date_begin = $_POST['begindate'];  //echo  $date_begin;
     
 //  $date_end = $_POST['enddate'];  // echo $date_end;
$dateoffset =10*60*60;  
$timeEnd=strtotime('today')+$dateoffset;

$timeBegin=strtotime("-30 days ",$t0); 

$date_begin= date("Y-m-d",$timeBegin);
$date_end= date("Y-m-d",$timeEnd);   
 }


 

///////////////////////////////////////////////////////////////

$tablename = 'sensor'; 
 $legend1="Temperature";
 $legend2="Humidity";
$legend3="Rain";
$legend4="Lux";
$legend5="";
$legend6="";
$legend7="";
$legend8="";
$data1=null;
$data2=null;
  $data3=null;
  $data4=null;
  $data5=null;
  $data6=null;
  $data7=null;
  $data8=null; 
 $data9=null;
$data10=null;
  $data11=null;
  $data12=null;
  $data13=null;
  $data14=null;
  $data15=null;
  $data16=null; 
 
 
 
 
     $t0=strtotime('today');
   
   $graph_dateBegin = strtotime("-3 days ",$t0); 
  // $st1 = strftime("%Y-%m-%d",$st0); //เพิ่มเวลา 1 วันตามอายุอ้อย และย้อนหลังไป 1 ปี
	//echo $st1;
 $graph_dateBegin= $graph_dateBegin*1000-18000000;
 
 
 //$db = mysql_select_db($database,$connection) or die  ("Could not select database.".mysql_error());  
        
                $query = "SELECT * FROM $tablename";
            //    $result = mysql_query($query)or ("Could not query ".mysql_error());  
               
               
 if ($result = mysqli_query($conn,$query))
 {
             
 

                while($row = mysqli_fetch_assoc($result))
                    {
                   $timeOffset = 5*60*60*1000;  

                   $timenow=strtotime('today');
                   $timenow=$timenow*1000-18000000;
                                                      $timestampdate = strtotime($row['date']);
                 
                                                    $timestampbegin=$timestampdate;
                 
                   
                                                    //  echo  $timestampdate;


                                                   $timestampdate=$timestampdate*1000-18000000;
                   
                   $timestamp = strtotime($row['time']);
                   $last_time=$row['time']; 
                   $row['time']= $timestamp*1000-18000000-$timenow+$timestampdate+$timeOffset;
                  // $row['time']=$timenow;
                 //  $row['time']=  $timestampdate;

                  //  $row['date']= date('Y m d', $row['date']);




 
         if (($timestampbegin >= $timeBegin)&&($timestampbegin <= $timeEnd))
             
             
             {
              $label = "Temperature (celcius)";
			//  echo $row['E']; echo ';';
                 if ($row['Temp']>0) {
					 
                  //  $data1[] = array(($row['time']),($row['A']=($row['A']-400)/19.5));    
				  //  $data2[] = array(($row['time']),($row['B']=($row['B']-400)/19.5)); 
				  //  $data3[] = array(($row['time']),($row['C']=($row['C']-1528)/22.8));
				//	 $data4[] = array(($row['time']),($row['D']=($row['D']-500)/40));
//				       $data1[] = array(($row['time']),($row['A']));   
                      $data1[] = array(($row['time']),($row['Temp']));  
					  
				   // $data2[] = array(($row['time']),($row['B'])); 
				      $data2[] = array(($row['time']),($row['Humid'])); 
				      $data3[] = array(($row['time']),($row['Rain']));
					  $data4[] = array(($row['time']),($row['Lux']));
				    
					
					
					  $data17[] = array(($row['time']),(20));
					  $data18[] = array(($row['time']),(25));
				 
				 
				 
				 }
                    //  $timeshow= date("Y-m-d H:i:s",($row['time']-18000000)/1000); 
                      
                    // echo  $timeshow;
					  
                   }      
 




                    }
					

  //echo json_encode($data1);
 
  
  mysqli_free_result($result);
}

//mysqli_close($conn);
///////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////
$tablename = 'a'; 
$legenda1="Station A Moisture 30cm";
$legenda2="Station A Temp 30cm";
$legenda3="Station A Moisture 50cm";
$legenda4="Station A Temp 50cm";
$legend5="";
$legend6="";
$legend7="";
$legend8="";

 
     $t0=strtotime('today');
   
   $graph_dateBegin = strtotime("-7 days ",$t0); 
  // $st1 = strftime("%Y-%m-%d",$st0); //เพิ่มเวลา 1 วันตามอายุอ้อย และย้อนหลังไป 1 ปี
	//echo $st1;
 $graph_dateBegin= $graph_dateBegin*1000-18000000;
 
 
 //$db = mysql_select_db($database,$connection) or die  ("Could not select database.".mysql_error());  
        
                $query = "SELECT * FROM $tablename";
            //    $result = mysql_query($query)or ("Could not query ".mysql_error());  
               
               
 if ($result = mysqli_query($conn,$query))
 {
             
 

                while($row = mysqli_fetch_assoc($result))
                    {
                   $timeOffset = 5*60*60*1000;  

                   $timenow=strtotime('today');
                   $timenow=$timenow*1000-18000000;
                                                      $timestampdate = strtotime($row['date']);
                 
                                                    $timestampbegin=$timestampdate;
                 
                   
                                                    //  echo  $timestampdate;


                                                   $timestampdate=$timestampdate*1000-18000000;
                   
                   $timestamp = strtotime($row['time']);
                   $last_time=$row['time']; 
                   $row['time']= $timestamp*1000-18000000-$timenow+$timestampdate+$timeOffset;
                  // $row['time']=$timenow;
                 //  $row['time']=  $timestampdate;

                  //  $row['date']= date('Y m d', $row['date']);




 
         if (($timestampbegin >= $timeBegin)&&($timestampbegin <= $timeEnd))
             
             
             {
              $label = "Temperature (celcius)";
                 if ($row['G']>0) {
					 
					 $row['A']=$MoisOffset-$MoisSense*$row['A'];
					 $row['C']=$MoisOffset-$MoisSense*$row['C'];
					 $row['B']=($row['B']-$TempOffset)/$TempSense;
					 $row['D']=($row['D']-$TempOffset)/$TempSense;
					 
                    $data5[] = array(($row['time']),($row['A']));    
				    $data6[] = array(($row['time']),($row['B'])); 
				    $data7[] = array(($row['time']),($row['C']));
                    $data8[] = array(($row['time']),($row['D']));
				   				
				}
                    //  $timeshow= date("Y-m-d H:i:s",($row['time']-18000000)/1000); 
                      
                    // echo  $timeshow;
					  
                   }      
 




                    }
					

 // echo json_encode($data5);
 
  
  mysqli_free_result($result);
}

//mysqli_close($conn);



////////////////////////////////////////////////////////////////////////
    
 
///////////////////////////////////////////////////////////////
$tablename = 'b'; 
 $legendb1="Station B Moisture 30cm ";
 $legendb2="Station B Temp 30cm";
$legendb3="Station B Moisture 50cm ";
$legendb4="Station B Temp 50cm ";
$legend5="";
$legend6="";
$legend7="";
$legend8="";
//$data1=null;
//$data2=null;
 // $data3=null;
 // $data4=null;
 // $data5=null;
 /// $data6=null;
 // $data7=null;
 // $data8=null; 
 
 
     $t0=strtotime('today');
   
   $graph_dateBegin = strtotime("-7 days ",$t0); 
  // $st1 = strftime("%Y-%m-%d",$st0); //เพิ่มเวลา 1 วันตามอายุอ้อย และย้อนหลังไป 1 ปี
	//echo $st1;
 $graph_dateBegin= $graph_dateBegin*1000-18000000;
 
 
 //$db = mysql_select_db($database,$connection) or die  ("Could not select database.".mysql_error());  
        
                $query = "SELECT * FROM $tablename";
            //    $result = mysql_query($query)or ("Could not query ".mysql_error());  
               
               
 if ($result = mysqli_query($conn,$query))
 {
             
 

                while($row = mysqli_fetch_assoc($result))
                    {
                   $timeOffset = 5*60*60*1000;  

                   $timenow=strtotime('today');
                   $timenow=$timenow*1000-18000000;
                                                      $timestampdate = strtotime($row['date']);
                 
                                                    $timestampbegin=$timestampdate;
                 
                   
                                                    //  echo  $timestampdate;


                                                   $timestampdate=$timestampdate*1000-18000000;
                   
                   $timestamp = strtotime($row['time']);
                   $last_time=$row['time']; 
                   $row['time']= $timestamp*1000-18000000-$timenow+$timestampdate+$timeOffset;
                  // $row['time']=$timenow;
                 //  $row['time']=  $timestampdate;

                  //  $row['date']= date('Y m d', $row['date']);




 
         if (($timestampbegin >= $timeBegin)&&($timestampbegin <= $timeEnd))
             
             
             {
              $label = "Temperature (celcius)";
                if ($row['G']>0) {
					 
					 $row['A']=$MoisOffset-$MoisSense*$row['A'];
					 $row['C']=$MoisOffset-$MoisSense*$row['C'];
					 $row['B']=($row['B']-$TempOffset)/$TempSense;
					 $row['D']=($row['D']-$TempOffset)/$TempSense;
					 
                    $data9[] = array(($row['time']),($row['A']));    
				    $data10[] = array(($row['time']),($row['B'])); 
				    $data11[] = array(($row['time']),($row['C']));
                    $data12[] = array(($row['time']),($row['D']));
								
				}
                    //  $timeshow= date("Y-m-d H:i:s",($row['time']-18000000)/1000); 
                      
                    // echo  $timeshow;
					  
                   }      
 




                    }
					

 // echo json_encode($data10);
 
  
 // mysqli_free_result($result);
}

//mysqli_close($conn);


///////////////////////////////////////////////////////////////
$tablename = 'c'; 
 $legend1c="R2R151 Top";
 $legend2c="Middle";
$legend3c="Bottom ";
$legend4="";
$legend5="";
$legend6="";
$legend7="";
$legend8="";
//$data1=null;
//$data2=null;
//  $data3=null;
//  $data4=null;
//  $data5=null;
//  $data6=null;
 // $data7=null;
//  $data8=null; 
 
 
     $t0=strtotime('today');
   
   $graph_dateBegin = strtotime("-7 days ",$t0); 
  // $st1 = strftime("%Y-%m-%d",$st0); //เพิ่มเวลา 1 วันตามอายุอ้อย และย้อนหลังไป 1 ปี
	//echo $st1;
 $graph_dateBegin= $graph_dateBegin*1000-18000000;
 
 
 //$db = mysql_select_db($database,$connection) or die  ("Could not select database.".mysql_error());  
        
                $query = "SELECT * FROM $tablename";
            //    $result = mysql_query($query)or ("Could not query ".mysql_error());  
               
               
 if ($result = mysqli_query($conn,$query))
 {
             
 

                while($row = mysqli_fetch_assoc($result))
                    {
                   $timeOffset = 5*60*60*1000;  

                   $timenow=strtotime('today');
                   $timenow=$timenow*1000-18000000;
                                                      $timestampdate = strtotime($row['date']);
                 
                                                    $timestampbegin=$timestampdate;
                 
                   
                                                    //  echo  $timestampdate;


                                                   $timestampdate=$timestampdate*1000-18000000;
                   
                   $timestamp = strtotime($row['time']);
                   $last_time=$row['time']; 
                   $row['time']= $timestamp*1000-18000000-$timenow+$timestampdate+$timeOffset;
                  // $row['time']=$timenow;
                 //  $row['time']=  $timestampdate;

                  //  $row['date']= date('Y m d', $row['date']);




 
         if (($timestampbegin >= $timeBegin)&&($timestampbegin <= $timeEnd))
             
             
             {
              $label = "Temperature (celcius)";
                 if ($row['E']>0) {
					 
                    $data13[] = array(($row['time']),($row['A']));    
				    $data14[] = array(($row['time']),($row['B'])); 
				    $data15[] = array(($row['time']),($row['C']));
				    $data16[] = array(($row['time']),($row['D']));
				
				 
				 }
                    //  $timeshow= date("Y-m-d H:i:s",($row['time']-18000000)/1000); 
                      
                    // echo  $timeshow;
					  
                   }      
 




                    }
					

  //echo json_encode($data16);
 
  
  mysqli_free_result($result);
}

mysqli_close($conn);


 

 
        
}//end if 

else
{
//$date_begin = $_POST['begindate'];  //echo  $date_begin;
     
 //  $date_end = $_POST['enddate'];  // echo $date_end;
$t0=strtotime('today');
 $dateoffset =10*60*60;  
$timeEnd=strtotime('today')+$dateoffset;

$timeBegin=strtotime("-1 days ",$t0); 

$date_begin= date("Y-m-d",$timeBegin);
$date_end= date("Y-m-d",$timeEnd);   





//echo $date_begin;
//echo ':';
//echo $date_end;	 

///////////////////////////////////////////////////////////////

$tablename = 'sensor'; 
 $legend1="Air Temperature";
 $legend2="Humidity";
$legend3="Rain";
$legend4="Light Intensity";
//$legend5="Middle";
//$legend6="Bottom";
//$legend4="";
//$legend5="";
//$legend6="";
$legend7="";
$legend8="";
$data1=null;
$data2=null;
  $data3=null;
  $data4=null;
  $data5=null;
  $data6=null;
  $data7=null;
  $data8=null; 
 $data9=null;
$data10=null;
  $data11=null;
  $data12=null;
  $data13=null;
  $data14=null;
  $data15=null;
  $data16=null; 
 
 
 
 
     $t0=strtotime('today');
   
   $graph_dateBegin = strtotime("-1 days ",$t0); 
  // $st1 = strftime("%Y-%m-%d",$st0); //เพิ่มเวลา 1 วันตามอายุอ้อย และย้อนหลังไป 1 ปี
	//echo $st1;
 $graph_dateBegin= $graph_dateBegin*1000-18000000;
 
 
 //$db = mysql_select_db($database,$connection) or die  ("Could not select database.".mysql_error());  
        
                $query = "SELECT * FROM $tablename";
            //    $result = mysql_query($query)or ("Could not query ".mysql_error());  
               
               
 if ($result = mysqli_query($conn,$query))
 {
             
 

                while($row = mysqli_fetch_assoc($result))
                    {
                   $timeOffset = 5*60*60*1000;  

                   $timenow=strtotime('today');
                   $timenow=$timenow*1000-18000000;
                   $timestampdate = strtotime($row['date']);
                   $timestampbegin=$timestampdate;
                 
                   
                                                    //  echo  $timestampdate;


                   $timestampdate=$timestampdate*1000-18000000;
                   
                   $timestamp = strtotime($row['time']);
                   $last_time=$row['time']; 
                   $row['time']= $timestamp*1000-18000000-$timenow+$timestampdate+$timeOffset;
                  // $row['time']=$timenow;
                 //  $row['time']=  $timestampdate;

                  //  $row['date']= date('Y m d', $row['date']);




 
         if (($timestampbegin >= $timeBegin)&&($timestampbegin <= $timeEnd))
             
             
             {
              $label = "Temperature (celcius)";
                 if ($row['Temp']>0) {
					 
                      $data1[] = array(($row['time']),($row['Temp']));  
					  
				   // $data2[] = array(($row['time']),($row['B'])); 
				      $data2[] = array(($row['time']),($row['Humid'])); 
				      $data3[] = array(($row['time']),($row['Rain']));
					  $data4[] = array(($row['time']),($row['Lux']));
				    
				      $data17[] = array(($row['time']),(20));
					 $data18[] = array(($row['time']),(25));
				 
				 
				 
				 }
                    //  $timeshow= date("Y-m-d H:i:s",($row['time']-18000000)/1000); 
                      
                    // echo  $timeshow;
					  
                   }      
 




                    }
					

//  echo json_encode($data1);
 
  
  mysqli_free_result($result);
}

//mysqli_close($conn);
///////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////
$tablename = 'a'; 
$legenda1="Station A Moisture 30cm ";
$legenda2="Station A Temp 30cm ";
$legenda3="Station A Moisture 50cm ";
$legenda4="Station A Temp 50cm ";
$legend5="";
$legend6="";
$legend7="";
$legend8="";

 
     $t0=strtotime('today');
   
   $graph_dateBegin = strtotime("-7 days ",$t0); 
  // $st1 = strftime("%Y-%m-%d",$st0); //เพิ่มเวลา 1 วันตามอายุอ้อย และย้อนหลังไป 1 ปี
	//echo $st1;
 $graph_dateBegin= $graph_dateBegin*1000-18000000;
 
 
 //$db = mysql_select_db($database,$connection) or die  ("Could not select database.".mysql_error());  
        
                $query = "SELECT * FROM $tablename";
            //    $result = mysql_query($query)or ("Could not query ".mysql_error());  
               
               
 if ($result = mysqli_query($conn,$query))
 {
             
 

                while($row = mysqli_fetch_assoc($result))
                    {
                   $timeOffset = 5*60*60*1000;   

                   $timenow=strtotime('today');
                   $timenow=$timenow*1000-18000000;
                                                      $timestampdate = strtotime($row['date']);
                 
                                                    $timestampbegin=$timestampdate;
                 
                   
                                                    //  echo  $timestampdate;


                                                   $timestampdate=$timestampdate*1000-18000000;
                   
                   $timestamp = strtotime($row['time']);
                   $last_time=$row['time']; 
                   $row['time']= $timestamp*1000-18000000-$timenow+$timestampdate+$timeOffset;
                  // $row['time']=$timenow;
                 //  $row['time']=  $timestampdate;

                  //  $row['date']= date('Y m d', $row['date']);




 
         if (($timestampbegin >= $timeBegin)&&($timestampbegin <= $timeEnd))
             
             
             {
              $label = "Temperature (celcius)";
                 if ($row['G']>0) {
					 
					 $row['A']=$MoisOffset-$MoisSense*$row['A'];
					 $row['C']=$MoisOffset-$MoisSense*$row['C'];
					 $row['B']=($row['B']-$TempOffset)/$TempSense;
					 $row['D']=($row['D']-$TempOffset)/$TempSense;
					 
                    $data5[] = array(($row['time']),($row['A']));    
				    $data6[] = array(($row['time']),($row['B'])); 
				    $data7[] = array(($row['time']),($row['C']));
                    $data8[] = array(($row['time']),($row['D']));
				   				
				}
                    //  $timeshow= date("Y-m-d H:i:s",($row['time']-18000000)/1000); 
                      
                    // echo  $timeshow;
					  
                   }      
 




                    }
					

 // echo json_encode($data5);
 
  
  mysqli_free_result($result);
}

//mysqli_close($conn);



////////////////////////////////////////////////////////////////////////
    
 
///////////////////////////////////////////////////////////////
$tablename = 'b'; 
$legendb1="Station B Moisture 30cm ";
$legendb2="Station B Temp 30cm ";
$legendb3="Station B Moisture 50cm ";
$legendb4="Station B Temp 50cm ";
$legend5="";
$legend6="";
$legend7="";
$legend8="";
//$data1=null;
//$data2=null;
 // $data3=null;
 // $data4=null;
 // $data5=null;
 /// $data6=null;
 // $data7=null;
 // $data8=null; 
 
 
     $t0=strtotime('today');
   
   $graph_dateBegin = strtotime("-7 days ",$t0); 
  // $st1 = strftime("%Y-%m-%d",$st0); //เพิ่มเวลา 1 วันตามอายุอ้อย และย้อนหลังไป 1 ปี
	//echo $st1;
 $graph_dateBegin= $graph_dateBegin*1000-18000000;
 
 
 //$db = mysql_select_db($database,$connection) or die  ("Could not select database.".mysql_error());  
        
                $query = "SELECT * FROM $tablename";
            //    $result = mysql_query($query)or ("Could not query ".mysql_error());  
               
               
 if ($result = mysqli_query($conn,$query))
 {
             
 

                while($row = mysqli_fetch_assoc($result))
                    {
                   $timeOffset = 5*60*60*1000;   

                   $timenow=strtotime('today');
                   $timenow=$timenow*1000-18000000;
                                                      $timestampdate = strtotime($row['date']);
                 
                                                    $timestampbegin=$timestampdate;
                 
                   
                                                    //  echo  $timestampdate;


                                                   $timestampdate=$timestampdate*1000-18000000;
                   
                   $timestamp = strtotime($row['time']);
                   $last_time=$row['time']; 
                   $row['time']= $timestamp*1000-18000000-$timenow+$timestampdate+$timeOffset;
                  // $row['time']=$timenow;
                 //  $row['time']=  $timestampdate;

                  //  $row['date']= date('Y m d', $row['date']);




 
         if (($timestampbegin >= $timeBegin)&&($timestampbegin <= $timeEnd))
             
             
             {
              $label = "Temperature (celcius)";
               //  echo $row['E'].',';
                 if ($row['G']>0) {
					 
					 $row['A']=$MoisOffset-$MoisSense*$row['A'];
					 $row['C']=$MoisOffset-$MoisSense*$row['C'];
					 $row['B']=($row['B']-$TempOffset)/$TempSense;
					 $row['D']=($row['D']-$TempOffset)/$TempSense;
                    
					 
                    $data9[] = array(($row['time']),($row['A']));    
				    $data10[] = array(($row['time']),($row['B'])); 
				    $data11[] = array(($row['time']),($row['C']));
                    $data12[] = array(($row['time']),($row['D']));
								
				}
                    //  $timeshow= date("Y-m-d H:i:s",($row['time']-18000000)/1000); 
                      
                    // echo  $timeshow;
					  
                   }      
 




                    }
					

// echo json_encode($data10);
 
  
 // mysqli_free_result($result);
}

//mysqli_close($conn);


///////////////////////////////////////////////////////////////
$tablename = 'c'; 
 $legendc1="R2R151 Top";
 $legendc2="Middle ";
$legendc3="Bottom ";
$legend4="";
$legend5="";
$legend6="";
$legend7="";
$legend8="";
//$data1=null;
//$data2=null;
//  $data3=null;
//  $data4=null;
//  $data5=null;
//  $data6=null;
 // $data7=null;
//  $data8=null; 
 
 
     $t0=strtotime('today');
   
   $graph_dateBegin = strtotime("-7 days ",$t0); 
  // $st1 = strftime("%Y-%m-%d",$st0); //เพิ่มเวลา 1 วันตามอายุอ้อย และย้อนหลังไป 1 ปี
	//echo $st1;
 $graph_dateBegin= $graph_dateBegin*1000-18000000;
 
 
 //$db = mysql_select_db($database,$connection) or die  ("Could not select database.".mysql_error());  
        
                $query = "SELECT * FROM $tablename";
            //    $result = mysql_query($query)or ("Could not query ".mysql_error());  
               
               
 if ($result = mysqli_query($conn,$query))
 {
             
 

                while($row = mysqli_fetch_assoc($result))
                    {
                   $timeOffset = 12*60*60*1000 ;

                   $timenow=strtotime('today');
                   $timenow=$timenow*1000-18000000;
                                                      $timestampdate = strtotime($row['date']);
                 
                   $timestampbegin=$timestampdate;
                 
                   
                                                    //  echo  $timestampdate;


                                                   $timestampdate=$timestampdate*1000-18000000;
                   
                   $timestamp = strtotime($row['time']);
                   $last_time=$row['time']; 
                   $row['time']= $timestamp*1000-18000000-$timenow+$timestampdate+$timeOffset;
                  // $row['time']=$timenow;
                 //  $row['time']=  $timestampdate;

                  //  $row['date']= date('Y m d', $row['date']);




 
         if (($timestampbegin >= $timeBegin)&&($timestampbegin <= $timeEnd))
             
             
             {
              $label = "Temperature (celcius)";
                 if ($row['A']>0) {
					 
                    $data13[] = array(($row['time']),($row['A']));    
				    $data14[] = array(($row['time']),($row['B'])); 
				    $data15[] = array(($row['time']),($row['C']));
				    $data16[] = array(($row['time']),($row['D']));
				
				 
				 }
                    //  $timeshow= date("Y-m-d H:i:s",($row['time']-18000000)/1000); 
                      
                    // echo  $timeshow;
					  
                   }      
 




                    }
					

  //echo json_encode($data16);
 
  
  mysqli_free_result($result);
}

mysqli_close($conn);





/////////////////////////////////////////////////////////////////////////// 
 









 echo '    
        


 

   
 <p> From

 
 
 <input type="input" id="popup_container3" name="date_begin" size="12" value="',$date_begin,'"></td>    
until
<input type="input" id="popup_container4" name="date_end" size="12" value="',$date_end,'"></td>        
    
<INPUT TYPE="button" align="center" NAME="exportdata" Value="DownloReport" onclick="exportwindow()" >     
 
 <div id="content">
<p><label><input id="enableTooltip" type="checkbox" checked="checked"></input>Enable tooltip</label></p>


   <fieldset> 
   <div id="chartLegend1"></div>
   <legend>Temperature</legend>
		<div class="demo-container">
			<div id="placeholder" class="demo-placeholder"></div>
		</div>

   </fieldset>
	
	
  
    <fieldset> 
   <legend>Moisture Content</legend>
  
		
		<div id="chartLegendHumid"></div> 
 <div class="demo-container5">
			<div id="placeholder5" class="demo-placeholder5"></div>
		</div>
	
	</fieldset>
	
	
	
	
	
	
   <fieldset> 
   <legend>Humidity</legend>
<div id="chartLegend2"></div>
	
		<div class="demo-container2">
			<div id="placeholder2" class="demo-placeholder2"></div>
		</div>
    </fieldset>
		
		<fieldset> 
   <legend>Rain</legend>
   <div id="chartLegend3"></div>
	<div class="demo-container3">
			<div id="placeholder3" class="demo-placeholder3"></div>
		</div>
    
	    </fieldset>
		
		<fieldset> 
   <legend>Light Intensity</legend>
	<div id="chartLegend4"></div>
	<div class="demo-container4">
			<div id="placeholder4" class="demo-placeholder4"></div>
		</div>
    </fieldset>
	
	
  
  
		
		
		

	
			
		

	
		
	</div>






</fieldset> 

        
    </div> ';}
     	
	
	
	
	



      
                     ?>       
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
              
