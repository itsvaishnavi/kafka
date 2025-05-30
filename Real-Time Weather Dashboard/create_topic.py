from kafka.admin import KafkaAdminClient, NewTopic

# Initialize admin client
admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092",
    client_id='weather-topic-creator'
)

# Define new topic
topic = NewTopic(
    name="weather-data",
    num_partitions=1,
    replication_factor=1
)

# Create topic if it doesn't exist
try:
    admin_client.create_topics(new_topics=[topic], validate_only=False)
    print("Topic 'weather-data' created.")
except Exception as e:
    print(f"Topic might already exist or error occurred: {e}")
