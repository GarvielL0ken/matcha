<?php
	session_start();
	
	$RGX_NAME = "^[A-Za-z]$";
	$RGX_USERNAME = "^[A-Za-z][A-Za-z0-9.\-_]{3,20}$";
	$DOMAIN_NAME = $_SERVER["REQUEST_SCHEME"] . '://' . $_SERVER["SERVER_NAME"] . ':' . $_SERVER["SERVER_PORT"];
	$IMAGES_PER_PAGE = 6;
?>