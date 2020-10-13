#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
@Time    :   22:29
@Auther  : Jarrett
@FileName: 1
@Software: PyCharm
"""

import paho.mqtt.client as mqtt

# 当连接上服务器后回调此函数
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # 放在on_connect函数里意味着重新连接时订阅主题将会被更新
    client.subscribe("$SYS/#")

# 从服务器接收到消息后回调此函数
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()  # client = mqtt.Client()  #
client.on_connect = on_connect # 设置连接上服务器回调函数
client.on_message = on_message  # 设置接收到服务器消息回调函数

client.connect("mqtt.eclipse.org", 1883, 60) # 连接服务器，端口为1883，维持心跳为60s

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.publish('chat', 'this is a test') # 往主题chat里发送消息

client.loop_forever()