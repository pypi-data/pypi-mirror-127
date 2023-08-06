﻿import json
from pynats import NATSClient, NATSMessage  # noqa
from function_scheduling_distributed_framework.consumers.base_consumer import AbstractConsumer
from function_scheduling_distributed_framework import frame_config


class NatsConsumer(AbstractConsumer):
    """
    nats作为中间件实现的。
    """
    BROKER_KIND = 24

    def _shedual_task(self):
        self.nats_client = NATSClient(frame_config.NATS_URL)
        self.nats_client.connect()

        def callback(msg: NATSMessage):
            # print(type(msg))
            # print(msg.reply)
            # print(f"Received a message with subject {msg.subject}: {msg.payload}")
            kw = {'body': json.loads(msg.payload)}
            self._submit_task(kw)

        self.nats_client.subscribe(subject=self.queue_name, callback=callback)
        self.nats_client.wait()

    def _confirm_consume(self, kw):
        pass

    def _requeue(self, kw):
        self.publisher_of_same_queue.publish(kw['body'])
