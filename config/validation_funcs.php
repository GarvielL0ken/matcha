<?php
    function validate_post($post, $name, $value)
    {
        $valid = true;
        if (!$_POST)
            $valid = false;
        else if (!isset($_POST[$name]))
            $valid = false;
        else if ($_POST[$name] != $value)
            $valid = false;
        if (!$valid)
            redirect_to_page('../index.php');
    }
?>