from base_consumer import BaseConsumer

class VIMConsumer(BaseConsumer):
    def __str__(self):
        return "VIM"

if __name__ == "__main__":
    consumer = VIMConsumer("localhost", queue_name="vim_queue")
    consumer.subscribe()
    consumer.consume()
    consumer.close_connection()