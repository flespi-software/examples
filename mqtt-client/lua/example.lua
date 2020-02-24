local mqtt = require("mqtt")

local client = mqtt.client{
	id = "flespi-examples-mqtt-client-lua",
	uri = "mqtt.flespi.io",
	-- see https://flespi.com/kb/tokens-access-keys-to-flespi-platform to read about flespi tokens
	username = "FlespiToken "..(os.getenv("FlespiToken") or ""),
	clean = true,
	secure = true,
	version = mqtt.v50,
}
print("mqtt client created, connecting...")

client:on{
	connect = function(connack)
		if connack.rc ~= 0 then
			print("connection to broker failed:", connack:reason_string(), connack)
			return
		end
		print('connected, subscribing to "test" topic...')

		assert(client:subscribe{ topic="test", qos=1, callback=function()
			print('subscribed to "test" topic, publishing message...')
			assert(client:publish{ topic="test", payload="hello from flespi mqtt client example script!", qos=1 })
		end})
	end,

	message = function(msg)
		assert(client:acknowledge(msg))

		print(string.format('received message in topic "%s": "%s"', msg.topic, msg.payload))
		print("disconnecting...")
		assert(client:disconnect())
	end,

	error = function(err)
		print("mqtt client error:", err)
	end,
}

mqtt.run_ioloop(client)
print("disconnected")
