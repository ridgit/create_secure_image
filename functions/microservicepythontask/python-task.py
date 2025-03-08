import os
import glob
import json
import shutil
import socket
import random
import subprocess
from flask_cors import CORS
from flask import Flask, request, render_template, jsonify

# This microservice accepts a POSTed JSON with the filenames and 
# the contents of one JSON file and one Python script.
# It executes the Python script and returns the jsonified output of it.

# POST:
# {
#     "datafile": "[The name of the JSON file]",
#     "data": "[The content of the JSON file]",
#     "codefile": "[The name of the Python file]",
#     "code": "[The content of the Python file]"
# }

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST","GET"])

def pythontask():
    # The current working directory
    cwd = os.getcwd()

    ### POST ###
    if request.method == "POST":
        os.chdir(cwd)

        # Create a randomly named temp_folder - avoiding any naming conflicts
        temp_folder = str(random.randint(1000000000,9999999999))
        os.makedirs(temp_folder)

        # Take the posted json data
        req = request.get_json()

        # Get and save the JSON file
        datafile = req["datafile"]
        data = req["data"]
        if not datafile == "":
            df = open("{}/{}".format(temp_folder, datafile), "w+")
            df.write(data)
            df.close()

        # Get and save the Python script
        codefile = req["codefile"]
        code = req["code"]
        if codefile.endswith(".py") and len(codefile) > 3:
            cf = open("{}/{}".format(temp_folder, codefile), "w+")
            cf.write(code)
            cf.close()
        else:
            # Remove temp_folder
            shutil.rmtree(temp_folder)
            return jsonify(output="Please enter a proper code filename ending with '.py'")

        src = os.getcwd() + '/thirdPartyPackages'

        # Enter temp_files directory and execute code file
        os.chdir(temp_folder)

        # Create symlink to third party packages

        dst = os.getcwd() + '/thirdPartyPackages'
        os.symlink(src, dst)
        
        # Try to run the code with subprocess (python3)
        try:
            process = subprocess.check_output(
                ["python3", codefile],
                stderr=subprocess.STDOUT,
                universal_newlines=True)
        # Check for error message
        except subprocess.CalledProcessError as e:
            # Leave temp_folder
            os.chdir(cwd)
            # Remove temp_folder
            shutil.rmtree(temp_folder)
            
            return jsonify(output=e.output)

        else:
            # If run successfully
            # Leave temp_folder
            os.chdir(cwd)
            # Remove temp_folder
            shutil.rmtree(temp_folder)
            # Return the output
            return jsonify(output=process.rstrip())

    ### GET ###
    else:
        os.chdir(cwd)
        # Render the native interface to communicate with the microservice
        return render_template("python-task.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=50000, debug=True)
