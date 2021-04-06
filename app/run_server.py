# USAGE
# Start the server:
# 	python run_front_server.py
# Submit a request via Python:
#	python simple_request.py

# import the necessary packages
import dill
import pandas as pd
import os
dill._dill._reverse_typemap['ClassType'] = type
#import cloudpickle
from flask import Flask, jsonify, request

import logging
from logging.handlers import RotatingFileHandler
from time import strftime

# initialize our Flask application and the model
app = Flask(__name__)
model = None

handler = RotatingFileHandler(filename='app.log', maxBytes=100000, backupCount=10)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

def load_model(model_path):
	# load the pre-trained model
	global model
	with open(model_path, 'rb') as f:
		model = dill.load(f)
	print(model)

modelpath = "/app/app/models/xgb_pipeline.dill"
load_model(modelpath)

@app.route("/", methods=["GET"])
def general():
	return """Welcome to Telco churn prediction process. Please use 'http://<address>/predict' to POST"""

@app.route("/predict", methods=["POST"])
def predict():
	try:
		test_json = request.get_json()
		test = pd.read_json(test_json, orient='records')

	except Exception as e:
		raise e


	if test.empty:
		return (bad_request())
	else:

		print("doing predictions now...")
		preds = model.predict_proba(test)
		print(preds)
		data = {'predictions' : preds.tolist()}
		print(type(data['predictions']))
		#prediction_series = list(pd.Series(preds))

		#final_predictions = pd.DataFrame(prediction_series)

		responses = jsonify(data)
		responses.status_code = 200

		return responses


# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
	print(("* Loading the model and Flask starting server..."
		"please wait until server has fully started"))
	port = int(os.environ.get('PORT', 8020))
	app.run(host='0.0.0.0', debug=True, port=port)
