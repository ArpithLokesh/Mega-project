import pika, os

def send_to_pi  (data):
    # Set up a connection to RabbitMQ
    url = 'amqps://rznmrvmc:3ZLKmdI3B43dr4pZYc4Q9NGdEhXml5ob@puffin.rmq2.cloudamqp.com/rznmrvmc'
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel() # start a channel
    
    queue_name = 'raspberry_pi'

    # Declare a queue for app2 to consume
    channel.queue_declare(queue=queue_name)

    # Send the data to the queue
    channel.basic_publish(exchange='', routing_key=queue_name, body=data)

    print("Message sent..")

    # Close the connection
    connection.close()