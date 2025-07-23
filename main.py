from flask import Flask, render_template, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = Flask(__name__)

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/inspire', methods=['POST'])
def inspire():
    try:
        prompt = "Give me a short and powerful motivational quote"
        response = model.generate_content(prompt)
        quote = response.text.strip()
        return jsonify({"quote": quote})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
