from fastapi import FastAPI
import uvicorn


class ApiApp:
    """
    Klasa ApiApp implementuje aplikację FastAPI.
    """

    def __init__(self):
        self.app = FastAPI()

    """
    Metoda zwracająca aplikację FastAPI.
    """

    def get_app(self):
        return self.app

    """
    Metoda uruchamiająca aplikację FastAPI.
    """

    def run(self):
        uvicorn.run(self.app, host="127.0.0.1", port=8000)
