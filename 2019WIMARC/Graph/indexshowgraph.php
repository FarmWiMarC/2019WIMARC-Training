
<?php


 


  if ((isset($_POST['loadTemp']))||(isset($_POST['loadHum']))||
         (isset($_POST['loadRain']))||(isset($_POST['loadWindspeed']))||(isset($_POST['loadLevel']))
         ||(isset($_POST['loadLux']))
		 ||(isset($_POST['loadAir'])) 
		   ||(isset($_POST['loadMoisture'])) 
		    ||(isset($_POST['loadDust'])) 
         
         )   
    {  
      
    
      
      
    echo '    
     
    

 
 <p> From

 
 <input type="input" id="popup_container3" name="date_begin" size="12" value="',$date_begin,'"></td>    
until
<input type="input" id="popup_container4" name="date_end" size="12" value="',$date_end,'"></td>        
    
<INPUT TYPE="button" align="center" NAME="exportdata" Value="Download Report" onclick="exportwindow()" >     
 <p> ฐานข้อมูล <input type="text" name ="database" id="database" value=',$tablename,' >  

 
 <div id="content">
<p><label><input id="enableTooltip" type="checkbox" checked="checked"></input>Enable tooltip</label></p>

<div id="chartLegend1"></div>
   <fieldset> 
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
		
		
	</fieldeset>
	
	
	
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