<?php
    require_once "../config/user.class.php";
    require_once "../config/user_funcs.php";
    require_once "../config/funcs.php";
    require_once "../config/setup.php";
    require_once "../config/db_funcs.php";
    
    session_start();
    /*if ($page != 'Login' && $page != 'Registration' && $page != 'Reset Password')
    {
        if (!isset($_SESSION['user']))
            redirect_to_page('login.php');
        if (!$_SESSION['user'])
            redirect_to_page('login.php');
    }*/
?>
<html>
    <head>
        <title>Matcha: <?php print($page)?></title>
    </head>
        <body>
            <h1><?php print($page)?></h1>
            <?php
                $p = array('Chat' => 0, 'Login' => 0, 'Notifications' => 0, 'Profile' => 0, 'Registration' => 0, 'Reset Password' => 0, 'Search' => 0, 'Suggestions' => 0, 'View' => 0);
                $p[$page] = 1;
                if (!$p['Login'] && !$p['Registration'] && !$p['Reset Password'])
                {
                    print(output_a('profile.php', 'profile', 'img'));
                    print(output_a('suggestions.php', 'suggestions', 'img'));
                    print(output_a('search.php', 'search', 'img'));
                    print(output_a('chat.php', 'chat', 'img'));
                    print(output_a('notifications.php', 'notifications', 'img'));
                    print(output_a('logout.php', 'Logout'));
                }
                if ($p['Login'] || $p['Reset Password'])
                    print(output_a('registration.php', 'Register'));
                if ($p['Registration'] || $p['Reset Password'])
                    print (output_a('login.php', 'Login'));
                if ($p['Login'] || $p['Profile'])
                    print(output_a('reset_password.php?action=send_link', 'Reset Password'));
            ?>
        </body>
</html>