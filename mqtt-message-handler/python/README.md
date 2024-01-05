# flespi.io MQTT device message listener

MySQL database, [gmqtt](https://github.com/wialon/gmqtt) library, python 3.5+

**Example:** [device_message_listener.py](device_message_listener.py)

First of all you should **create a new table** in your database to handle messages.

    CREATE TABLE message_receiver.python_message_listener (
        ident varchar(100) NOT NULL,
        `server.timestamp` DOUBLE NOT NULL,
        `position.longitude` DOUBLE NULL,
        `position.latitude` DOUBLE NULL,
        `timestamp` DOUBLE NULL,
        `position.altitude` DOUBLE NULL,
        `position.direction` DOUBLE NULL,
        `position.speed` DOUBLE NULL,
        `position.satellites` INT NULL,
        CONSTRAINT python_message_listener_PK PRIMARY KEY (ident,`server.timestamp`,`timestamp`)
    )
    ENGINE=MyISAM
    DEFAULT CHARSET=utf8
    COLLATE=utf8_general_ci;

*You can change columns as you wish. But then you should change the respective insert query in `on_message` function.*


**Also you should configure the listener by changing these configuration lines:**

    device_id = '12345'
    flespi_mqtt_host = 'mqtt.flespi.io'
    flespi_token = 'YOUR FLESPI TOKEN'
    mysql_host = 'localhost'
    mysql_user = 'root'
    mysql_passwd = 'password'
    mysql_db = 'message_receiver'

**To start this example you need to install the following dependencies:**

    pip3 install asyncio gmqtt pymysql uvloop

**Then start the example:**

    python3 device_message_listener.py
