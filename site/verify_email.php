<?php
$page = "Verify Email";
require_once "header.php";
?>
<html>
<body>
	<form action= '../config/verify_email.php' method= 'post'>
		<?php
			if ($_GET['action'] == 'resend_link')
			{
				$value = "";
				if ($_SESSION['user_data'])
				{
					if ($_SESSION['user_data']['email'])
						$value = $_SESSION['user_data']['email'];
				}
				print('<pre>Enter your email address and if an account with that email exists a link will be sent</pre>
						<pre>Email: <input required type= "text" name= "email" value="' . $value . '"></pre>
						<input type= "submit" name= "submit" value= "Send link">');
			}
			else if ($_GET['action'] == 'verify_email')
			{
				if (isset($_GET['hash']))
				{
					$_SESSION['verification_hash'] = $_GET['hash'];
					redirect_to_page('../config/verify_email.php');
					print('apples');
				}
				else
				{
					print('<pre>A hash is required to verify your account</pre>
							<pre>If an email was sent to your account then it will contain a link with a hash</pre>
							<pre>If no email was recieved <a href= "./verify_email.php?action=resend_link">click here</a> to resend the email</pre>');
				}
			}
			else if ($_GET['action'] == 'display_message')
				print_error_msg();
		?>
	</form>
</body>
</html>