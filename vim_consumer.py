from base_consumer import BaseConsumer

class VIMConsumer(BaseConsumer):
    def __str__(self):
        return "VIM"

if __name__ == "__main__":
    consumer = VIMConsumer("localhost")
    consumer.consume("text_exchange")
    consumer.close_connection()