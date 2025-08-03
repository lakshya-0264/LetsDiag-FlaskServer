# 💊 OTC Medicine Recommendation API for LetsDiag

This project implements a Flask-based API that recommends over-the-counter (OTC) medications based on user-provided symptoms. It leverages the Perplexity AI API for generating recommendations and the RxNav API (with a fallback to Wikipedia) for retrieving drug information. It also handles API key management and Cross-Origin Resource Sharing (CORS). This API simplifies the process of finding appropriate OTC medications by providing a convenient and accessible interface for symptom-based recommendations.

## 🚀 Features

- **Symptom-Based Recommendations:**  Recommends OTC medications based on user-provided symptoms using the Perplexity AI API.
- **Drug Information Retrieval:** Fetches drug information from the RxNav API and Wikipedia, providing users with essential details about the recommended medications.
- **API Key Management:** Securely manages the Perplexity AI API key using environment variables.
- **CORS Support:** Enables Cross-Origin Resource Sharing (CORS) to allow requests from different origins.
- **Fallback Mechanism:** Uses Wikipedia as a fallback for drug information when the RxNav API doesn't provide sufficient data.
- **Easy Integration:** Simple API endpoint (`/api/recommend`) for easy integration with external applications.

## 🛠️ Tech Stack

- **Backend:**
    - Python 3.x
    - Flask: Web framework for creating the API
    - Flask-CORS: For handling Cross-Origin Resource Sharing (CORS)
- **AI Model:**
    - Perplexity AI API: For generating medication recommendations
- **Data Source:**
    - RxNav API: For retrieving drug information
    - Wikipedia: As a fallback for drug information
- **Environment Management:**
    - `dotenv`: For loading environment variables from a `.env` file
- **Other:**
    - `os`: For accessing environment variables
    - `requests`: For making HTTP requests to external APIs (RxNav and Perplexity AI)
    - `json`: For handling JSON data

## 📦 Installation

### Prerequisites

- Python 3.x installed
- pip package manager
- A Perplexity AI API key

### Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  Create a virtual environment (recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  Set up environment variables:

    - Create a `.env` file in the root directory.
    - Add your Perplexity AI API key to the `.env` file:

      ```
      PERPLEXITY_API_KEY=YOUR_PERPLEXITY_API_KEY
      ```

### Running locally

1.  Run the Flask application:

    ```bash
    python app.py
    ```

2.  The API will be accessible at `http://127.0.0.1:5000`.

## 💻 Usage

To use the API, send a POST request to the `/api/recommend` endpoint with a JSON payload containing the `symptoms` field.

Example:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"symptoms": "headache, fever, cough"}' http://127.0.0.1:5000/api/recommend
```

The API will return a JSON response containing the recommended medications and their corresponding information.

```json
[
  {
    "medicine": "Acetaminophen",
    "link": "https://rxnav.nlm.nih.gov/REST/rxcui/161/related.json?rela=tradename_of"
  },
  {
    "medicine": "Ibuprofen",
    "link": "https://rxnav.nlm.nih.gov/REST/rxcui/6039/related.json?rela=tradename_of"
  }
]
```

## 📂 Project Structure

```
├── app.py               # Main Flask application file
├── requirements.txt     # List of Python dependencies
├── .env                 # Environment variables (API keys)
├── venv/                # Virtual environment directory (optional)
└── README.md            # Project documentation
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive commit messages.
4.  Push your changes to your fork.
5.  Submit a pull request.

## 📬 Contact

If you have any questions or suggestions, feel free to contact me at [your_email@example.com](mailto:your_email@example.com).

Thank you for checking out this project! I hope it's helpful. Your feedback and contributions are greatly appreciated.
