<?php
    require_once 'db_funcs.php';
    require_once 'globals.php';
    require_once 'user.class.php';

    function create_user($username)
    {
        global $USER_KEYS;
        foreach ($USER_KEYS as $key)
            $columns .= $key .',';
        $columns = substr($columns, 0, -1);
        $results  = get_results('users', $columns, 'username', $username);
        foreach ($USER_KEYS as $key)
            $arr_user_data[$key] = $results[$key];
        $user = new User($arr_user_data);
    }

    function display_user($user, $mode)
    {
        global $USER_KEYS;
        if ($mode == 1)
            $html = '<form action= "../config/profile.php" method= "post">';
        else
            $html = '<div>';
        foreach ($USER_KEYS as $key)
            $html .= output_user_data($user->{$key}, $key, $mode);
        if ($mode == 1)
            $html .= '<input type= "submit" name= "save" value= "Save"></form>';
        else
            $html .= '</div>';
        print($html);
    }

    function output_user_data($data, $field, $mode)
    {
        $html = '<pre>';
        if (!$mode)
            $html .= $data;
        else
        {
            $html .= $field . ': <input required type= "text" name= "' . $field . '"';
            if ($data)
                $html .= ' value= "' . $data . '"';
            $html .= '>';
        }
        $html .= '</pre>';
        return ($html);
    }
?>