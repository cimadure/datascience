'''This example demonstrates embedding a standalone Bokeh document
into a simple Flask application, with a call from OpenModelica.

To view the example, run:

    python simple.py

in this directory, and navigate to:

    http://localhost:XXXX  ( maybe 5000 ?! )

'''
from __future__ import print_function

import flask

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.util.string import encode_utf8


from OMPython import ModelicaSystem
import matplotlib.pyplot as plt


app = flask.Flask(__name__)

colors = {
    'Black': '#000000',
    'Red':   '#FF0000',
    'Green': '#00FF00',
    'Blue':  '#0000FF',
}


def getitem(obj, item, default):
    if item not in obj:
        return default
    else:
        return obj[item]


@app.route("/")
def polynomial():
    """ Very simple embedding of a polynomial chart

    """

    file = "BouncingBall.mo"

    package = "BouncingBall"
    mod = ModelicaSystem(file, package)

    # Grab the inputs arguments from the URL
    args = flask.request.args

    # Get all the form arguments in the url with defaults
    color = getitem(args, 'color', 'Black')
    _height = int(getitem(args, '_height', 1))
    _from = int(getitem(args, '_from', 0))
    to = int(getitem(args, 'to', 2))
    name = getitem(args, 'name', 'Ron.')

    #mod.setInputs(height=_height)
    mod.setParameters(height=_height, e=0.9)
    mod.setSimulationOptions(startTime=_from, stopTime=to, tolerance=1e-08)
    mod.simulate()

    time, height = mod.getSolutions("time", "h")

    # Create a polynomial line graph with those arguments
    fig = figure(title="Natural Fall")

    fig.line(time, height, color=colors[color], line_width=2)
    fig.xaxis.axis_label = 'time (s)'
    fig.yaxis.axis_label = 'height of falling (m)'
    resources = INLINE.render()

    script, div = components(fig)
    html = flask.render_template('index.html', plot_script=script, plot_div=div, resources=resources, color=color,
                                 _from=_from, to=to, _height=_height, name=name)
    return encode_utf8(html)


if __name__ == "__main__":
    print(__doc__)
    app.run(port=5001, debug=True)
