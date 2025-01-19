import os


class Paths:
    """
    Klasa odpowiedzialna za zarządzanie ścieżkami do plików.
    """

    def __init__(self):

        self._root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self._etc = os.path.join("{}/../".format(self._root), "etc")

        pass

    """
    Metoda zwracająca ścieżkę do katalogu głównego aplikacji.
    """

    def get_root_path(self):
        return self._root

    """
    Metoda zwracająca ścieżkę do katalogu etc.
    """

    def get_etc_path(self):
        return self._etc
