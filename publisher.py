from interfaces import IPublisher
import pika

class Publisher(IPublisher):
    def __init__(self, host, exchange="text_exchange"):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
        self.exchange = exchange
        self.channel.exchange_declare(exchange=self.exchange, exchange_type="fanout")

    def publish(self, message):
        self.channel.basic_publish(
            exchange=self.exchange,
            routing_key='',
            body=message
        )
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
    publisher.publish(message=message)
    publisher.close_connection()