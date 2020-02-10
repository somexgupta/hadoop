import configparser
import kafka
from kafka_producer_consumer import push_message,get_connection_consumer,get_connection_producer,create_topic
from webscraping import get_movies

config = configparser.ConfigParser()
config.read('config.properties')

# global properties
bootstrap_ip_port=config['KAFKA']['KAFKA_BROKER_IP_PORT']
num_partitions=config['KAFKA']['NUM_PARTITIONS']
replication_factor=config['KAFKA']['REPLICATION_FACTOR']
url=config['SCRAPING_SITE']['URL']
producer = None
consumer = None

# connect to kafka
producer = get_connection_producer(bootstrap_ip_port)

# get list of all the topics present
topic_set=set()
try:
    consumer_topics = kafka.KafkaConsumer(bootstrap_servers=[bootstrap_ip_port])
    topic_set=consumer_topics.topics()
except Exception as ex:
    print('Exception while getting Kafka topics')
    print(str(ex))
finally:
    consumer_topics.close()


print("Press:\n1 to push custom message to kafka topic\n2 to fetch message from a topic\
    \n3 to push message from website and fetch back\n4 to exit\n")
valid_input = [1,2,3,4]
while(True):
    option=int(input("Your input : "))
    if option not in valid_input:
        print(" Enter a valid input ")
        continue
    if option == 4:
        break

    kafka_topic=raw_input("Enter kafka topic name : ")
    
    if kafka_topic not in topic_set:
        res = create_topic(bootstrap_ip_port,kafka_topic,num_partitions, replication_factor)
        if res == 1:
            topic_set.add(kafka_topic)
        else:
            print(res)
            break

    if option == 1:
        kafka_message = raw_input("Enter message to push : ")
        print(push_message(producer,kafka_topic,str(option),kafka_message))
    elif option == 2:
        message_item=[]
        consumer = get_connection_consumer(bootstrap_ip_port,kafka_topic)
        message_item=[msg for msg in consumer]
        print(message_item)
    elif option == 3:
        all_movies = get_movies(url)
        for movies in all_movies:
            _=push_message(producer,kafka_topic,str(option),movies)
        print(_)


if producer is not None :
    producer.close()
if consumer is not None :
    consumer.close()