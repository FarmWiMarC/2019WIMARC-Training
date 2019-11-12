<?php

$parent_category = $_GET['TestVar'];
 
//dateBegin=" + dateBegin+"?dateEnd=" + dateEnd; 
 
 
$dateBegindb = $_GET['dateBegin'];
$dateEnddb = $_GET['dateEnd'];
 
$filename= $parent_category.'From'.$dateBegin.'To'.$dateEnd;
$dateBegin=strtotime($dateBegindb);
$dateEnd=strtotime($dateEnddb);
//alert ($dateBegin);
//alert ($dateEnd);
 
       

 
//echo $parent_category;
$extension=".xls";
$downloadfile = $filename.$extension;
$table = "SELECT * FROM ";
 //  $parent_category = "datafrom25570415";
   $table2 = $table.$parent_category;
 
// Connect to database server and select database
//$con = mysql_connect('localhost','997989','ricelab2015');
//mysql_select_db('997989db2', $con); 
 $database = "GHNongMang";
$con = mysql_connect('localhost','791677','opastrith');
mysql_select_db($database, $con); 

 
// write your SQL query here (you may use parameters from $_GET or $_POST if you need them)
$export = mysql_query($table2);
$header = '';
$data ='';
//$export = mysql_query ($query ) or die ( "Sql error : " . mysql_error( ) );
 
// extract the field names for header 
//$fields = mysql_num_fields ( $export );
/*

$dateBegin = "2017-11-16";//$_GET['dateBegin'];
$dateEnd = "2017-11-20";//$_GET['dateEnd'];
$dateBegin=strtotime($dateBegin);
$dateEnd=strtotime($dateEnd);



$connection=mysql_connect("localhost", "791677", "opastrith");
//$connection=mysql_connect("localhost", "root", "1234"); 
 //$database = "GHbangyai";
  $database = "warehouse";
 $result = mysql_list_tables($database);

 $tablename1 = 'a';
 $tablename2 = 'a';
 $tablename3 = 'b';
 $tablename4 = 'c';
 $tablename5 = 'd';
 //  echo $tablename1;
             
              
         
 $db = mysql_select_db($database,$connection) or die  ("Could not select database.".mysql_error());  
        
                $query1 = "SELECT * FROM $tablename1";
                $result1 = mysql_query($query1)or ("Could not query ".mysql_error());  
               
 */
 


//$fileoutput=$database."from ".$dateBegindb."until ".$dateEnddb."time".",".","."";
echo $database."from ".$dateBegindb."until ".$dateEnddb.","."time".",".",".""."\n";
$fileoutput=""; 
for ( $i = 0; $i < 24; $i++ )
{ 
//echo "H: ".$i;

$Aave=0;
$Bave=0;
$Cave=0;
$Dave=0;
$Eave=0;
$Fave=0;
$Gave=0;


    if ($i<10)
   {	
   $timescan =  "0".$i;//.":00";
   }
   else
   {
	$timescan =  $i;//.":00";   
   }   

$db = mysql_select_db($database,$con) or die  ("Could not select database.".mysql_error());  
        
               // $query1 = "SELECT * FROM $tablename1";
                $export= mysql_query($table2)or ("Could not query ".mysql_error());  
               
while( $row = mysql_fetch_row( $export ) )
{
 
          $timestampdate = strtotime($row[0]);
    //      $timestamptime = strtotime($row[2]);
//$message = "wrong answer";
   // echo    $timestampdate;
 
// echo "<script type='text/javascript'>alert('$row[1]');</script>"; 
 
             $timestampbegin=$timestampdate;
   if (($timestampbegin >= $dateBegin)&&($timestampbegin <= $dateEnd))
   {    $timecheck =  substr($row[1],0,2);
       // echo   $timescan;
    if ($timecheck == $timescan)
	{	
    ////////////////////////////////////////////////   
     if (($row[2]>0) && ($Aave >0))  
	 { $Aave =($Aave+$row[2])/2;
 
    //  echo   $Aave; 
       $timesave=$timecheck;
     
	 }
	 else
	 { if ($Aave == 0)
         {		 
		 $Aave = $row[2];
		 }
	 }	 
    ////////////////////////////////////////////////   
     if (($row[3]>0) && ($Bave >0))  
	 { $Bave =($Bave+$row[3])/2;
 
    //  echo   $Aave; 
       $timesave=$timecheck;
     
	 }
	 else
	 { if ($Bave == 0)
         {		 
		 $Bave = $row[3];
		 }
	 }
	////////////////////////////////////////////////   
     if (($row[4]>0) && ($Cave >0))  
	 { $Cave =($Cave+$row[4])/2;
 
    //  echo   $Aave; 
       $timesave=$timecheck;
     
	 }
	 else
	 { if ($Cave == 0)
         {		 
		 $Cave = $row[4];
		 }
	 }
	////////////////////////////////////////////////   
     if (($row[5]>0) && ($Dave >0))  
	 { $Dave =($Dave+$row[5])/2;
 
    //  echo   $Aave; 
       $timesave=$timecheck;
     
	 }
	 else
	 { if ($Dave == 0)
         {		 
		 $Dave = $row[5];
		 }
	 }
	
	////////////////////////////////////////////////   
     if (($row[6]>0) && ($Eave >0))  
	 { $Eave =($Eave+$row[6])/2;
 
    //  echo   $Aave; 
       $timesave=$timecheck;
     
	 }
	 else
	 { if ($Eave == 0)
         {		 
		 $Eave = $row[6];
		 }
	 }
	
	////////////////////////////////////////////////   
     if (($row[7]>0) && ($Fave >0))  
	 { $Fave =($Fave+$row[7])/2;
 
    //  echo   $Aave; 
       $timesave=$timecheck;
     
	 }
	 else
	 { if ($Fave == 0)
         {		 
		 $Fave = $row[7];
		 }
	 }
	
	////////////////////////////////////////////////   
     if (($row[8]>0) && ($Gave >0))  
	 { $Gave =($Gave+$row[8])/2;
 
    //  echo   $Aave; 
       $timesave=$timecheck;
     
	 }
	 else
	 { if ($Gave == 0)
         {		 
		 $Gave = $row[8];
		 }
	 }
	
	} 
 //echo "<script type='text/javascript'>alert('$row[1]');</script>";    
//echo "<script type='text/javascript'>alert('$dateBegin');</script>"; 
 
 
    
    }
     $fileoutput = $timesave.",".$Aave.",".$Bave.",".$Cave.",".$Dave.",".$Eave.",".$Fave.",".$Gave;
}

$fileoutput = $fileoutput."\n";//.$timescan.",".$Aave.","; 
echo $fileoutput;


} 
if ( $fileoutput == "" )
{
    $data = "\nNo Record(s) Found!\n";                        
}

   $filename = $parent_category.".csv";
           header('Content-type: application/csv');
          header('Content-Disposition: attachment; filename='.$filename);

			echo $fileoutput;
		//	echo $output;
		//	echo $data1[];
			exit;

/*
 
// allow exported file to download forcefully
header("Content-type: application/octet-stream");
//header("Content-Disposition: attachment; filename=export.xls");
header("Content-Disposition: attachment; filename=".$downloadfile);
header("Pragma: no-cache");
header("Expires: 0");
print "$header\n$data";
*/ 
?>
 