from bottle import default_app, route, template
import get_weather, requests


@route('/proj')
def chartproj():
    return template("proj")

application = default_app()
