Learning Flask....

app = Flask(__name__) creates app object/instance of Flass class

Using Decorators -> @app.route('/index') -> routes to index

HTML files should be placed inside the templates folder

They can be accessed using render_template('name.html')

HTML methods -> GET used to get things from the server -> POST used to post things to server

Jinja -> used to write code inside HTML - {{variables}} - {% for-if-else %} - {# Comments #}

redirect(url_for(view_name, args)) -> url_for creates url for the view_name with args to be passed to it, while redirect redirects to that url