<?php
    require_once 'database.php'
    require_once 'setup.php'
    require_once 'validation_funcs.php'
    require_once 'user_funcs.php'

    session_start();

    validate_post($_POST, 'login', 'Login');
    $username = $_POST['username'];
    $password = hash('whirlpool', $_POST['passwd']);
    $valid = true;
    $error_msg = null;

    if (!is_in_db('users', 'username', $username))
    {
        $valid = false;
        $error_msg = 'Username and password match not found';
    }
    if ($valid)
    {
        $results = get_results('users', 'passwd, verified', 'username', $username);
        $db_password = $results[0]['passwd'];
        $db_verified = $results[0]['verified'];
        if ($password != $db_password)
        {
            $valid = false;
            $error_msg = 'Username and password match not found';
        }
        else if (!$db_verified)
        {
            $valid = false;
            $error_msg = 'Verify email address first';
        }
    }
    if (!$valid)
        redirect_to_page('../site/login.php', $error_msg);
    $_SESSION['user'] = create_user($username);
    redirect_to_page('../site/profile.php');
?>