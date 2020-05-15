<?php
	require_once 'config/funcs.php';
	require_once 'config/setup.php';
	$conn = connect_to_db();
	redirect_to_page('site/login.php');
?>