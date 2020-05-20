<?php
$page = "Verify Email";
require_once "header.php";
?>
<html>
<body>
	<form action= '../config/verify_email.php' method= 'POST'>
		<?php
			if ($_GET['action'] == 'resend_link')
			{
				$value = 'placeholder= "j.doe@gmail.com"';
				if ($_SESSION['user_data'])
				{
					if ($_SESSION['user_data']['email'])
						$value = 'value= "' . $_SESSION['user_data']['email'] . '"';
				}
				$html = '<pre>Enter your email address and if an account with that email exists a link will be sent</pre>
						<pre>Email: <input required type= "text" name= "email" ' . $value . '></pre>';
				$submit = "Send Link";
			}
			else if ($_GET['action'] == 'verify_email')
			{
				$value = 'placeholder= "Da big number(dis do be a hash)"';
				if (isset($_GET['hash']))
					$value = 'value= "' . $_GET['hash'] . '"';
				$html = '<pre>The link sent to you via email should automatically fill the textbox.<br>If not copy and paste the hash from the email into the textbox</pre>';
				$html .= '<pre>Hash: <input required type= "text" name= "hash" ' . $value . '></pre>';
				$submit = "Verify Email";
			}
			if ($_GET['action'] == 'display_message')
				print_error_msg();
			else
			{
				$html .= '<pre><input type= "submit" name= "submit" value= "' . $submit . '"></pre>';
				print($html);
			}
		?>
	</form>
</body>
</html>