import os
from pprint import pprint as pp

import colorgram
from flask import Flask
from flask import render_template
app = Flask(__name__)

def get_filenames(f_dir, prefix='', suffix=''):
    """Get list of filenames within a directory. Optionally scope by prefix/suffix."""
    f_names = []
    for r,d,files in os.walk(f_dir):
        for f in files:
            if f.startswith(prefix) and f.endswith(suffix):
                f_names.append('{}/{}'.format(r, f))
    return f_names

def get_colors(num_cols=6):
    imgs = []
    for suffix in ['jpg', 'jpeg', 'png', 'gif']:
        for fname in get_filenames('static', suffix=suffix):
            colors = colorgram.extract(fname, num_cols)
            summary = []
            for color in colors:
                summary.append({
                    'rgb':tuple(color.rgb),
                    'hsl':tuple(color.hsl),
                    'percent':round(color.proportion * 100, 1)
                })
            imgs.append({
                'fname':fname,
                'colors':summary
            })
    return imgs

@app.route("/")
def home():
    imgs = get_colors()
    return render_template('color.html', imgs=imgs)

@app.route("/api")
def api_home():
    imgs = get_colors()
    return {'images':imgs}

@app.route("/<int:num_cols>")
def number_colors(num_cols):
    imgs = get_colors(num_cols)
    return render_template('color.html', imgs=imgs)
