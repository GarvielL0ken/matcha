<?php
	function validate_password($passwd)
	{
		if (!preg_match('/[A-Z]/', $passwd) || !preg_match('/[a-z]/', $passwd) || !preg_match('/[0-9]/', $passwd))
			return(false);
		if (strlen($passwd) < 2) //change to 8
			return(false);
		return(true);
	}
?>