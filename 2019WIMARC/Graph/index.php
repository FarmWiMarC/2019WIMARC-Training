<html>
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8" />
 
<script src="jquery.min.js"></script>

  <link rel="stylesheet" href="horizontal.css" type="text/css" charset="utf-8"/>
   <link rel="stylesheet" href="element0.css" type="text/css" charset="utf-8"/>
   <link rel="stylesheet" href="element1.css" type="text/css" charset="utf-8"/>
   <link href="tmecgraph.css" rel="stylesheet" type="text/css">
<script language="javascript" type="text/javascript" src="jquery.js.download"></script>
	<script language="javascript" type="text/javascript" src="jquery.flot.js.download"></script>
		<!--[if lte IE 8]><script language="javascript" type="text/javascript" src="../excanvas.min.js"></script><![endif]-->
    
         <script src="jquery.js"></script>
		<script  type="text/javascript" src="jquery.flot.js"></script>
		
		<script type="text/javascript" src="jquery.flot.stack.js"></script> 
		<script type="text/javascript" src="jquery.flot.fillbetween.js"></script> 
		<script language="javascript" type="text/javascript" src="jquery.flot.categories.js"></script> 
 
<script src="excanvas.min.js"></script>
<script src="jquery.flot.min.js"></script>       
  <script type="text/javascript" src="jquery.flot.axislabels.js"></script>     
  
  
 
     	<link rel="stylesheet" href="/jquery-ui-themes-1.12.1/jquery-ui.css">

      <script src="/jquery-ui-1.12.1/jquery-ui.js"></script>
  
	<script type="text/javascript">
       $(function() {
             //  $("#begindate").datepicker({ dateFormat: "yy-mm-dd" }).val()
			  // $("#enddate").datepicker({ dateFormat: "yy-mm-dd" }).val()
			  
			   $( "#begindate" ).datepicker({
      changeMonth:true,
      changeYear:true,
      yearRange:"-100:+0",
      dateFormat:"dd MM yy"
     });
	 
	  $( "#enddate" ).datepicker({
      changeMonth:true,
      changeYear:true,
      yearRange:"-100:+0",
      dateFormat:"dd MM yy"
     });
	 
	 
	 
			  
       });
   </script>

	

	
  <style type="text/css">


/* ==================== Form style sheet END ==================== */

</style>
    <style>



</style>

<style>

</style>

<style>



</style>






<style>
#chartLegend1 .legendLabel { padding-right: 10px; }
</style>

<style>
#chartLegend2 .legendLabel { padding-right: 10px; }
</style>
<style>
#chartLegend3 .legendLabel { padding-right: 10px; }
</style>
<style>
#chartLegend4 .legendLabel { padding-right: 10px; }
</style>

<style>
#chartLegendHumid .legendLabel { padding-right: 10px; }
</style>

<style>
aside {
  box-sizing: border-box;
  width: 1000px;
  padding: 16px;
  background: #fbb;
  position: absolute;
  top: 0px;
  left: 10px;
  border: 2px solid #f77;
}

</style>
       <!--Load the AJAX API-->
   

       
       
       
       <script type="text/javascript">
   
       
    function drawChartfromtable() {
       
        var TestVar = tablename.value; 
      window.location.href = "showgraphFlot.php?TestVar=" + TestVar; 
                             
    }

    </script> 
</SCRIPT>
<SCRIPT LANGUAGE="JavaScript">
function exportwindow () {
  var TestVar = document.getElementById('database').value;; 
  var dateBegin = document.getElementById('popup_container3').value;
  var dateEnd = document.getElementById('popup_container4').value;
 
    
  //myWindow = window.open("","myWindow","width=200,height=100");    // Opens a new window
// window.location.href = "export_db2.php?TestVar=" + TestVar;       
window.location.href = "exportreportdate.php?TestVar=" + TestVar+"&dateBegin=" + dateBegin+"&dateEnd=" + dateEnd; 
//console.log window.location.href ;


}

</SCRIPT>





       
<title>Soil Moisture Monitoring</title>
 
    

</head>
<body>
<!--<img src="kasetfield.jpg">-->

<div id="data" >

<img id="image" align="middle"  src="/wimarcfarmlogoT.png" />

  
 
 
 
</div>




 
   
                
                


       
       




 
 <?php 

include "indexHistorygraph.php" 
?>
  
             
 <div> 
 
 
 <aside>
 
 <table> 
 <form name="menuform" method="post" target="_self" >
  
    
  
  <td width="75">  
  <BUTTON class="button botton1" name="loadTemp" value="submit" type="submit" title="3 DAYS"> 
  <IMG src="pic/temp3day.png"  width="75" height="75" alt="wow"></BUTTON>
  </td>
 
  <td width="75"> 
  
   <BUTTON class="button botton1" name="loadHum" value="submit" type="submit" title="7 DAYS"> 
  <IMG src="pic/temp7day.png"  width="75" height="75" alt="wow"></BUTTON>
  
  </td>
  
  <td width="75"> 
  
  <BUTTON class="button botton1" name="loadRain" value="submit" type="submit" title="15 DAYS"> 
  <IMG src="pic/temp15day.png"  width="75" height="75" alt="wow"></BUTTON>
  </td>
  
 
 
 
 <!--
  <td width="75"> 
  
  <BUTTON class="button botton1" name="loadWindspeed" value="submit" type="submit" title="Wind Speed"> 
  <IMG src="/pic/WindSpeed.png"  width="75" height="75" alt="wow"></BUTTON>
  </td>
 --> 
  
  

 
 
 
 <td width="75"> 

 <BUTTON class="button botton1" name="loadLux" value="submit" type="submit" titleLux="30 DAYS"> 
  <IMG src="pic/temp30day.png"  width="75" height="75" alt="wow"></BUTTON>
  </td>
 
<td><font color="#006699">FROM</font>

 <input type="text" name="begindate" id="begindate">  
<p>
<font color="#006699">UNTIL</font> 

  <input type="text" name="enddate" id="enddate">  
</td>

  
  <td width="75"> 

  
 <BUTTON class="button botton1" name="loadMoisture" value="submit" type="submit" titleLux="Moisture"> 
 
 <IMG src="pic/tempxday.png"  width="75" height="75" alt="wow"></BUTTON>
  </td>

 
  

 
<!--<td width="75"> <input id="C" NAME="loadBaro" type="submit" value="ความดันบรรยากาศ" /></td>

<td width="75"> <input id="C" NAME="loadRT" type="submit" value="อุณหภูมิห้อง MRD 2" /></td>


    <td width="75"><input id="D" NAME="loadB5" type="submit" value="B5" /></td>
    <td width="75"><input id="D" NAME="loadB6" type="submit" value="B6" /></td>

</tr>

<tr>
 <td width="75"> <input id="C" NAME="loadTsoil" type="submit" value="กระแสไฟจากโซลาร์เซล" /></td>
 
<td width="75"> <input id="C" NAME="loadTDR" type="submit" value="ความชื้นดิน TDR" /></td>

<td width="75"> <input id="C" NAME="loadTen" type="submit" value="ความชื้นดิน Tensiometer" /></td>



</tr>-->
  </table> 
  
  </form>
 
  
      </aside>     	

</div>

  

  
 <script type="text/javascript">

 
	$(function() {
           var stack = 0,
			bars = true,
			lines = false,
			steps = false;
  
              

		 var Data1 = <?php echo json_encode($data1); ?>;
		// var Data2 = <?php echo json_encode($data2); ?>;
        // var Data3 = <?php echo json_encode($data3); ?>;
		// var Data5 = <?php echo json_encode($data5); ?>;
		 var Data6 = <?php echo json_encode($data6); ?>;
         var Data8 = <?php echo json_encode($data8); ?>;
		 // var Data9 = <?php echo json_encode($data9); ?>;
		 var Data10 = <?php echo json_encode($data10); ?>;
         var Data12 = <?php echo json_encode($data12); ?>;
		//  var Data13 = <?php echo json_encode($data13); ?>;
		// var Data14 = <?php echo json_encode($data14); ?>;
        // var Data15 = <?php echo json_encode($data15); ?>;
		// var Data17 = <?php echo json_encode($data17); ?>;
        // var Data18 = <?php echo json_encode($data18); ?>;
		// var Data6 = <?php echo json_encode($data6); ?>;
        //          var Data7 = <?php echo json_encode($data7); ?>;
		// var Data8 = <?php echo json_encode($data8); ?>;
       

		 
                  $.plot("#placeholder", [ 
                //   { data: Data3, label: "<?php echo $legend3; ?>"},
                   { data: Data1, label: "<?php echo $legend1; ?>"},
                //   { data: Data2, label: "<?php echo $legend2; ?>"},
				//   { data: Data5, label: "<?php echo $legenda1; ?>"},
                   { data: Data6, label: "<?php echo $legenda2; ?>"},
                   { data: Data8, label: "<?php echo $legenda3; ?>"},
				//    { data: Data9, label: "<?php echo $legendb1; ?>"},
                   { data: Data10, label: "<?php echo $legendb2; ?>"},
                   { data: Data12, label: "<?php echo $legendb3; ?>"},
				//    { data: Data13, label: "<?php echo $legendc1; ?>"},
                //   { data: Data14, label: "<?php echo $legendc2; ?>"},
                //   { data: Data15, label: "<?php echo $legendc3; ?>"},
                  // { data: Data17,id:"lowerlimit", label: "Lower Limit"},//
                   
				  // { data: Data18,fillBetween:"lowerlimit", label: "Upper Limit"},
				   //   { data: Data17, label: "Lower Limit"},
                   
				 //  { data: Data18, label: "Upper Limit"},
                //  { data: Data6, label: "Sensor 6"},
                //   { data: Data7, label: "Sensor 7"},
                //   { data: Data8, label: "Sensor 8"}
    
                          ], {
			
            series: {
				   points: {show: true}
			},
			yaxis: { axisLabel: "<?php echo $label; ?>"
                                
				
			},
			xaxis: {mode: "time",
                                timeformat: "%d/%m",
                                axisLabel: "วันที่ "
                                
			},
                         grid: {
				hoverable: true,
				clickable: true
			},
                        legend: {
                         noColumns: 3,
                         container: $("#chartLegend1")
                        },
                        
		});

		
		
		
		
$("<div id='tooltip'></div>").css({
			position: "absolute",
			display: "none",
			border: "1px solid #fdd",
			padding: "2px",
			"background-color": "#fee",
			opacity: 0.80
		}).appendTo("body");

		$("#placeholder").bind("plothover", function (event, pos, item) {

			
			if ($("#enableTooltip:checked").length > 0) {
				if (item) {
                                    
                                    
					var x = item.datapoint[0].toFixed(2),
						y = item.datapoint[1].toFixed(2);

var a = new Date(item.datapoint[0]-(7*60*60*1000));
 var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
     var year = a.getFullYear();
     var month = months[a.getMonth()];
     var date = a.getDate();
     var hour = a.getHours();
     var min = a.getMinutes();
     var sec = a.getSeconds();
      var time = "<br />"+" on "+date+' '+month+' '+year+' Time: '+hour+':'+min ;



					$("#tooltip").html(item.series.label +":"+y +time )
						.css({top: item.pageY+5, left: item.pageX+5})
						.fadeIn(200);
				} else {
					$("#tooltip").hide();
				}
			}
		});

		$("#placeholder").bind("plotclick", function (event, pos, item) {
			if (item) {
				$("#clickdata").text(" - click point " + item.dataIndex + " in " + item.series.label);
				plot.highlight(item.series, item.datapoint);
			}
		});



		// Add the Flot version string to the footer

		$("#footer").prepend("Flot " + $.plot.version + " &ndash; ");
	});

	</script>             


<script type="text/javascript">


 
	$(function() {
            
              

		// var Data1 = <?php echo json_encode($data1); ?>;
		// var Data2 = <?php echo json_encode($data2); ?>;
        //          var Data3 = <?php echo json_encode($data3); ?>;
		            var Data2 = <?php echo json_encode($data2); ?>;
              //     var Data2 = <?php echo json_encode($data2); ?>;
		// var Data6 = <?php echo json_encode($data6); ?>;
             //     var Data7 = <?php echo json_encode($data7); ?>;
			//	   var Data17 = <?php echo json_encode($data17); ?>;
        // var Data18 = <?php echo json_encode($data18); ?>;
		// var Data8 = <?php echo json_encode($data8); ?>;
               
                  $.plot("#placeholder2", [ 
                //   { data: Data1, label: "<?php echo $legend1; ?>"},
                //   { data: Data2, label: "<?php echo $legend2; ?>"},
                //   { data: Data3, label: "<?php echo $legend3; ?>"},
                   { data: Data2, label: "<?php echo $legend2; ?>"},
                //  { data: Data2, label: "<?php echo $legenda1; ?>"},
                //   { data: Data6, label: "<?php echo $legenda2; ?>"},
                //   { data: Data7, label: "<?php echo $legenda3; ?>"},
				//    { data: Data17, label: "Lower Limit"},
                   
				//   { data: Data18, label: "Upper Limit"},
               //    { data: Data8, label: "Sensor 8"}
    
                          ], {
			series: {
				   points: {show: true}
			},
                        yaxis: { axisLabel: "Humidity(%RH)"
                                
				
			},
			xaxis: {mode: "time",
                                timeformat: "%d/%m",
                                axisLabel: "วันที่ "
                                
			},
                         grid: {
				hoverable: true,
				clickable: true
			},
                        legend: {
                         noColumns: 3,
                         container: $("#chartLegend2")
                        },
                        
		});

$("<div id='tooltip'></div>").css({
			position: "absolute",
			display: "none",
			border: "1px solid #fdd",
			padding: "2px",
			"background-color": "#fee",
			opacity: 0.80
		}).appendTo("body");

		$("#placeholder2").bind("plothover", function (event, pos, item) {

			
			if ($("#enableTooltip:checked").length > 0) {
				if (item) {
                                    
                                    
					var x = item.datapoint[0].toFixed(2),
						y = item.datapoint[1].toFixed(2);

var a = new Date(item.datapoint[0]-(7*60*60*1000));
 var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
     var year = a.getFullYear();
     var month = months[a.getMonth()];
     var date = a.getDate();
     var hour = a.getHours();
     var min = a.getMinutes();
     var sec = a.getSeconds();
      var time = "<br />"+" on "+date+' '+month+' '+year+' Time: '+hour+':'+min ;



					$("#tooltip").html(item.series.label +":"+y +time )
						.css({top: item.pageY+5, left: item.pageX+5})
						.fadeIn(200);
				} else {
					$("#tooltip").hide();
				}
			}
		});

		$("#placeholder2").bind("plotclick", function (event, pos, item) {
			if (item) {
				$("#clickdata").text(" - click point " + item.dataIndex + " in " + item.series.label);
				plot.highlight(item.series, item.datapoint);
			}
		});



		// Add the Flot version string to the footer

		$("#footer").prepend("Flot " + $.plot.version + " &ndash; ");
	});

	</script>             

	<script type="text/javascript">


 
	$(function() {
            
              

		// var Data9 = <?php echo json_encode($data9); ?>;
		// var Data10 = <?php echo json_encode($data10); ?>;
        // var Data11 = <?php echo json_encode($data11); ?>;
		// var Data17 = <?php echo json_encode($data17); ?>;
        // var Data18 = <?php echo json_encode($data18); ?>;
		 var Data3 = <?php echo json_encode($data3); ?>;
       //            var Data5 = <?php echo json_encode($data5); ?>;
		// var Data6 = <?php echo json_encode($data6); ?>;
      //            var Data7 = <?php echo json_encode($data7); ?>;
		// var Data8 = <?php echo json_encode($data8); ?>;
               
                  $.plot("#placeholder3", [ 
                   { data: Data3, label: "<?php echo $legend3; ?>"},
                  // { data: Data10, label: "<?php echo $legendb2; ?>"},
                  // { data: Data11, label: "<?php echo $legendb3; ?>"},
          //       { data: Data17, label: "Lower Limit"},
                   
				   //{ data: Data18, label: "Upper Limit"},
               //   { data: Data6, label: "Sensor 6"},
               //    { data: Data7, label: "Sensor 7"},
               //    { data: Data8, label: "Sensor 8"}
    
                          ], {
			series: {
				   points: {show: true}
			},
                        yaxis: { axisLabel: "Rain(mm)"
                                
				
			},
			xaxis: {mode: "time",
                                timeformat: "%d/%m",
                                axisLabel: "วันที่ "
                                
			},
                         grid: {
				hoverable: true,
				clickable: true
			},
                        legend: {
                         noColumns: 3,
                         container: $("#chartLegend3")
                        },
                        
		});

$("<div id='tooltip'></div>").css({
			position: "absolute",
			display: "none",
			border: "1px solid #fdd",
			padding: "2px",
			"background-color": "#fee",
			opacity: 0.80
		}).appendTo("body");

		$("#placeholder3").bind("plothover", function (event, pos, item) {

			
			if ($("#enableTooltip:checked").length > 0) {
				if (item) {
                                    
                                    
					var x = item.datapoint[0].toFixed(2),
						y = item.datapoint[1].toFixed(2);

var a = new Date(item.datapoint[0]-(7*60*60*1000));
 var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
     var year = a.getFullYear();
     var month = months[a.getMonth()];
     var date = a.getDate();
     var hour = a.getHours();
     var min = a.getMinutes();
     var sec = a.getSeconds();
      var time = "<br />"+" on "+date+' '+month+' '+year+' Time: '+hour+':'+min ;



					$("#tooltip").html(item.series.label +":"+y +time )
						.css({top: item.pageY+5, left: item.pageX+5})
						.fadeIn(200);
				} else {
					$("#tooltip").hide();
				}
			}
		});

		$("#placeholder3").bind("plotclick", function (event, pos, item) {
			if (item) {
				$("#clickdata").text(" - click point " + item.dataIndex + " in " + item.series.label);
				plot.highlight(item.series, item.datapoint);
			}
		});



		// Add the Flot version string to the footer

		$("#footer").prepend("Flot " + $.plot.version + " &ndash; ");
	});

	</script>             

	
		<script type="text/javascript">


 
	$(function() {
            
              

		 var Data4 = <?php echo json_encode($data4); ?>;
		// var Data14 = <?php echo json_encode($data14); ?>;
        // var Data15 = <?php echo json_encode($data15); ?>;
		// var Data17 = <?php echo json_encode($data17); ?>;
        // var Data18 = <?php echo json_encode($data18); ?>;
		// var Data4 = <?php echo json_encode($data4); ?>;
       //            var Data5 = <?php echo json_encode($data5); ?>;
		// var Data6 = <?php echo json_encode($data6); ?>;
      //            var Data7 = <?php echo json_encode($data7); ?>;
		// var Data8 = <?php echo json_encode($data8); ?>;
               
                  $.plot("#placeholder4", [ 
                   { data: Data4, label: "<?php echo $legend4; ?>"},
          //         { data: Data14, label: "<?php echo $legendc2; ?>"},
           //        { data: Data15, label: "<?php echo $legendc3; ?>"},
          //       { data: Data17, label: "Lower Limit"},
                   
		   //		   { data: Data18, label: "Upper Limit"},
               //   { data: Data6, label: "Sensor 6"},
               //    { data: Data7, label: "Sensor 7"},
               //    { data: Data8, label: "Sensor 8"}
    
                          ], {
			series: {
				   points: {show: true}
			},
                        yaxis: { axisLabel: "Light Intentsity(kLux)"
                                
				
			},
			xaxis: {mode: "time",
                                timeformat: "%d/%m",
                                axisLabel: "วันที่ "
                                
			},
                         grid: {
				hoverable: true,
				clickable: true
			},
                        legend: {
                         noColumns: 3,
                         container: $("#chartLegend4")
                        },
                        
		});

$("<div id='tooltip'></div>").css({
			position: "absolute",
			display: "none",
			border: "1px solid #fdd",
			padding: "2px",
			"background-color": "#fee",
			opacity: 0.80
		}).appendTo("body");

		$("#placeholder4").bind("plothover", function (event, pos, item) {

			
			if ($("#enableTooltip:checked").length > 0) {
				if (item) {
                                    
                                    
					var x = item.datapoint[0].toFixed(2),
						y = item.datapoint[1].toFixed(2);

var a = new Date(item.datapoint[0]-(7*60*60*1000));
 var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
     var year = a.getFullYear();
     var month = months[a.getMonth()];
     var date = a.getDate();
     var hour = a.getHours();
     var min = a.getMinutes();
     var sec = a.getSeconds();
      var time = "<br />"+" on "+date+' '+month+' '+year+' Time: '+hour+':'+min ;



					$("#tooltip").html(item.series.label +":"+y +time )
						.css({top: item.pageY+5, left: item.pageX+5})
						.fadeIn(200);
				} else {
					$("#tooltip").hide();
				}
			}
		});

		$("#placeholder4").bind("plotclick", function (event, pos, item) {
			if (item) {
				$("#clickdata").text(" - click point " + item.dataIndex + " in " + item.series.label);
				plot.highlight(item.series, item.datapoint);
			}
		});



		// Add the Flot version string to the footer

		$("#footer").prepend("Flot " + $.plot.version + " &ndash; ");
	});

	</script>             

	
	
	
	
	
	
	
	
	<script type="text/javascript">


 
	$(function() {
            
              

		 var Data5 = <?php echo json_encode($data5); ?>;
		 var Data7 = <?php echo json_encode($data7); ?>;
         var Data9 = <?php echo json_encode($data9); ?>;
		 var Data11 = <?php echo json_encode($data11); ?>;
              //     var Data5 = <?php echo json_encode($data5); ?>;
		// var Data6 = <?php echo json_encode($data6); ?>;
        //          var Data7 = <?php echo json_encode($data7); ?>;
		// var Data8 = <?php echo json_encode($data8); ?>;
               
                  $.plot("#placeholder5", [ 
                   { data: Data5, label: "<?php echo $legenda1; ?>"},
                   { data: Data7, label: "<?php echo $legenda2; ?>"},
                   { data: Data9, label: "<?php echo $legendb1; ?>"},
                   { data: Data11, label: "<?php echo $legendb2; ?>"},
             //       { data: Data5, label: "<?php echo $legend5; ?>"},
            //      { data: Data6, label: "Sensor 6"},
             //      { data: Data7, label: "Sensor 7"},
             //      { data: Data8, label: "Sensor 8"}
    
                          ], {
			series: {
				   points: {show: true}
			},
                        yaxis: { axisLabel: "Moisture Volumatic Content"
                                
				
			},
			xaxis: {mode: "time",
                                timeformat: "%d/%m",
                                axisLabel: "วันที่ "
                                
			},
                         grid: {
				hoverable: true,
				clickable: true
			},
                        legend: {
                         noColumns: 3,
                         container: $("#chartLegendHumid")
                        },
                        
		});

$("<div id='tooltip'></div>").css({
			position: "absolute",
			display: "none",
			border: "1px solid #fdd",
			padding: "2px",
			"background-color": "#fee",
			opacity: 0.80
		}).appendTo("body");

		$("#placeholder5").bind("plothover", function (event, pos, item) {

			
			if ($("#enableTooltip:checked").length > 0) {
				if (item) {
                                    
                                    
					var x = item.datapoint[0].toFixed(2),
						y = item.datapoint[1].toFixed(2);

var a = new Date(item.datapoint[0]-(7*60*60*1000));
 var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
     var year = a.getFullYear();
     var month = months[a.getMonth()];
     var date = a.getDate();
     var hour = a.getHours();
     var min = a.getMinutes();
     var sec = a.getSeconds();
      var time = "<br />"+" on "+date+' '+month+' '+year+' Time: '+hour+':'+min ;



					$("#tooltip").html(item.series.label +":"+y +time )
						.css({top: item.pageY+5, left: item.pageX+5})
						.fadeIn(200);
				} else {
					$("#tooltip").hide();
				}
			}
		});

		$("#placeholder5").bind("plotclick", function (event, pos, item) {
			if (item) {
				$("#clickdata").text(" - click point " + item.dataIndex + " in " + item.series.label);
				plot.highlight(item.series, item.datapoint);
			}
		});



		// Add the Flot version string to the footer

		$("#footer").prepend("Flot " + $.plot.version + " &ndash; ");
	});

	</script>             



 
 
              
<?php include "indexshowgraph.php" ?>
           
 
              
              
 

  <script src="jquery.simple-scroll-follow.min.js"></script>
 <script src="sample.js"></script>            
              
              
              
              
              
              






</body>



</html>