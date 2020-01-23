<?php
    require_once "../config/funcs.php";

    /*session_start();
    if (!$_SESSION['user'] && ($page != "login" && $page != "registration"))
        redirect_to_page('login.php');*/
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
                if ($p['Login'])
                    print(output_a('registration.php', 'Register'));
                if ($p['Registration'])
                    print (output_a('login.php', 'Login'));
                if (!$p['Login'] && !$p['Registration'] && !$p['Reset Password'])
                    print(output_a('logout.php', 'Logout'));
            ?>
        </body>
</html>