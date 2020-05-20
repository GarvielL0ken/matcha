<?php
	$page = "Profile";
	require_once "header.php";
?>
<html>
	<body>
		<?php
			$viewed_user = NULL;
			if (!isset($_GET['action'] || !isset($_GET['user']))
				$mode = 'display';
			else
			{
				$mode = $_GET['mode'];
				if ($_GET['user'] != $user->username)
					$viewed_user = new User($_GET['user']);
				if ($viewed_user)
				{
					if ($mode == 'edit')
						$mode = 'view';
				}
				elseif ($mode == 'view')
					$mode = 'display';
			}
			if ($viewed_user)
				$viewed_user->to_string($mode);
			else
				$user->to_string($mode);
		?>
	</body>
</html>