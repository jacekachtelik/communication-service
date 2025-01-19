from fastapi import FastAPI, Request, HTTPException

from cloud_event_model import CloudEventModel


class ApiEndpoints:
    """
    Klasa ApiEndpoints zawiera definicje endpointów API.
    """

    def __init__(self, app: FastAPI):
        self.app = app
        self.events = {}

        @app.get("/", status_code=200)
        def hello():
            return {"Hello": "World"}

        """
        Metoda wysyłająca zdarzenie.
        :param request: Zdarzenie do wysłania.
        :return: Informacja o wysłaniu zdarzenia.
        """

        @app.post("/event/", status_code=201)
        async def send_event(request: Request):

            # TODO wywołanie metody zapisującej zdarzenie w bazie danych
            event_data = await request.json()
            print("Event Data otrzymane: ", event_data)
            event = CloudEventModel(**event_data)
            print("Event otrzymane: ", event)
            self.events[event.id] = event
            return {"message": "Event sent successfully"}

        """
        Metoda zwracająca zdarzenie.
        :param event_id: Identyfikator zdarzenia.
        :return: Zdarzenie.
        """

        @app.get("/event/{event_id}", status_code=200)
        async def get_event(event_id: str):
            if (event := self.events.get(event_id)) is None:
                print("Event not found")
                raise HTTPException(status_code=404, detail="Document not found")
            print("Event: ", event)
            return event

        """
        Metoda zwracająca wszystkie zdarzenia.
        :return: Zdarzenia.
        """
