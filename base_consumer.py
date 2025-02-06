from interfaces import IConsumer
import pika

class BaseConsumer(IConsumer):
    def __init__(self, host):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
    
    def callback(self, ch, method, properties, body):
        print(f"[x] {self}: Processando documento...\nCorpo:\n{body.decode('utf-8')}")
        print("Processamento finalizado!")
    
    def consume(self, exchange):
        self.channel.exchange_declare(exchange=exchange, exchange_type="fanout")

        queue_name = self.create_unique_queue(exchange)

        self.channel.basic_consume(
            queue=queue_name,
            on_message_callback=self.callback,
            auto_ack=True
        )
        print(f"[{self}] está aguardando mensagens. Para sair, pressione CTRL+C")
        self.channel.start_consuming()
    
    def create_unique_queue(self, exchange):
        result = self.channel.queue_declare(queue='', exclusive=True)
        queue_name = result.method.queue
        self.channel.queue_bind(exchange=exchange, queue=queue_name)
        return queue_name
    
    def close_connection(self):
        self.connection.close()