<?php
	$page = "Registration";
	require_once "header.php";
	session_start();
	$set = isset($_SESSION['user_data']);
	$fields = array('first_name', 'last_name', 'username', 'email');
	$placeholders = array('John', 'Doe', 'J.Doe', 'jdoe@gmail.com');
	$html_array = array();
	foreach ($fields as $field)
	{
		$html = '<input required type= "text" ';
		if ($set)
			$html .= 'value= "' . $_SESSION['user_data'][$field] .'"';
		else
			$html .= 'placeholder= "' . $placeholders[$field] . '"';
		$html .= ' name= "' . $field . '"></pre>';
		$html_array[$field] = $html;
	}
?>
<html>
	<form action= '../config/new_user.php' method= "post">
		<pre>First Name:       <?php print($html_array['first_name']);?>
		<pre>Last name:        <?php print($html_array['last_name']);?>
		<pre>Username:         <?php print($html_array['username']);?>
		<pre>Email Address:    <?php print($html_array['email']);?>
		<pre>Password:         <input required type= "password" name= "passwd"></pre>
		<pre>Confirm password: <input required type= "password" name= "confirm_passwd"></pre>
		<input type= "submit" name= "submit" value= "Submit">
		<?php print_error_msg()?>
	</form>
</html>