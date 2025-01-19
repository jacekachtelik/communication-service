import toml


class Configuration:
    """
    Klasa Configuration odpowiada za zarządzanie konfiguracją aplikacji.
    """

    CONFIG_FILE = "config.toml"

    def __init__(self, config_path: str):

        self.__config = toml.load("{}/{}".format(config_path, self.CONFIG_FILE))

        self.__debug = self.__config["mode"]["debug"]
        self.__redis_host = self.__config["redis"]["host"]
        self.__redis_port = self.__config["redis"]["port"]
        self.__redis_password = self.__config["redis"]["password"]

    """
    Metoda zwracająca tryb debugowania.
    """

    def get_debug_mode(self):
        return self.__debug

    """
    Metoda zwracająca host Redis.
    """

    def get_redis_host(self):
        return self.__redis_host

    """
    Metoda zwracająca port Redis.
    """

    def get_redis_port(self):
        return self.__redis_port

    """
    Metoda zwracająca hasło Redis.
    """

    def get_redis_password(self):
        return self.__redis_password
