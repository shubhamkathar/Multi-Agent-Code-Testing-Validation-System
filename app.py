from flask import Flask, request, jsonify
from crew_setup import run_crew

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json

    code = data.get("code")

    result = run_crew(code)

    return jsonify({
        "status": "success",
        "result": str(result)
    })

if __name__ == "__main__":
    app.run(debug=True)
