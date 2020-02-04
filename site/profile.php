<?php
    $page = "Profile";
    $mode = 0;
    
    require_once "header.php";
    require_once '../config/profile.php';
?>
<html>
    <body>
        <div>
            <?php
                if (isset($_GET))
                {
                    if (isset($_GET['action']))
                    {
                        if ($_GET['action'] == 'edit')
                            $mode = 1;
                    }
                }
                display_user($user, $mode);
            ?>
        </div>
    </body>
</html>