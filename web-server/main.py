import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
# https://www.uvicorn.org/

#sintaxis que se conoce como decorador:
@app.get('/')
def get_list():
    return [1,2,3]
# https://fastapi.tiangolo.com/advanced/custom-response/?h=response+html
@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
        <h1>Hola soy una pagina</h1>
        <p>soy un parrafo</p>
    """


def run():
    store.get_categories()

if __name__ == '__main__':
    run()