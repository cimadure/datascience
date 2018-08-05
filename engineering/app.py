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

app = flask.Flask(__name__)

COLORS = {
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


def simulate_system(mod, height, start_time, stop_time):
    mod.setParameters(height=height, e=0.9)
    mod.setSimulationOptions(startTime=start_time, stopTime=stop_time, tolerance=1e-08)
    mod.simulate()
    return mod.getSolutions("time", "h")


def draw_figure(time, height, color):
    fig = figure(title="Natural Fall")
    fig.line(time, height, color=color, line_width=2)
    fig.xaxis.axis_label = 'time (s)'
    fig.yaxis.axis_label = 'height of falling (m)'
    return fig


@app.route("/")
def boncing_ball():
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

    time, height = simulate_system(height=_height, start_time=_from, stop_time=to)

    # Create a figure of the result
    fig = draw_figure(time=time, height=height, color=COLORS[color])

    resources = INLINE.render()

    script, div = components(fig)
    html = flask.render_template('app.html', plot_script=script, plot_div=div, resources=resources, color=color,
                                 _from=_from, to=to, _height=_height, name=name)
    return encode_utf8(html)


if __name__ == "__main__":
    print(__doc__)
    app.run(port=5001, debug=True)
