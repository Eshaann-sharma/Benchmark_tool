import psutil
from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/benchmark')
def benchmark():
    num_runs = 5  # You can adjust the number of runs
    total_time = 0  # Placeholder for benchmark result

    for _ in range(num_runs):
        execution_time = perform_benchmark()
        total_time += execution_time

    average_time = total_time / num_runs
    return jsonify({"average_time": average_time})

def perform_benchmark():
    start_time = time.time()
    for _ in range(1000000):
        # Simulate some work (e.g., mathematical calculations)
        _ = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
    end_time = time.time()
    return end_time - start_time

@app.route('/system_info')
def system_info():
    cpu_info = {
        "CPU Count": psutil.cpu_count(logical=False),
        "CPU Threads": psutil.cpu_count(logical=True),
    }

    # Memory information
    memory_info = psutil.virtual_memory()
    memory_usage = {
        "Memory Usage (%)": memory_info.percent
    }

    return jsonify({"cpu_info": cpu_info, "memory_usage": memory_usage})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
