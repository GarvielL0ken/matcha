<?php
    require_once 'globals.php';

	function send_email($to, $subject, $message)
	{
		$headers = "MIME-Version: 1.0" . "\r\n";
		$headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";
		if (mail($to, $subject, $message, $headers))
			return (1);
		else
			return (0);
	}

	function send_reset_hash($email, $username, $hash)
	{
		global $DOMAIN_NAME;

		$link = "<a href='" . $DOMAIN_NAME . "/matcha/site/reset_password.php?action=reset_password&hash=$hash'>Link</a>";
		$message = "<html>
						<body>
							<pre>Hello $username.</pre>
							<pre>You can reset your password by clicking the following link: $link</pre>
						</body>
					</html>";
		return (send_email($email, 'Matcha: Reset Passowrd', $message));
	}
?>