import pika

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare an exchange named 'example_exchange'
channel.exchange_declare(exchange='example_exchange', exchange_type='direct')

# Publish a message to the exchange
channel.basic_publish(exchange='example_exchange', routing_key='', body='Hello, RabbitMQ!')

print(" [x] Sent 'Hello, RabbitMQ!'")

# Close the connection
connection.close()