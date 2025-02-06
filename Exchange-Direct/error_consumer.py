from base_consumer2 import BaseConsumer

class ERRORConsumer(BaseConsumer):
    def __str__(self):
        return "ERROR"

if __name__ == "__main__":
    consumer = ERRORConsumer("localhost", "error")
    consumer.consume("direct_error")
    consumer.close_connection()