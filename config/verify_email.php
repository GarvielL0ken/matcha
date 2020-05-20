<?php
	session_start();
	$results = get_results('hashes', 'id_user', array('verification' => $_SESSION['verification_hash']));
	if (!$results)
	print_r($_SESSION['verification_hash']);
?>