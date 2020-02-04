<?php
    session_start();

    $user = $_SESSION['user'];
    if (validate_post($_POST, 'save', 'Save'))
    {
        $error_msg = validate_user_data($_POST);
        if ($error_msg)
            redirect_to_page('../site/profile.php?action=edit', $error_msg);
    }
    else if (!$user->gender)
        $mode = 1;
?>