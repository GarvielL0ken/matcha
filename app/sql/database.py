config = {
  'user': 'root',
  'password': '123456',
  'host': 'localhost',
  'raise_on_warnings': True
}

DB_NAME = 'db_matcha_py'

TABLES = {}
TABLES['users'] = (
	"CREATE TABLE IF NOT EXISTS `users` ("
	"  `id_user`		INT				NOT NULL	AUTO_INCREMENT,"
	"  `first_name`		VARCHAR(32)		NOT NULL,"
	"  `last_name`		VARCHAR(32)		NOT NULL,"
	"  `username`		VARCHAR(32)		NOT NULL,"
	"  `email`			VARCHAR(48)		NOT NULL,"
	"  `password`		VARCHAR(256)	NOT NULL,"
	"  `dob`			DATE			DEFAULT NULL,"
	"  `gender`			enum('M','F')	DEFAULT NULL,"
	"  `preferences`	INT				DEFAULT NULL,"
	"  `bio`			VARCHAR(256)	DEFAULT NULL,"
	"  `pict_0`			VARCHAR(64)		DEFAULT NULL,"
	"  `pict_1`			VARCHAR(64)		DEFAULT NULL,"
	"  `pict_2`			VARCHAR(64)		DEFAULT NULL,"
	"  `pict_3`			VARCHAR(64)		DEFAULT NULL,"
	"  `pict_4`			VARCHAR(64)		DEFAULT NULL,"
	"  `intrigue`		INT				DEFAULT NULL,"
	"  PRIMARY KEY (`id_user`)"
	") ENGINE=InnoDB")
TABLES['hashes'] = (
	"CREATE TABLE IF NOT EXISTS `hashes` ("
	"  `id_user`		INT				NOT NULL	AUTO_INCREMENT,"
	"  `verification`	VARCHAR(128)	DEFAULT NULL,"
	"  `reset_password`	VARCHAR(128)	DEFAULT NULL,"
	"  PRIMARY KEY (`id_user`)"
	") ENGINE=InnoDB")
TABLES['tags'] = (
	"CREATE TABLE IF NOT EXISTS `tags` ("
	"  `id_tag`			INT				NOT NULL	AUTO_INCREMENT,"
	"  `text`			VARCHAR(32)		DEFAULT NULL,"
	"  PRIMARY KEY (`id_tag`)"
	") ENGINE=InnoDB")
TABLES['tag_map'] = (
	"CREATE TABLE IF NOT EXISTS `tag_map` ("
	"  `id_user`		INT				NOT NULL,"
	"  `id_tag`			INT				NOT NULL"
	") ENGINE=InnoDB")