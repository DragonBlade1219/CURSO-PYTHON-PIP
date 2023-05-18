import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return [1,2,3]

@app.get("/contact", response_class = HTMLResponse)
def get_list():
    return """
            <h1> Hola, esta es la primera página web retornada por un código Back End con fast API </h1>
            <p> Soy su párrafo </p>
            """
    
# {"name": "Platzi"}

def run():
    store.get_categories()

if __name__=="__main__":
    run()