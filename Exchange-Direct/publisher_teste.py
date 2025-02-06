from interfaces import IPublisher
import pika

class Publisher(IPublisher):
    def __init__(self, host):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
    
    def publish(self, exchange, message, routing_key):
        self.channel.exchange_declare(exchange=exchange, exchange_type='direct')

        self.channel.basic_publish(exchange=exchange, routing_key=routing_key, body=message)
        print(f"[x] Documento enviado para chave de roteamento '{routing_key}':\n{message}")

        return message
    
    def close_connection(self):
        self.connection.close()

def publish_log():
    message = """Este é um log de exemplo."""
    routing_key = 'log'
    publisher = Publisher('localhost')
    publisher.publish(
        exchange='direct_error_log',
        message=message,
        routing_key=routing_key
    )
    publisher.close_connection()

def publish_error():
    message = """Este é um erro de exemplo."""
    routing_key = 'error'
    publisher = Publisher('localhost')
    publisher.publish(
        exchange='direct_error_log',
        message=message,
        routing_key=routing_key
    )
    publisher.close_connection()

if __name__ == "__main__":
    publish_log()

    publish_error()
