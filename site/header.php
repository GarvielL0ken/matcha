<?php
    require_once "../config/funcs.php";

    start_session();
    if (!$_SESSION['user'] && ($page != "login" && $page != "registration"))
        redirect_to_page('login.php');

    $html = '<head>
                <title>Matcha: ' . $page . '</title>
            </head>';
?>