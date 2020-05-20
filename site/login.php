<?php
	$page = "Login";
	require_once "header.php";
	if(isset($_SESSION['user_data']))
		$html = 'value = "' . $_SESSION['user_data']['username'] . '"';
	else
		$html = 'placeholder = "JDoe"';
?>
<html>
	<body>
		<?php print_error_msg(); ?>
		<form action= '../config/login.php' method= 'post'>
			<pre>Username: <input required type= 'text' <?php print($html);?> name= 'username'></pre>
			<pre>Password: <input required type= 'password' name= 'passwd'></pre>
			<input type= 'submit' name= 'submit' value= 'Submit'>
			<?php print_error_msg()?>
		</form>
		<pre>Don't have an account? <a href= 'registration.php?'>Create one</a></pre>
	</body>
</html>