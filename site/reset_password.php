<?php
	$page = "Reset Password";
	require_once "header.php";
?>
<html>
	<body>
		<form action= '../config/reset_password.php' method= 'post'>
			<?php
				if ($_GET['action'] == 'send_link')
				{
					$value = "";
					if ($_SESSION['user_data'])
					{
						if ($_SESSION['user_data']['email'])
							$value = $_SESSION['user_data']['email'];
					}
					print('<pre>Enter your email address and a link will be sent to reset your password</pre>
							<pre>Email: <input required type= "text" name= "email" value="' . $value . '"></pre>
							<input type= "submit" name= "submit" value= "Send link">');
				}
				else if ($_GET['action'] == 'reset_password')
				{
					if (isset($_GET['hash']))
					{
						$_SESSION['reset_password_hash'] = $_GET['hash'];
						print('<pre>    New password: <input required type= "password" name= "new_password"></pre>
						<pre>Confirm password: <input required type= "password" name= "confirm_pasword"></pre>
						<pre>            Hash: <input required type= "text" name= "hash" value= "' . $_GET['hash'] . '"></pre>
						<input type= "submit" name= "submit" value= "Reset password">');
					}
					else
					{
						print('<pre>A hash is required to reset a password</pre>
								<pre>If an email was sent to your account then it will contain a hash</pre>
								<pre>If no email was recieved <a href= "./reset_password.php?action=send_link">click here</a> to resend the email</pre>');
					}
				}
				else if ($_GET['action'] == 'display_message')
					print_error_msg();
			?>
		</form>
	</body>
</html>