import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare an exchange named 'example_exchange'
channel.exchange_declare(exchange='example_exchange', exchange_type='direct')

# Declare a queue named 'example_queue'
channel.queue_declare(queue='example_queue')

# Bind the queue to the exchange
channel.queue_bind(exchange='example_exchange', queue='example_queue', routing_key='')

print(' [*] Waiting for messages. To exit press CTRL+C')

# Callback function to handle incoming messages
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# Consume messages from the queue
channel.basic_consume(queue='example_queue', on_message_callback=callback, auto_ack=True)

# Start consuming messages
channel.start_consuming()
