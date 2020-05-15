<?php
	session_start();
	$_SESSION['user']->update_online_status(1);
	$_SESSION['user'] = NULL;
?>