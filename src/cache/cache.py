from abc import ABC, abstractmethod


class Cache(ABC):
    """
    Klasa Cache jest abstrakcyjną klasą bazową (ABC) dla implementacji pamięci podręcznej.

    Metody abstrakcyjne:
    - get(key): Pobiera wartość z pamięci podręcznej na podstawie klucza.
    - set(key, value): Ustawia wartość w pamięci podręcznej dla danego klucza.

    Każda klasa dziedzicząca po Cache musi zaimplementować te metody.
    """

    """
    Metoda get(key) jest abstrakcyjna, więc musi być zaimplementowana w klasie dziedziczącej.
    Pobiera wartość z pamięci podręcznej na podstawie klucza.
    
    :param key: Klucz, dla którego ma zostać pobrana wartość z pamięci podręcznej.
    :return: Wartość z pamięci podręcznej na podstawie kl
    """

    @abstractmethod
    def get(self, key):
        pass

    """
    Metoda set(key, value) jest abstrakcyjna, więc musi być zaimplementowana w klasie dziedziczącej.
    Ustawia wartość w pamięci podręcznej dla danego klucza.
    """

    @abstractmethod
    def set(self, key, value):
        pass
