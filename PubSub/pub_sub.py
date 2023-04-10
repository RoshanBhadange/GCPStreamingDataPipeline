import Config.config as cfg
from concurrent import futures
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(cfg.params["PROJECT_ID"], cfg.params["TOPIC_ID"])
publish_futures = []

def get_callback(publish_future, data):
    def callback(publish_future):
        try:
        # Wait 60 seconds for the publish call to succeed.
            print(publish_future.result(timeout=60))
        except futures.TimeoutError:
            print(f"Publishing {data} timed out.")
    return callback