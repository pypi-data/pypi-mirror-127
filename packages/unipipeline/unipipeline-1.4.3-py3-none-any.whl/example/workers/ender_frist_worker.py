from unipipeline import UniWorker

from example.messages.ender_message import EnderMessage


class EnderFristWorker(UniWorker[EnderMessage, None]):
    def handle_message(self, message: EnderMessage) -> None:
        raise NotImplementedError('method handle_message must be specified for class "EnderFristWorker"')
