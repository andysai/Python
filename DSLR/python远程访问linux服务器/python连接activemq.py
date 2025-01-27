# -*-coding:utf-8-*-
import stomp
import time
import pika

queue_name = '/queue/sai'
topic_name = '/topic/sai'
listener_name = 'SampleListener'
test_name = "saiMqQueue"
springBootMqQueue = '/queue/saiMqQueue'

class SampleListener(object):
    def on_message(self, headers, message):
        print('headers: %s' % headers)
        print('message: %s' % message)

# 推送到队列queue
def send_to_queue(msg):
    conn = stomp.Connection10([('amq-pos-test.cosmo-lady.com', )], auto_content_length=False)
    conn.connect(username='admin', passcode='Dslr2024')
    conn.send(springBootMqQueue, msg)
    conn.disconnect()


#从队列接收消息
def receive_from_queue():
    conn = stomp.Connection10([('amq-pos-test.cosmo-lady.com', 61616)], auto_content_length=False)
    conn.set_listener(listener_name, SampleListener())
    conn.connect(username='admin', passcode='Dslr2024')
    conn.subscribe(springBootMqQueue)
    time.sleep(1)  # secs
    conn.disconnect()

if __name__ == '__main__':
    send_to_queue(
        '{"content":{"flow":{"network":"5","times":"1-1","url":"http://www.baidu.com","way":"5"},"sms":{"direction":"0","text":"短信内容详情"},"voice":{"connect":"5","key":"挂断"}},"form":"13901295021","formPort":"com4","interval":"2-2","network":"5","taskId":"1dsf3641212434g","times":"1-3","to":"18611010269","type":"1"}')
    receive_from_queue()
