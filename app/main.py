# uvicorn main:app

from fastapi import FastAPI, Request, Form
from fastapi.responses import FileResponse, RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
import random
import json


app = FastAPI()
templates = Jinja2Templates(directory="public")

@app.get('/')
async def main_view():
    return FileResponse("public/index.html")

# редирект по сгенерированному адресу
@app.get('/{link}')
async def redirect(link:str):

    url_arr = open_Json()     
    for j in url_arr: 
        if url_arr[j].split('/')[-1] == link:
            return RedirectResponse(j)
        else:
            return RedirectResponse('/')

# Генерация страницы
@app.post("/", response_class=HTMLResponse)
async def get_url(request: Request, url: str = Form()):
    return templates.TemplateResponse("res.html", {"request": request, "url": generate_url(url)})

def open_Json():
    with open('urls.json') as j:
        url_arr = json.load(j)
        return url_arr

def generate_url(url):

    # Проверка на сущестующий URL
    url_arr = open_Json()
    for j in url_arr:
        if j == url:
            return url_arr[j]
    old_url = url

    # генерация уникального адреса
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    link=''

    for i in range(5):
        link += random.choice(chars)
    new_url = f"http://localhost:8000/{link}"

    # запись в файл
    url_arr = open_Json()
    url_arr[old_url] = new_url

    with open('urls.json', 'w') as j:
        json.dump(url_arr, j)

    return new_url


