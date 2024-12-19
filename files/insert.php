<style type="text/css">
<!--
.STYLE3 {font-family: "Times New Roman", Times, serif}
.STYLE5 {font-size: larger}
-->
</style>



<table width="979" border="0">
  <tr>
    <th width="1396" align="center" valign="middle" class="STYLE3" scope="row"><div align="center"><span class="STYLE5">
     <p> <a href="<?php echo($_GET['file']);?>">download</a></p>
	  
	</th>
  </tr>
</table>
<hr />



<?php
		$local=$_POST['s2'];
		$email=$_POST['emailcheck'];
		$db = mysql_connect("118.139.179.99","rootbupt","SQwsg@163");
		if (!$db)
		{
			die('Could not connect: ' . mysql_error());
		}
	//	echo("connect succeed");
		$sqlname="rootbupt";
		mysql_select_db($sqlname,$db);
		mysql_query("SET NAMES 'utf8'",$db);
		if($local!="0"&&$local!=null){
			$sql = "insert  into local_email(local,email) values('$local','$email')";
			$result = mysql_query($sql); 
		}
	//	echo($result);
		mysql_close($db);
	
?> 

