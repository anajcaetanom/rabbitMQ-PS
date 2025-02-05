import pika, os, logging
logging.basicConfig()

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='pdfprocess')

channel.basic_publish(
    exchange='',
    routing_key='pdfprocess',
    body='Nome: Deivison lindo'
)

print("[x] Message sent to consumer.")

connection.close()