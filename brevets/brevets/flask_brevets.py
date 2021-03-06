"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
from flask import Flask, redirect, request, render_template
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import config
import os 

import logging

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()
##app.secret_key = CONFIG.SECRET_KEY

#client = MongoClient("mongodb://admin:.mlab.com:/times)
#db = client.times



###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)
    bDist = request.args.get('bDist', type = float)
    bTime = request.args.get('bTime', type = float)
    bDate = request.args.get('bDate', type = float)
    
    
    app.logger.debug("km={}".format(km))
    app.logger.debug("request.args: {}".format(request.args))
    #Now takes correct distance/time
   
    open_time = acp_times.open_time(km, bDist, bTime)
    close_time = acp_times.close_time(km, bDist, bTime)
    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)

@app.route("/display", methods = ['POST'])
def display():
 
    ## insert into db 
    
##############

    app.debug = CONFIG.DEBUG    
    if app.debug:
        app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
