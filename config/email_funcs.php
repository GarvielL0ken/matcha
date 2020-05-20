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

	function send_verification_email($username, $email, $hash)
	{
		global $DOMAIN_NAME;

		$verification_link = "<a href='" . $DOMAIN_NAME . "/matcha/site/verify_email.php?action=verify_email&hash=$hash'>Link</a>";
		$message = '<html>
						<body>
							<pre>Hello $username.</pre>
							<pre>Verify your Matcha Account by clicking on the following link: $verification_link</pre>
							<pre>If the link does not work copy and paste the following "hash" into the textbox:</pre>
							<pre>' . $hash . '</pre>
							<pre>If this was not you then ignore this email</pre>
						</body>
					</html>';
		send_email($email, "Verify your Matcha Account", $message);
	}
?>