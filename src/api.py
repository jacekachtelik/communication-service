from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Document(BaseModel):
    id: str
    description: str
    url: str | None = None


documents = {}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/documents/", status_code=201)
def create_document(document: Document):

    documents[document.id] = document
    return {
        "document": "Document id: {} - {} created".format(
            document.id, document.description
        )
    }


@app.get("/documents/{document_id}")
def get_document(document_id: str):
    if (document := documents.get(document_id)) is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return documents[document_id]
