# Kafka messaging service
- End to End implementation of Kafka messaging service
- Read, Write messages to and from topics

## Python2.7

How To 
1. Install Required Libraries
```
pip install kafka-python
pip install msgpack
pip install requests
pip install beautifulsoup4
pip install configparser
```
2. Update config.properties file according to your environment
```
[KAFKA]
KAFKA_BROKER_IP_PORT = comma separated values of Kafka broker IP and port
NUM_PARTITIONS = partition number where to create and access topics from
REPLICATION_FACTOR = replication factor of topics

example:
[KAFKA]
KAFKA_BROKER_IP_PORT = 172.18.0.2:6667
NUM_PARTITIONS = 1
REPLICATION_FACTOR = 1

[SCRAPING_SITE]
URL = URL for which you want to perform web scrapping, according to the website line number 19,24,25 of webscraping.py which suits your requirement

example:
[SCRAPING_SITE]
URL = https://in.bookmyshow.com/bengaluru/movies/comingsoon

```
3. Run
```
python main_kafka_messaging.py
```
4. Sample Output
```
Press:
1 to push custom message to Kafka topic
2 to fetch message from a topic    
3 to push message from website and fetch back
4 to exit

Your input : 1
Enter kafka topic name : fruits
Enter message to push : apple
Message push successfully.

Your input : 1
Enter kafka topic name : fruits
Enter message to push : mango
Message push successfully.

Your input : 2
Enter kafka topic name : fruits
[ConsumerRecord(topic=u'fruits', partition=0, offset=0, timestamp=1581347140273, timestamp_type=0, key='1', value='apple', headers=[], checksum=None, serialized_key_size=1, serialized_value_size=5, serialized_header_size=-1), ConsumerRecord(topic=u'fruits', partition=0, offset=1, timestamp=1581347155785, timestamp_type=0, key='1', value='mango', headers=[], checksum=None, serialized_key_size=1, serialized_value_size=5, serialized_header_size=-1)]

Your input : 3
Enter kafka topic name : movies_list
Fetching movies ...
Message push successfully.
Your input : 2
Enter kafka topic name : movies_list
[ConsumerRecord(topic=u'movies_list', partition=0, offset=0, timestamp=1581347288384, timestamp_type=0, key='3', value='Fantasy Island:14 feb', headers=[], checksum=None, serialized_key_size=1, serialized_value_size=21, serialized_header_size=-1), ConsumerRecord(topic=u'movies_list', partition=0, offset=1, timestamp=1581347288442, timestamp_type=0, key='3', value='Hum Bhi Akele Tum Bhi Akele:14 feb', headers=[], checksum=None, serialized_key_size=1, serialized_value_size=34, serialized_header_size=-1), ConsumerRecord(topic=u'movies_list', partition=0, offset=2, timestamp=1581347288445, timestamp_type=0, key='3', value='A Game Called Relationship:14 feb', headers=[], checksum=None, serialized_key_size=1, serialized_value_size=33, serialized_header_size=-1), ConsumerRecord(topic=u'movies_list', partition=0, offset=3, timestamp=1581347288447, timestamp_type=0, key='3', value='Hawayein:14 feb', headers=[], checksum=None, serialized_key_size=1, serialized_value_size=15, serialized_header_size=-1), ConsumerRecord(topic=u'movies_list', partition=0, offset=4, timestamp=1581347288449, timestamp_type=0, key='3', value='Ordinary Love:14 feb', headers=[], checksum=None, serialized_key_size=1, serialized_value_size=20, serialized_header_size=-1), ConsumerRecord(topic=u'movies_list', partition=0, offset=5, timestamp=1581347288450, timestamp_type=0, key='3', value='Joker Re-Release:14 feb', headers=[], checksum=None, serialized_key_size=1, serialized_value_size=23, serialized_header_size=-1)]

Your input : 4
```