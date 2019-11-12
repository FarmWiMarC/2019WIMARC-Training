<?php


$parent_category = $_GET['TestVar'];
//$parent_category = "test"; 
//dateBegin=" + dateBegin+"?dateEnd=" + dateEnd; 
 
//$dateBegin = "2017-11-16";//$_GET['dateBegin'];
//$dateEnd = "2017-11-20";//$_GET['dateEnd'];
 
 

 
$dateBegin = $_GET['dateBegin'];
$dateEnd = $_GET['dateEnd'];

$tablename = $parent_category; 


if (strcmp($parent_category,"LORAA")==0)
{	$parent_category="waterplant";
}
else
{
	if (strcmp($parent_category,"LORAB")==0) $parent_category="RO";
	
}





 
$filename= $parent_category.'From'.$dateBegin.'To'.$dateEnd.".csv";
$dateBegin=strtotime($dateBegin);
$dateEnd=strtotime($dateEnd);
//alert ($dateBegin);
//alert ($dateEnd);
 
// echo $filename;
 //$connection=mysql_connect("localhost", "791677", "opastrith");
//$connection=mysql_connect("localhost", "root", ""); 
 //$database = "mpibmbk1";

$conn = mysqli_connect("localhost","root","opastrith","mpibmPV1");
/////////////////////////////////////////////////////////////////////////////////////
//$tablename = $parent_category; 
 $legend1="phuket1 pH";
 $legend2="phuket1 DO";
  $legend3="phuket1 Ec";
   $legend4="phuket1 Tur";
    $legend5="phuket1 Level";
	 $legend6="phuket1 Temp";
	  $legend7="phuket1 7";
	   $legend8="phuket1 8";
// $legend3="อุณหภูมิในแปลง 2";
 
 
 
 $db = mysql_select_db($database,$connection) or die  ("Could not select database.".mysql_error());  
        
                $query = "SELECT * FROM $tablename";
                $result = mysql_query($query)or ("Could not query ".mysql_error());  
               
               
     $result = mysql_query($query)or ("Could not query ".mysql_error());  if ($result = mysqli_query($conn,$query))
 {   

   if (strcmp($tablename,"sensor")==0)
   {
   
   $filelabel = "date,"."time,"."Temp(C),"."Humid(%RH),"."Lux(kLux),"."Rain(mm)"."\n";//,"."Turbidity,"."Waterlevel,"."WaterTemp"."\n";
  
   }
    if ((strcmp($tablename,"a")==0)||(strcmp($tablename,"b")==0))
   {
   
   $filelabel = "date,"."time,"."Moisture30cm(mV),"."Temp30cm(C),"."Moisture50cm(mV),"."Temp50cm(C),"."Pressure(Bar)"."\n";//,"."Turbidity,"."Waterlevel,"."WaterTemp"."\n";
   }
   
   $fileoutput='';
   
                while($row = mysql_fetch_assoc($result))
                    {
                  
                   $timestampdate = strtotime($row['date']);
                   
                         $timestampbegin=$timestampdate;

                  
 



    if (($timestampbegin >= $dateBegin)&&($timestampbegin <= $dateEnd))


{
	
	
	if ((strcmp($tablename,"sensor")==0)||(strcmp($tablename,"LORAB")==0))
	{
	
             			  
			   if ($row['Temp']>0) {
                      
				  $row['A']=$row['Temp'];}
			  
                 if ($row['Humid']>0) {
                      
				  $row['B']=$row['Humid'];}
                     if ($row['Lux']>=0) {
                      
				  $row['C']=$row['Lux'];}				  
                					
					if ($row['Rain']>=0) {
                      
				  $row['D']=$row['Rain'];}				
				
	
	 $data= $row['date'].",".$row['time'].",".$row['A'].",".$row['B'].",".$row['C'].",".$row['D']."\n";   
	// echo $data;
	}
    
	else
	{
	
             if (($row['A'] > 300)&&(($row['A']) < 4500)) 
                  {
                      $row['A'] = 225- (($row['A']/1200)*100) ; //($row['A']-400)/1500*14;
				  //$row['A'] =100*$row[A]/29;
                    //  $data1[] = array(($row['time']),($row['A']));
                   
                    }
					else $row['A'] ='-'; 
                 $label2 = "DO";  
                      if (($row['B'] > 300)&&(($row['B']) < 4500)) 
                  {
                      $row['B'] = ($row['B']-500)/10;
				  //$row['A'] =100*$row[A]/29;
                     // $data2[] = array(($row['time']),($row['B']));
                   
                    }
					else $row['B'] ='-'; 
					 if (($row['C'] > 300)&&(($row['C']) < 4500)) 
                  {
                      $row['C'] =  225- (($row['C']/1200)*100) ; //($row['A']-400)/1500*14;
				  //$row['A'] =100*$row[A]/29;
                    //  $data1[] = array(($row['time']),($row['A']));
                   
                    }
					else $row['C'] ='-'; 
					
					
					
				 $label3 = "Conductivity"; 	
					
             if (($row['D'] > 300)&&(($row['D']) < 4500)) 
                  {
                      $row['D'] = ($row['D']-500)/10;
				  //$row['A'] =100*$row[A]/29;
                    //  $data3[] = array(($row['time']),($row['D']));
                //if (strcmp($tablename,"phuket3")==0) {$row['D'] = ($row['D']-400)/1500*40000;}  
                    }
					else $row['D'] ='-'; 
				$label4 = "Turbidity (NTU)"; 	
					
      if (($row['E'] > 300)&&(($row['E']) < 4500)) 
                  {
                   $row['E'] = ($row['E']-500)/1000;
				  //$row['A'] =100*$row[A]/29;
                     // $data4[] = array(($row['time']),($row['E']));
                   
                   }
                  else $row['E'] ='-'; 
/*					
      if (($row['F'] > 100)&&(($row['F']) < 4500)) 
                  {
					  
if (strcmp($tablename,"phuket1")==0)   {$row['F'] = ($row['F']-908)/1.48/1000;}
if (strcmp($tablename,"phuket2")==0)   {  $row['F'] = ($row['F']-170)/900;}
if (strcmp($tablename,"phuket3")==0)  	{ $row['F'] = ($row['F']-214)/1000;}
				  //$row['A'] =100*$row[A]/29;
                    //  $data5[] = array(($row['time']),($row['F']));
                   
                    }
			    $label6 = "Water Temp"; 		
      if (($row['G'] > 300)&&(($row['G']) < 4500)) 
                  {
                    $row['G'] = (2100-$row['G'])/10.9;
				  //$row['A'] =100*$row[A]/29
                    //  $data6[] = array(($row['time']),($row['G']));
                   
                    }
      if (($row['G'] > 300)&&(($row['G']) < 4500)) 
                  {
                    //  $row['G'] = ($row['G']-1850)/1333;
				  //$row['A'] =100*$row[A]/29;
                    //  $data7[] = array(($row['time']),($row['H']));
                   
                    }
      if (($row['H'] > 0)&&(($row['H']) < 4500)) 
                  {
                    //  $row['H'] = ($row['H'])/5000*4;
				  //$row['A'] =100*$row[A]/29;
                    //  $data8[] = array(($row['time']),($row['H']));
                   
                    }	

*/
					
		 $data= $row['date'].",".$row['time'].",".$row['A'].",".$row['B'].",".$row['C'].",".$row['D'].",".$row['E']."\n";   
		//echo $data;
	}


			
   //  $data= $row['date'].",".$row['time'].",".$row['A'].",".$row['B'].",".$row['D'].",".$row['E'].",".$row['F'].",". $row['G']."\n";   
				 
				 
			 $fileoutput= $fileoutput.$data;	 
                       
            //$data=$data.$data;
                       
                   }      
 
                    }
 //////////////////////////////////////////////////////////////////////////////////////////////////////////////
//echo $fileoutput;
 $fileoutput= $filelabel.$fileoutput;	 
 

 header('Content-type: application/csv');
 header('Content-Disposition: attachment; filename='.$filename);


echo $fileoutput;
 
?>
 