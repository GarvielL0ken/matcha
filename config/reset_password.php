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
		$hash = generate_hash();
		if (send_reset_hash($email, $results[0]['username'], $hash))//REMOVE
			update_record('hashes', array('id_user' => $id_user, 'reset_passwd' => $hash), array('id_user', $id_user));
		else
			$messsage = "Something went wrong while attempting to send the email. This is most likely due to a server side issue";	
		$page = "../site/reset_password.php?action=display_message";
		return (array($page, $messsage));
	}

	function reset_password($post)
	{
		//$results = get_results('hashes', 'id_user', array('reset_passwd', $_SESSION['reset_password_hash']))
		$hash = $post['hash'];
		$page = '../site/reset_password?action=reset_password&hash=' . $hash;
		$results = get_results('hashes', 'id_user', array('reset_passwd', $hash));
		if (!$results)
			redirect_to_page($page, 'Invalid hash');
		$id_user = $results[0]['id_user'];
		$passwd = $post['new_passwd'];
		$confirm_passwd = $post['confirm_passwd']
		if ($passwd != $confirm_passwd)
			redirect_to_page($page, 'Passwords do not match');
		if (!validate_password($passwd))
			redirect_to_page($page, 'Invalid Password');
		$passwd = hash( 'whirlpool', $passwd);
		update_record('users', array('passwd' => $passwd), array('id_user', $id_user));
		remove_hash('verification', $_POST['hash']);
		$page = '../site/login.php';
		redirect_to_page($page, 'Password was successfully changed');
		return (0);
	}

	if ($_POST['submit'] == 'Send link')
		$result = send_link($_POST['email']);
	else if ($_POST['submit'] == 'Reset password')
		$result = reset_password($_POST);
	
	$page = $result[0];
	$messsage = $result[1];
	redirect_to_page($page, $messsage);
?>