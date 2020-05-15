<?php
	require_once 'email_funcs.php';
	require_once 'db_funcs.php';
	require_once 'funcs.php';

	function send_link($email)
	{
		$_SESSION['user_data']['email'] = $email;
		$results = get_results('users', 'id_user, username', array('email_address', $email));
		if (!$results[0])
			redirect_to_page('../site/reset_passord.php?action=send_link');
		$id_user = $results[0]['id_user'];
		$hash = bin2hex(openssl_random_pseudo_bytes(64));
		if (send_reset_hash($email, $results[0]['username'], $hash))//REMOVE
			update_record('hashes', array('id_user' => $id_user, 'reset_passwd' => $hash), array('id_user', $id_user));
		else
			$messsage = "Something went wrong while attempting to send the email. This is most likely due to a server side issue";	
		$page = "../site/reset_password.php?action=display_message";
		return (array($page, $messsage));
	}

	function reset_password($post)
	{
		//$results = get_results('hashes', 'id_user', array('reset_passwd', $_SESSION['hash']))
		return (0);
	}

	if ($_POST['submit'] == 'Send link')
		$result = send_link($_POST['email']);
	else if ($_POST['submit'] == 'Reset password')
		reset_password($_POST);
	
	$page = $result[0];
	$messsage = $result[1];
	redirect_to_page($page, $messsage);
?>