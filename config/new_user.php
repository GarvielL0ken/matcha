<?php
    print("hello");
    /*require_once 'funcs.php';
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
    $location = '../site/registration.php';*/
    
    /*if (!ctype_alpha($first_name))
        redirect_to_page($location, 'Names must only be alphabetical characters', $user_data, array('first_name'));
    if (!ctype_alpha($last_name))
        redirect_to_page($location, 'Names must only be alphabetical characters', $user_data, array('last_name'));
    if(!preg_match('/' . $RGX_USERNAME . '/', $username))
        redirect_to_page($location, 'Invalid Username', $user_data, array('username'));
    if ($passwd != $confirm_passwd)
        redirect_to_page($location, 'Passwords do not match', $user_data);
    if (!validate_password($passwd))
        redirect_to_page($location, 'Invalid Password', $user_data);*/
    //if (!is_in_db('users', 'username', $username))
        //redirect_to_page($location, 'Username already in use', $user_data);
    //$user_data['passwd'] = hash( 'whirlpool', $passwd);
    //insert_new_record('users', $user_data);
    //redirect_to_page('../site/login.php', 'An email has been sent to your email address to verify your account');
?>