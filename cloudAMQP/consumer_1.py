import pika, os, time

def pdf_process_function(msg):
    print("PDF processing...")
    print("[x] Received " + str(msg))

    time.sleep(5)
    print("PDF processing finished.")
    return;

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

def callback(ch, method, properties, body):
    pdf_process_function(body)

channel.basic_consume(
    'pdfprocess',
    callback,
    auto_ack=True
)

channel.start_consuming()
connection.close()