<style type="text/css">
<!--
.STYLE3 {font-family: "Times New Roman", Times, serif}
.STYLE5 {font-size: larger}
-->
</style>



<table width="979" border="0">
  <tr>
    <th width="1396" align="center" valign="middle" class="STYLE3" scope="row"><div align="center"><span class="STYLE5">
      <p>Resources</p>
    </span>
		<div align="left"><span id="tran_1_0" jquery17107644017319793973="23" data-aligning="#src_1_0,#tran_1_0">If you are interested in these codes, please submit your information and download it!</span></div>
    </div></th>
  </tr>
</table>
<hr />


<form  action="<?php   $varl=$_GET['file'];
				echo "insert.php?file=$varl"?>" method="post" >
<ol >
	<a>Please select your continent  </a><select name="s1" id="continent"  onChange="getCountry()">
						<option value="0" selected>Please Select</option> 
						<option value="1">Africa & Middle East</option>
						<option value="2">America Region</option>
						<option value="3">Asia-Pacific</option>
						<option value="4">Europe Region</option>
					</select></p>
	<a>Please select your   country/region       </a><select name="s2" id="country">
						<option value="0" selected>Please Select</option>
					</select></p>

	<a>Please  input your Email   </a><input type="text" size=18 name="emailcheck" id="email"></p>
	<input type="submit" value="Submit" onClick="return checkemail()" >
 
 </ol>
 </form>
<p class="STYLE3">&nbsp;</p>
<p class="STYLE3">&nbsp;</p>
<p class="STYLE3">&nbsp;</p>


<script type="text/javascript">

	function checkemail(){
	var testresults=false;
	var str=document.getElementById("email").value;
	var filter=/^.+@.+\..{2,3}$/;
	var temp =document.getElementById("country");
	if(temp.options[temp.options.selectedIndex].value=="0"){
		alert("Please select your country/region");
	}
	else{
		if (filter.test(str)){
			testresults=true;
		
		}
		else{
			alert("Please input corrected Email!");
			testresults=false;
		}
	}
	return testresults;
	}	
	
	
	var select1_len = 5;
	var select2 = new Array(select1_len);
	for (i=0; i<select1_len; i++) 
	{
		select2[i] = new Array();
	}
		select2[0][0] = new Option("Please Select", "Please Select");
		
		select2[1][0] = new Option("Africa & Middle East", "Please Select" );        
		select2[1][1] = new Option("Africa & Middle East", "Africa" ); 
		select2[1][2] = new Option("Africa & Middle East", "Algeria" ); 			
		select2[1][3] = new Option("Africa & Middle East", "Egypt" ); 
		select2[1][4] = new Option("Africa & Middle East", "Iraq" ); 
		select2[1][5] = new Option("Africa & Middle East", "Israel" ); 
		select2[1][6] = new Option("Africa & Middle East", "Middle East" ); 		
		select2[1][7] = new Option("Africa & Middle East", "Morocco" );
		select2[1][8] = new Option("Africa & Middle East", "North Africa" );
		select2[1][9] = new Option("Africa & Middle East", "Saudi Arabia" );	
		select2[1][10] = new Option("Africa & Middle East", "South Africa " );	
		select2[1][11] = new Option("Africa & Middle East", "Tunisia" );	
		select2[1][12] = new Option("Africa & Middle East", "Afghanistan" );  	
		
		select2[2][0] = new Option("America Region", "Please Select" );      
		select2[2][1] = new Option("America Region", "Canada" ); 
		select2[2][2] = new Option("America Region", "Latin Spanish " ); 
		select2[2][3] = new Option("America Region", "Mexico" ); 
		select2[2][4] = new Option("America Region", "United States" ); 
		select2[2][5] = new Option("America Region", "Brazil" );  
	
		select2[3][0] = new Option("Asia-Pacific", "Please Select" );   
		select2[3][1] = new Option("Asia-Pacific", "Bangladesh" );    
		select2[3][2] = new Option("Asia-Pacific", "China" );    
		select2[3][3] = new Option("Asia-Pacific", "Hong Kong" );    
		select2[3][4] = new Option("Asia-Pacific", "India" );    
		select2[3][5] = new Option("Asia-Pacific", "Indonesia" );    
		select2[3][6] = new Option("Asia-Pacific", "Japan" );    
		select2[3][7] = new Option("Asia-Pacific", "Korea" );    
		select2[3][8] = new Option("Asia-Pacific", "Maldives" );    
		select2[3][9] = new Option("Asia-Pacific", "Malaysia" );    
		select2[3][10] = new Option("Asia-Pacific", "Nepal" );    
		select2[3][11] = new Option("Asia-Pacific", "New Zealand" );    
		select2[3][12] = new Option("Asia-Pacific", "Pakistan" );    
		select2[3][13] = new Option("Asia-Pacific", "Philippines" );   
		select2[3][14] = new Option("Asia-Pacific", "Singapore" );   
		select2[3][15] = new Option("Asia-Pacific", "Sri Lanka" ); 
		select2[3][16] = new Option("Asia-Pacific", "Taiwan" );
		select2[3][17] = new Option("Asia-Pacific", "Thailand" );
		select2[3][18] = new Option("Asia-Pacific", "Turkey" );
		select2[3][19] = new Option("Asia-Pacific", "Vietnam " );
		select2[3][20] = new Option("Asia-Pacific", "Australia" ); 
		
		select2[4][0] = new Option("Europe Region", "Please Select" );
		select2[4][1] = new Option("Europe Region", "Bulgaria" ); 
		select2[4][2] = new Option("Europe Region", "Czech Rep" ); 
		select2[4][3] = new Option("Europe Region", "Denmark" ); 
		select2[4][4] = new Option("Europe Region", "Finland" ); 
		select2[4][5] = new Option("Europe Region", "France" ); 
		select2[4][6] = new Option("Europe Region", "Germany" ); 
		select2[4][7] = new Option("Europe Region", "Greece" ); 
		select2[4][8] = new Option("Europe Region", "Hungary" ); 
		select2[4][9] = new Option("Europe Region", "Ireland" ); 
		select2[4][10] = new Option("Europe Region", "Italy" ); 
		select2[4][11] = new Option("Europe Region", "Netherlands" ); 
		select2[4][12] = new Option("Europe Region", "Norway" ); 
		select2[4][13] = new Option("Europe Region", "Poland" ); 
		select2[4][14] = new Option("Europe Region", "Portugal" ); 
		select2[4][15] = new Option("Europe Region", "Romania" ); 
		select2[4][16] = new Option("Europe Region", "Russia" ); 
		select2[4][17] = new Option("Europe Region", "Serbia" ); 
		select2[4][18] = new Option("Europe Region", "Slovakia" ); 
		select2[4][19] = new Option("Europe Region", "Spain" ); 
		select2[4][20] = new Option("Europe Region", "Sweden" ); 
		select2[4][21] = new Option("Europe Region", "Switzerland" ); 
		select2[4][22] = new Option("Europe Region", "Ukraine" ); 
		select2[4][23] = new Option("Europe Region", "United Kingdom" ); 	
		select2[4][24] = new Option("Europe Region", "Belgium" );		
	function getCountry()
	{
		var tempcontinent=document.getElementById("continent");
		var temp =document.getElementById("country");
		while(temp.options.length>1){
			temp.options.remove(temp.options.length-1);
		}
		var x=tempcontinent.options.selectedIndex;
		for (i=1;i<=select2[x].length;i++)
		{
			temp.options[i]=new Option(select2[x][i].value)
		}
		temp.options[0].selected=true;
	}  
  
</script>
