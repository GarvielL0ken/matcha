<?php
    function display_user($user, $mode)
    {
        if ($mode == 1)
            $html = '<form action= "../config/update_user_data.php" method= "post">';
        else
            $html = '<div>';
        $arr_keys = array('first_name', 'last_name', 'username', 'gender', 
                          'sexual_preferences', 'bio', 'tags', 'profile_pictures', 
                          'age', 'fame_rating');
        foreach ($arr_keys as $key)
            $html .= output_user_data($user->{$key}, $key, $mode);
        if ($mode == 1)
            $html .= '</form>';
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