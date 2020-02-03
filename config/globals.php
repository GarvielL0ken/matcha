<?php
	session_start();
	
	$RGX_NAME = "^[A-Za-z]$";
	$RGX_USERNAME = "^[A-Za-z][A-Za-z0-9.\-_]{3,20}$";
	$DOMAIN_NAME = $_SERVER["REQUEST_SCHEME"] . '://' . $_SERVER["SERVER_NAME"] . ':' . $_SERVER["SERVER_PORT"];
	$USER_KEYS = $arr_keys = array('first_name', 'last_name', 'username', 'gender', 
								   'sexual_preferences', 'bio', 'tags', 'profile_pictures', 
									'age', 'fame_rating');
?>