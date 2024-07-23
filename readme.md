# activate virtual environment and install packages :
>>python -m venv venv
>>venv\Scripts\activate
>>python.exe -m pip install --upgrade pip
>>pip install poetry
>>poetry add wheel fastapi SQLAlchemy psutil schedule requests pydantic uvicorn selenium pymysql translate pandas pyperclip

- u can use pip instead of poetry by the command below :
>>pip install -r requirements.txt

# to run through uvicorn server implemented by fastapi :
>>cd app
- change host and port and then run the command (local host normally is  : host 127.0.0.1 port 8000):
>>python -m uvicorn main:app --reload --host 185.110.190.86 --port 5050 --no-use-colors
- or you can just do this :
>>python -m uvicorn main:app --reload --no-use-colors
- run fastapi swagger : (go to http://host:port/docs)
- if your localhost doesn't work go to : http://localhost:8000/docs or http://localhost:8080/docs

# to get your hostname :
- run the python code below using socket library :
>>socket.gethostbyname(socket.gethostname())
- usually port 5050 is a free port

# run crawler :
- open a new powershell and activate venv:
>>venv\Scripts\activate
- run crawler :
>>python crawler.py