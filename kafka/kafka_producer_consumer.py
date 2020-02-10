from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaConsumer, KafkaProducer

def get_connection_producer(bootstrap_ip_port):
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=[bootstrap_ip_port])
    except Exception as ex:
        print('Exception while connecting Kafka producer')
        print(str(ex))
    finally:
        return _producer
def create_topic(bootstrap_ip_port,kafka_topic,num_parts, repli_factor):       
    admin_client = KafkaAdminClient(bootstrap_servers=[bootstrap_ip_port])
    topic_list = []
    topic_list.append(NewTopic(name=kafka_topic, num_partitions=int(num_parts), replication_factor=int(repli_factor)))
    try:
        admin_client.create_topics(new_topics=topic_list, validate_only=False)
    except Exception as ex:
        return ex
    finally:
        admin_client.close()
        return 1

def push_message(producer,kafka_topic,key,kafka_message):
    try:
        key_bytes = key.encode("utf-8")
        value_bytes = kafka_message.encode("utf-8")
        producer.send(kafka_topic, key=key_bytes, value=value_bytes)
        producer.flush()
        return('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        return(str(ex))
        
def get_connection_consumer(bootstrap_ip_port,kafka_topic):
    _consumer = None
    _consumer = KafkaConsumer(kafka_topic, auto_offset_reset='earliest', bootstrap_servers=[bootstrap_ip_port], consumer_timeout_ms=1000)
    return _consumer