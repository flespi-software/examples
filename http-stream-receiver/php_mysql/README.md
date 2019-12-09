# flespi.io http stream receiver (PHP+MySQL)


## Start server

Just copy `index.php` file to your preconfigured **nginx** or **apache** (or another http server) **with PHP and MySQL** support into `/post` (or another) subdirectory.

Then **create a new table** in your database to handle messages.

    CREATE TABLE message_receiver.php_message_listener (
        ident varchar(100) NOT NULL,
        `server.timestamp` DOUBLE NOT NULL,
        `position.longitude` DOUBLE NULL,
        `position.latitude` DOUBLE NULL,
        `timestamp` DOUBLE NULL,
        `position.altitude` DOUBLE NULL,
        `position.direction` DOUBLE NULL,
        `position.speed` DOUBLE NULL,
        `position.satellites` INT NULL,
        CONSTRAINT php_message_listener_PK PRIMARY KEY (ident,`server.timestamp`,`timestamp`)
    )
    ENGINE=MyISAM
    DEFAULT CHARSET=utf8
    COLLATE=utf8_general_ci;

*You can change columns as you wish. But then you should change the respective insert query in index.php*

**Edit MySQL config lines:**

    $mysql_host = 'localhost';
    $mysql_user = 'root';
    $mysql_password = 'password';
    $mysql_db = 'message_receiver';
    $mysql_table = 'php_message_listener';

## Stream configuration

**configuration:** `http`

**uri:** `http://yourserver/post`
