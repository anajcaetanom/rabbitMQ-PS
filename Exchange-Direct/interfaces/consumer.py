from abc import ABC, abstractmethod

class IConsumer(ABC):
    @abstractmethod
    def callback(self, ch, method, properties, body):
        """
        Método que será chamado quando uma mensagem for recebida.
        """
        pass

    @abstractmethod
    def consume(self, exchange):
        """
        Inicia o consumo de mensagens em uma fila temporária.
        """
        pass
    
    @abstractmethod
    def close_connection(self):
        """
        Fecha a conexão com o RabbitMQ.
        """
        pass