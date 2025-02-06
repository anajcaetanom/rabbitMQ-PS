from abc import ABC, abstractmethod

class IPublisher(ABC):
    @abstractmethod
    def publish(self, exchange, message):
        """
        Publica uma mensagem a ser enviada para os consumidores.
        """
        pass

    @abstractmethod
    def close_connection(self):
        """
        Fecha a conexão com o RabbitMQ.
        """
        pass