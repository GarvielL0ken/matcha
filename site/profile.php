<?php
    $page = "Profile";
    require_once "header.php";
?>
<html>
    <body>
        <div>
            <?php
                $user = new User(array('username' => 'Joe', 'first_name' => 'Not_Joe', 'last_name' => 'Joeson'));
                $mode = 0;
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