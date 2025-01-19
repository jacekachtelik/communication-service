from enviroment import paths
from configuration import configuration
from api import api_app, api_endpoints

paths = paths.Paths()
config = configuration.Configuration(paths.get_etc_path())


# Utworzenie instancji klasy ApiApp
api_app = api_app.ApiApp()

# Pobranie aplikacji FastAPI
app = api_app.get_app()

# Utworzenie instancji klasy ApiEndpoints
api_endpoints.ApiEndpoints(app)

# Uruchomienie aplikacji
api_app.run()
