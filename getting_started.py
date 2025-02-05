import pika, sys, os

def send():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='fila')

    channel.basic_publish(exchange='',
                          routing_key='fila',
                          body='oie')

    print("fulano mandou 'oie'")

    connection.close()

def callback(ch, method, properties, body):
    print(f"fulano recebeu {body}")

def receive():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='fila')

    channel.basic_consume(queue='fila',
                          auto_ack=True,
                          on_message_callback=callback)

    print('fulano esperando por mensagens. pra sair aperta ctrl + c')
    channel.start_consuming()

def main():
    try:
        send()
        receive()
    except KeyboardInterrupt:
        print('interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

if __name__ == "__main__":
    main()

