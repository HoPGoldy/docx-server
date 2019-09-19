from flask import Flask, send_file
from urllib.parse import quote

from docxCreater.helloWorld.main import create as hello_world_create

app = Flask(__name__)

@app.route('/')
def download_file():
    file_stream = hello_world_create()
    filename = quote('helloWorld.docx')
    rv = send_file(file_stream, as_attachment=True, attachment_filename=filename)
    rv.headers['Content-Disposition'] += f'; filename*=utf-8''{filename}'
    return rv

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')