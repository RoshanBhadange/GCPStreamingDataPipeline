import json
from PubSub.pub_sub import publisher as pubsub
from datagen import message_generator as msggen

if __name__ == '__main__':
    for i in range(10):
        message_json = msggen.create_random_message()
        data = json.dumps(message_json)
        publish_future = pubsub.publisher.publish(pubsub.topic_path, data.encode("utf-8"))
        publish_future.add_done_callback(pubsub.get_callback(publish_future, data))
        pubsub.publish_futures.append(publish_future)

    # Wait for all the publish futures to resolve before exiting.
    pubsub.futures.wait(pubsub.publish_futures, return_when=pubsub.futures.ALL_COMPLETED)

    print(f"Published messages with error handler to {pubsub.topic_path}.")