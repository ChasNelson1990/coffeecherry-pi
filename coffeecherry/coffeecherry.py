from flask import Flask

# import blueprints
import sys
import os
[sys.path.append(os.path.join("/home/pi/coffeecherry-pi",d)) for d in os.listdir("/home/pi/coffeecherry-pi/") if os.path.isdir(os.path.join("/home/pi/coffeecherry-pi",d))]
from smart import smart_ssr
from tank import tank
from pid import new_pid

app = Flask(__name__)

brew = new_pid(17, 100)
steam = new_pid(22, 150)

# register blueprints - comment out those not needed
app.register_blueprint(smart_ssr, url_prefix='/manual')
app.register_blueprint(tank, url_prefix='/tank')
app.register_blueprint(brew, url_prefix='/brew')
app.register_blueprint(steam, url_prefix='/steam')

@app.route('/')
def index():
    return 'true'
