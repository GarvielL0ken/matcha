<?php
    function key_isset($array, $key)
    {
        $set = false;
        if (isset($array))
        {
            if (isset($array[$key]))
                $set = true;
        }
        return ($set);
    }

    function output_a($href, $string, $type= null)
    {
        $html = '<a href= "' . $href . '">';
        if (!$type)
            $html .= $string;
        if ($type == 'img')
            $html .=  '<img src= "../resources/' . $string . '.png" alt= "' . $string . '" width= "50" height= "50">';
        $html .= '</a>';
        return ($html);
    }

    function output_field($text, $type, $name, $placeholder= null)
    {
        $html = '<pre>' . $text . '<input required type= "' . $type . '" name= "' . $name . '"';
        $mode = 0;
        if (isset($_SESSION['user_data']))
        {
            if (isset($_SESSION['user_data'][$name]))
                $mode = 1;
        }
        if ($mode)
            $html .= ' value= "' . $_SESSION['user_data'][$name] . '"';
        else if ($placeholder)
            $html .= ' placeholder= "' . $placeholder . '"';
        $html .= '></pre>';
        return ($html);
    }

    function print_error_msg()
	{
		if ($_SESSION['error_msg'])
		{
			print('<pre>' . $_SESSION['error_msg'] . '</pre>');
			$_SESSION['error_msg'] = null;
		}
    }

    function redirect_to_page($page, $error_msg= null, $user_data= null, $null_keys= null)
    {
        $_SESSION['error_msg'] = $error_msg;
        if ($user_data)
            $user_data = set_keys($user_data, $null_keys);
        $_SESSION['user_data'] = $user_data;
        header('Location: ' . $page);
        die();
    }

    function set_keys($user_data, $null_keys)
    {
        $arr_keys = array('first_name', 'last_name', 'username', 'email');
        foreach ($arr_keys as $key)
        {
            if (!isset($user_data[$key]))
                $user_data[$key] = null;
        }
        foreach ($null_keys as $null_key)
            $user_data[$null_key] = null;
        return ($user_data);
    }
?>