<?php
	$page = "Profile";
	require_once "header.php";
?>
<html>
	<body>
		<?php
			if (!isset($_GET['action'])
				$mode = 'display';
			else
				$mode = $_GET['action']
			$user->to_string($mode);
		?>
	</body>
</html>