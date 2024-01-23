#include <HTTPClient.h>
#include <WiFiClientSecure.h>
#include "credentials.h" // WIFI/MQTT credentials, certs

#if defined(ESP32) || defined(ESP8266)
WiFiClientSecure  wifiClient;
#endif


void setup() {
  Serial.begin(115200);
  Serial.println("Ready");
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(">");
  }
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  WiFiClientSecure *client = new WiFiClientSecure;
  if(client) {
#if defined(ESP32)
    client->setCACert(root_ca);
#elif defined(ESP8266)
    client->setFingerprint(fingerprint);
#endif

    HTTPClient https;
    Serial.print("HTTPS begin\n");
    if (https.begin(*client, HTTPS_SERVER)) {  // HTTPS
      Serial.print("HTTPS POST send\n");
      https.addHeader("Content-Type", "application/json");
      int httpCode = https.POST("[{\"ident\":\"123\"}]");
      if (httpCode > 0) {
       Serial.printf("HTTPS POST code: %d\n", httpCode);
        if (httpCode == HTTP_CODE_OK || httpCode == HTTP_CODE_MOVED_PERMANENTLY) {
          String payload = https.getString();
          Serial.println(payload);
        }
      }
      else {
        Serial.printf("HTTPS POST failed: %s\n", https.errorToString(httpCode).c_str());
      }
      https.end();
    }
  }
  else {
    Serial.printf("HTTPS failed to connect\n");
  }
  Serial.println();

  delay(5000);
}
