from app import app

@app.route('/')
@app.route('/index')
def index():
    return """Hello, World!<br>
              <br>
              Flask-sl4a created by Alexei Bushuev alexei@abushuev.ru<br>"""
