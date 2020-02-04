<?php
    require_once 'funcs.php';
    require_once 'globals.php';

    function validate_post($post, $name, $value)
    {
        if (key_isset($post, $name))
            $valid = false;
        else if ($post[$name] != $value)
            $valid = false;
        if (!$valid)
            redirect_to_page('../index.php');
    }
?>