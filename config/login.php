<?php
	require_once './database.php';
	require_once './setup.php';
	require_once './globals.php';

	$username = $_POST['username'];
	$passwd = $_POST['passwd'];

	if (!$username || !$passwd)
		return (print(1))
	$passwd = hash( 'whirlpool', $passwd);
	$results = get_results('users', 'passwd, verified', array('username' => $username));
	if (!$results)
		redirect_to_page('../site/login.php', 'Password and username do not match');
	if ($results[0]['passwd'] != $passwd)
		redirect_to_page('../site/login.php', 'Password and username do not match');
	if (!$results[0]['verified'])
		redirect_to_page('../site/login.php', 'Validate email address first', array('username' => $username));
	$_SESSION['user_data'] = NULL;
	$_SESSION['user'] = new User($username);
	$action = "";
	if (!$_SESSION['user']->info_completed)
		$action = "?action=edit";
	header("Location: ../site/profile.php" . $action);
?>