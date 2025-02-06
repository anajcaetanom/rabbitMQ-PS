from base_consumer2 import BaseConsumer

class LOGConsumer(BaseConsumer):
    def __str__(self):
        return "LOG"

if __name__ == "__main__":
    consumer = LOGConsumer("localhost","log")
    consumer.consume("direct_error_log")
    consumer.close_connection()