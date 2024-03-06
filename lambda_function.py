import json
import time
import os
import logging
from flask import Flask, jsonify, request
from flask_cors import CORS
import function_chat as fc
import function_chat_new as fcn
import psutil

app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/get_data": {"origins": "*"}})
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

@app.route('/get_data', methods=['POST'])
def lambda_handler():
    try:
        # Measure CPU usage
        start_time_cpu = time.time()
        cpu_usage_start = psutil.cpu_percent(interval=None)

        data = request.get_json()
        logger.debug(data)
        assistant_id = data.get('assistant_id',None)
        thread_id =  data.get('thread_id', None)
        user_input = data.get('user_input')
        graph_type = data.get('graph_type')
        print("user_input",user_input)

        # Call function_chat function
        response = fcn.function_chat(user_input, graph_type, assistant_id, thread_id)

        # Measure CPU usage again
        end_time_cpu = time.time()
        cpu_usage_end = psutil.cpu_percent(interval=None)
        total_time = end_time_cpu-start_time_cpu
        print("total time taken===================>",total_time)
        # Measure memory usage
        memory_usage = psutil.virtual_memory()

        # Log CPU and memory usage
        logger.debug("CPU Usage (start): {}%".format(cpu_usage_start))
        logger.debug("CPU Usage (end): {}%".format(cpu_usage_end))
        logger.debug("Memory Usage: {}".format(memory_usage))

        print("response to be rendered in UI",response)
        # Return response to the client
        return jsonify(response), 200
    except Exception as e:
        print("Error occurred: {}".format(str(e)))
        response = {"response": {"text": "Something went wrong. Please try again later."}}
        return jsonify(response), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
