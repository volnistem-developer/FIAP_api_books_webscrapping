from abc import ABC, abstractmethod


class IServiceRole(ABC):
    @abstractmethod
    def list(self):
        pass
