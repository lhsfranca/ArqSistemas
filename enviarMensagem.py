import pika, os
from time import sleep

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqps://ykqmsyqy:8sBTSsqK5KvGzf0av_jdassL205lmi4N@woodpecker.rmq.cloudamqp.com/ykqmsyqy')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue
channel.basic_publish(exchange='', routing_key='hello', body='Fala ae garotinho')

contador = 0
flag = True
while flag:
        print("[x] Enviado 'Meu bom'")
        sleep(1)
        contador += 1
        if contador == 3:
                flag = False
connection.close()
