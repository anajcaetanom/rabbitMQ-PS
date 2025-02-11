from base_consumer import BaseConsumer

class PDFConsumer(BaseConsumer):
    def __str__(self):
        return "PDF"

if __name__ == "__main__":
    consumer = PDFConsumer("localhost", queue_name="pdf_queue")
    consumer.subscribe()
    consumer.consume()
    consumer.close_connection()