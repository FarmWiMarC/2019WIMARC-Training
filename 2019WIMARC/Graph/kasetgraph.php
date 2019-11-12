
              
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
        <fieldset>


     <table class="table1">
    
    <tfoot>
        <tr>
            <td scope="row">  </td>
           <th width="5%" align="center"> <br> </th>
            <td>',$label,'</td>
           
        </tr>
    </tfoot>
    
</table>    

    
 <p> From
<input type="input" id="popup_container3" name="date_begin" size="12" value="',$date_begin,'"></td>    
until
<input type="input" id="popup_container4" name="date_end" size="12" value="',$date_end,'"></td>        
    
<INPUT TYPE="button" align="center" NAME="exportdata" Value="เก็บข้อมูล download" onclick="exportwindow()" >     
 <p> ฐานข้อมูล <input type="text" name ="database" id="database" value=',$tablename,' >  
<div id="content">
<p><label><input id="enableTooltip" type="checkbox" checked="checked"></input>Enable tooltip</label></p>
<div id="chartLegend"></div>
		<div class="demo-container">
			<div id="placeholder" class="demo-placeholder"></div>
		</div>

	
			
		

	
		
	</div>






</fieldset> 

        
    </div> ';}
 

?>

