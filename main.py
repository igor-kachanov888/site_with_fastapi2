# объявление import
from fastapi import FastAPI, Form, Request
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel

import uvicorn

from models.posts import add_post
import os
# инициализация
app = FastAPI()

# монтирование статической папки для обслуживания статических файлов
app.mount("/static", StaticFiles(directory="static"), name="static")

# экземпляр шаблона Jinja2 для возврата веб-страниц через шаблонизатор
templates = Jinja2Templates(directory="templates")


# класс  модели данных Pydantic
class Item(BaseModel):
    # language: str
    language = 'english'




# проверка isAlpha, метод GET, параметр запроса, возврат JSON
@app.get('/alpha')
async def alpha(text: str):
    result = {'text': text, 'is_alpha': text.isalpha()}

    return result


# создание нового пользователя, метод POST, поля формы, возврат JSON
@app.post('/create-user')
async def create_user(id: str = Form(...), name: str = Form(...)):
    # код для аутентификации, валидации, обновления базы данных

    data = {'id': id, 'name': name}
    result = {'status_code': '0', 'status_message': 'Success', 'data': data}

    return result





# обслуживание веб-страницы, метод GET, возврат HTML
@app.get('/', response_class=HTMLResponse)
async def get_webpage_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Contact Us"})

@app.get('/data_loader', response_class=HTMLResponse)
async def get_webpage_file_download(request: Request):
    return templates.TemplateResponse("file_download.html", {"request": request, "message": "Contact Us"})


@app.post("/download_file")
async def download_file(request: Request):  #, response_class=PlainTextResponse
    """
    for k, v in request.items():
        print("request", k, v)
    """
    form = await request.form()
    file = form["file"].file

    with file as temp:

        result = "\r\n".join([str(row) for row in temp])
        #print(f"{type(result)}, result = {result}")
    path = os.path.join(os.getcwd(), "data", "file.txt")
    with open(path, "w") as f:
        f.write(result)
    print(temp.__dict__, temp._file)
    add_post(content=result, user_id=0, title=str(request.client[0]))

    #return {"request": request, "message": "Download OK!"}



# ответ файла, метод GET, возврат файла как вложения
@app.get('/get-language-file/{language}')
async def get_language_file(language: str):
    file_name = "%s.json" % (language)
    file_path = "./static/language/" + file_name

    return FileResponse(path=file_path, headers={"Content-Disposition": "attachment; filename=" + file_name})


# main
if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)