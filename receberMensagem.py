# consume.py
import pika, os

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqps://ykqmsyqy:8sBTSsqK5KvGzf0av_jdassL205lmi4N@woodpecker.rmq.cloudamqp.com/ykqmsyqy')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue
def callback(ch, method, properties, body):
  print(" [x] Recebido " + str(body))

channel.basic_consume('hello', callback, auto_ack=True)

print(' [*] Esperando por mensagens:')
channel.start_consuming()

connection.close()
