<?php
	require_once 'funcs.php';
	require_once 'email_funcs.php';
	require_once 'validation_funcs.php';
	require_once 'db_funcs.php';

	session_start();

	function is_set($key)
	{
		return(isset($_POST[$key]));
	}

	if(!isset($_POST))
		exit();
	if (!is_set('first_name') || !is_set('last_name') || !is_set('username') || !is_set('email') || !is_set('passwd') || !is_set('confirm_passwd'))
		exit();
	$first_name     = $_POST['first_name'];
	$last_name      = $_POST['last_name'];
	$username       = $_POST['username'];
	$email          = $_POST['email'];
	$passwd         = $_POST['passwd'];
	$confirm_passwd = $_POST['confirm_passwd'];
	$user_data = array('first_name' => $first_name, 'last_name' => $last_name, 'username' => $username, 'email' => $email);
	$location = '../site/registration.php';
	global $RGX_USERNAME;

	if (!ctype_alpha($first_name))
		redirect_to_page($location, 'Names must only be alphabetical characters', $user_data, array('first_name'));
	if (!ctype_alpha($last_name))
		redirect_to_page($location, 'Names must only be alphabetical characters', $user_data, array('last_name'));
	if(!preg_match('/' . $RGX_USERNAME . '/', $username))
		redirect_to_page($location, 'Invalid Username', $user_data, array('username'));
	if ($passwd != $confirm_passwd)
		redirect_to_page($location, 'Passwords do not match', $user_data);
	if (!validate_password($passwd))
		redirect_to_page($location, 'Invalid Password', $user_data);
	if (is_in_db('users', 'username', $username))
		redirect_to_page($location, 'Username already in use', $user_data);
	$user_data['passwd'] = hash( 'whirlpool', $passwd);
	insert_new_record('users', $user_data);
	$user_id = get_user_id($user_data['username']);
	$hash = generate_hash();
	send_verification_email($username, $email, $hash);
	insert_new_record('hashes', array('id_user' => $user_id, 'verification' => $hash));
	redirect_to_page('../site/verify_email.php?action=verify_email', 
						'A link has been sent to you via email to verify your account<br>Verify your account before attempting to login');
?>