from interfaces import IConsumer
import pika

class BaseConsumer(IConsumer):
    def __init__(self, host, exchange="text_exchange", queue_name="queue"):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
        self.exchange = exchange
        self.queue_name = queue_name
        self.channel.exchange_declare(exchange=self.exchange, exchange_type="fanout")
        self.channel.queue_declare(queue=self.queue_name)

    def callback(self, ch, method, properties, body):
        print(f"[x] {self}: Processando documento...\nCorpo:\n{body.decode('utf-8')}")
        print("Processamento finalizado!")

    def consume(self):
        self.channel.basic_consume(
            queue=self.queue_name,
            on_message_callback=self.callback,
            auto_ack=True
        )
        print(f"[{self}] está aguardando mensagens. Para sair, pressione CTRL+C")
        self.channel.start_consuming()

    def subscribe(self):
        self.channel.queue_bind(exchange=self.exchange, queue=self.queue_name)

    def unsubscribe(self):
        self.channel.queue_unbind(exchange=self.exchange, queue=self.queue_name)

    def close_connection(self):
        self.connection.close()