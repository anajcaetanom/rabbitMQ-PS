from base_consumer import BaseConsumer

class PDFConsumer(BaseConsumer):
    def __str__(self):
        return "PDF"

if __name__ == "__main__":
    consumer = PDFConsumer("localhost")
    consumer.consume("text_exchange")
    consumer.close_connection()