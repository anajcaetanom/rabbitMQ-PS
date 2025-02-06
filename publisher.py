from interfaces import IPublisher
import pika

class Publisher(IPublisher):
    def __init__(self, host):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
    
    def publish (self, exchange, message):
        self.channel.exchange_declare(exchange=exchange, exchange_type="fanout")
        self.channel.basic_publish(exchange=exchange, routing_key='', body=message)
        print(f"[x] Documento enviado:\n{message}")

        return message
    
    def close_connection(self):
        self.connection.close()

if __name__ == "__main__":
    message = """#   #        #  #          #   #   #          #     #  #
#   #        #  #          #  # #  #          #     #  #
#   #   ##   #  #   ##      # # # #   ##   ## #   ###  #
#####  #  #  #  #  #  #     # # # #  #  #  #  #  #  #  #
#   #  ####  #  #  #  # ##  # # # #  #  #  #  #  #  #  #
#   #  #     #  #  #  #     # # # #  #  #  #  #  #  #   
#   #   ###  #  #   ##       #   #    ##   #  #   ###  #"""

    publisher = Publisher('localhost')
    publisher.publish(
        exchange='text_exchange',
        message=message
    )
    publisher.close_connection()