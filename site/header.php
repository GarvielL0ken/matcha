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
        </body>
</html>