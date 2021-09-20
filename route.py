from flask import Flask, render_template, jsonify
from sqlalchemy import create_engine
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/test/<noc>/<inc>/<dob>/<dow>/<fam>/<job>/<others>')
def yes(noc, inc, dob, dow, fam, job, others):
    return(noc, inc)





if __name__ == "__main__":
    app.run(debug=True)