<?php
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

	function output_input($required, $type, $name, $value= null, $placeholder= null)
	{
		$html = '<input';
		if ($required)
			$html .= ' required';
		$html .= ' type= "' . $type . '"';
		$html .= ' name= "' . $name . '"';
		if ($value)
			$html .= ' value= "' . $value . '"';
		if ($placeholder)
			$html .= ' placeholder= "' . $placeholder . '"';
		$html .= '>';
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

	function generate_hash()
	{
		$hash = bin2hex(openssl_random_pseudo_bytes(64));
		return ($hash);
	}
?>