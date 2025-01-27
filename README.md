# Sabi Boy 🤓

Sabi Boy is a Streamlit web app that helps users settle arguments by providing research-based or scientific answers. It integrates with **Semantic Scholar**, **PubMed**, **Google Scholar**, and **arXiv** to fetch real references and generate AI-powered responses using OpenAI's GPT model.

---

## Features

- **AI-Powered Answers**: Generates concise, research-based answers using OpenAI's GPT.
- **Real References**: Fetches research papers from:
  - **Semantic Scholar**: General research papers.
  - **PubMed**: Biomedical research papers.
  - **Google Scholar**: Broad academic research.
  - **arXiv**: Cutting-edge preprints in AI, physics, and more.
- **Caching**: Improves performance by caching API responses.
- **Error Handling**: Gracefully handles API errors and provides user-friendly messages.

---

## Installation

### Prerequisites

- Python 3.8 or higher.
- An OpenAI API key (sign up at [https://openai.com/](https://openai.com/)).

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/StMarkFx/sabi-boy.git
   cd sabi-boy
   ```

2. Install dependencies:
    ```bash
pip install -r requirements.txt
    ```

3. Set up environment variables:
    Create a .env file in the root directory and add your OpenAI API key:
        ```bash
        OPENAI_API_KEY=your_openai_api_key
        ```

4. Run the app:
    ```bash
    streamlit run app/main.py
    ```
5. Open your browser and navigate to the URL provided by Streamlit (usually http://localhost:8501).

## Usage

1. Enter Your Argument:
    Type your argument in the input box (e.g., "boys live longer than girls").
    Press Enter.

2. View the Response:
    Sabi Boy will generate a research-based answer using OpenAI's GPT.
    It will also fetch and display related research papers from Semantic Scholar, PubMed, Google Scholar, and arXiv.
    
3. Explore References:
    Click on the links to access the full research papers.

## Project Structure

sabi-boy/
├── app/                      # Main application code
│   ├── __init__.py
│   ├── main.py               # Streamlit app entry point
│   ├── api/                  # API integration modules
│   │   ├── __init__.py
│   │   ├── semantic_scholar.py
│   │   ├── pubmed.py
│   │   ├── google_scholar.py
│   │   └── arxiv.py
│   ├── utils/                # Utility functions
│   │   ├── __init__.py
│   │   ├── generate_response.py
│   │   ├── cache.py
│   │   └── error_handling.py
│   └── assets/               # Static assets (images, CSS, etc.)
│       └── logo.png
|
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (e.g., API keys)
├── .gitignore                # Files/folders to ignore in Git
└── README.md                 # Project documentation

## Contributing

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a new branch:

    ```bash
    git checkout -b feature/your-feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add your feature"
    ``` 
4. Push to the branch:
    ```bash
    git push origin feature/your-feature-name
    ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

 - **OpenAI:** For the GPT model powering the AI responses.
 - **Semantic Scholar:** For providing access to research papers.
 - **PubMed:** For biomedical research references.
 - **Google Scholar:** For broad academic research.
 - **arXiv:** For cutting-edge preprints.

## Contact

For questions or feedback, please contact:

 - **Your Name:** stmarkadebayo@gmail.com
 - **LinkedIn:** St. Mark Adebayo[https://www.linkedin.com/in/stmarkadebayo]
 - **GitHub:** github.com/StMarkFx