<?php
	require_once 'database.php';

	function connect_to_db()
	{
		global $dbhost, $dbname, $dbusername, $dbpassword;
		try {
			$conn = new PDO("mysql:host=$dbhost", $dbusername, $dbpassword);
			$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
			$conn->exec("CREATE DATABASE IF NOT EXISTS $dbname");
			$conn->query("use $dbname");
			$sql = "CREATE TABLE IF NOT EXISTS `additional_photos` (
				`id_user`			INT				NOT NULL,
				`image_01`			VARCHAR(100)	DEFAULT NULL,
				`image_02`			VARCHAR(100)	DEFAULT NULL,
				`image_03`			VARCHAR(100)	DEFAULT NULL,
				`image_04`			VARCHAR(100)	DEFAULT NULL)";
			$conn->exec($sql);
			$sql = "CREATE TABLE IF NOT EXISTS `blocks` (
				`id_blocker`		INT				NOT NULL,
				`id_blockee`		INT				NOT NULL)";
			$conn->exec($sql);
			$sql = "CREATE TABLE IF NOT EXISTS `genders` (
				`id_gender`			INT				NOT NULL,
				`name`				VARCHAR(128)	NOT NULL)";
			$conn->exec($sql);
			$sql = "CREATE TABLE IF NOT EXISTS `hashes` (
				`id_user`			INT				PRIMARY KEY,
				`verification`		VARCHAR(128)	DEFAULT NULL,
				`reset_passwd`		VARCHAR(128)	DEFAULT NULL)";
			$conn->exec($sql);
			$sql = "CREATE TABLE IF NOT EXISTS `likes` (
				`id_user_1`			INT				NOT NULL,
				`id_user_2`			INT				NOT NULL,
				`match`				BOOLEAN			NOT NULL		DEFAULT FALSE)";
			$conn->exec($sql);
			$sql = "CREATE TABLE IF NOT EXISTS `messages` (
				`id_sender`			INT				NOT NULL,
				`id_receiver`		INT				NOT NULL,
				`time_sent`			TIMESTAMP		NOT NULL,
				`message`			VARCHAR(1024)	NOT NULL)";
			$conn->exec($sql);
			$sql = "CREATE TABLE IF NOT EXISTS `notifications` (
				`id`				INT				AUTO_INCREMENT	PRIMARY KEY,
				`id_to`				INT				NOT NULL,
				`id_from`			INT				NOT NULL,
				`notification`		VARCHAR(20)		NOT NULL)";
			$conn->exec($sql);
			$sql = "CREATE TABLE IF NOT EXISTS `preferences` (
				`id_user`			INT				NOT NULL,
				`id_gender`			INT				NOT NULL)";
			$conn->exec($sql);
			$sql = "CREATE TABLE IF NOT EXISTS `users` (
				`id_user`			INT				AUTO_INCREMENT	PRIMARY KEY,
				`first_name`		VARCHAR(30)		NOT NULL,
				`last_name`			VARCHAR(30)		NOT NULL,
				`username`			VARCHAR(20)		NOT NULL,
				`email`				VARCHAR(70)		NOT NULL,
				`new_email`			VARCHAR(70)		DEFAULT NULL,
				`gender`			INT				DEFAULT NULL,
				`profile_picture`	VARCHAR(100)	DEFAULT NULL,
				`bio`				VARCHAR(256)	DEFAULT NULL,
				`last_online`		VARCHAR(128)		DEFAULT NULL,
				`passwd`			VARCHAR(128)	NOT NULL,
				`verified`			BOOLEAN			NOT NULL		DEFAULT FALSE,
				`info_completed`	BOOLEAN			NOT NULL		DEFAULT FALSE)";
			$conn->exec($sql);
			$sql = "CREATE TABLE IF NOT EXISTS `tags` (
				`id_tag`			INT				AUTO_INCREMENT	PRIMARY KEY,
				`name`				VARCHAR(128)	NOT NULL)";
			$conn->exec($sql);
			$sql = "CREATE TABLE IF NOT EXISTS `tag_map` (
				`id_user`			INT				NOT NULL,
				`id_tag`			INT				NOT NULL)";
			$conn->exec($sql);
			$sql = "CREATE TABLE IF NOT EXISTS `views` (
				`id_viewer`			INT				NOT NULL,
				`id_viewed`			INT				NOT NULL)";
			$conn->exec($sql);
			return($conn);
		} catch (PDOException $pe) {
			die("Could not connect to the database $dbname :" . $pe->getMessage());
		}
	};
?>