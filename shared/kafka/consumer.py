from confluent_kafka import Consumer
import json
import asyncio

class ConsumerMeneage:
    def __init__(self, bootstarp_servers:str, topics: list, group_id: str):
        self.conf = {
            "bootstarp_servers": bootstarp_servers,
            "group_id": group_id,
            "auto.offset.reset":"earliest"
        }
        self.consumer = Consumer(self.conf)
        self.topics =topics
    
    async def consumer_loop(self, callback):
        """listening to kafka topic"""
        self.consumer.subscribe(self.topics)
        print(f"Consumer started. Listening to topic {self.topics}...")
        try:
            while True:
                print(f"DEBUG: consumer is polling for messages...")
                msg = await asyncio.to_thread(self.consumer.poll,1.0)

                if msg is None:
                    await asyncio.sleep(0.1)
                    continue

                if msg.error():
                    print(f"consumer error: {msg.error}")
                    continue

                try:
                    row_data = msg.value().decode('utf-8')  # type: ignore
                    data = json.loads(row_data)

                    await callback(data)
                
                except json.JSONDecodeError:
                    print("failed to decode the meesage")
                
                except Exception as e:
                    print(e)
                
        except KeyboardInterrupt:
            print("the consumer stopped by the user")

        finally:
            print("close the consumer")
            self.consumer.close()

