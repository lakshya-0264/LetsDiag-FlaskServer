import os
import requests
import json
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS

load_dotenv()

API_KEY = os.environ.get("PERPLEXITY_API_KEY")
if not API_KEY:
    raise ValueError("API key not found. Please set the PERPLEXITY_API_KEY environment variable.")

API_URL = "https://api.perplexity.ai/chat/completions"


def get_medicine_info(medicine_name):
    """Fetch drug info from RxNav API; fallback to Wikipedia link if RxNav lacks info."""
    info = {
        "name": medicine_name,
        "link": f"https://en.wikipedia.org/wiki/{medicine_name.replace(' ', '_').capitalize()}"
    }

    try:
        # Step 1: Get RxCUI
        url = f"https://rxnav.nlm.nih.gov/REST/drugs.json?name={medicine_name}"
        resp = requests.get(url)
        if resp.status_code == 200:
            data = resp.json()
            concept_group = data['drugGroup'].get('conceptGroup', [])
            if concept_group:
                concept = concept_group[0]['conceptProperties'][0]
                info['name'] = concept.get("synonym", medicine_name)
                # The link remains the same; no description is fetched or stored
    except Exception as e:
        print(f"Error fetching info for {medicine_name}: {e}")

    return info



def recommend_medicine(symptoms):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    prompt = f"""For symptoms like '{symptoms}', list ONLY generic names of 2-3 common OTC medications. 
    Format: comma-separated names. No explanations. Example: 'paracetamol, ibuprofen'"""

    payload = {
        "model": "sonar",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(API_URL, json=payload, headers=headers)
    if response.status_code != 200:
        raise Exception(f"API request failed: {response.status_code} - {response.text}")

    try:
        response_data = response.json()
    except json.JSONDecodeError as e:
        raise Exception(f"Failed to parse JSON: {e}")

    raw_output = response_data['choices'][0]['message']['content'].strip()
    medicines = [m.strip().split('(')[0].strip() for m in raw_output.split(',')]
    return ', '.join(medicines[:3])

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    symptoms = data.get('symptoms', '')
    if not symptoms:
        return jsonify({"error": "No symptoms provided."}), 400
    try:
        medicines_str = recommend_medicine(symptoms)
        medicine_names = [m.strip() for m in medicines_str.split(',')]
        # Fetch details for each medicine
        medicines = [get_medicine_info(name) for name in medicine_names]
        return jsonify({"medicines": medicines})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
