# document-analyzer/README.md

# AI Invoice/Document Analyzer

This project is an AI-powered Invoice and Document Analyzer web application built using Python. It leverages Optical Character Recognition (OCR) functionality with `pytesseract` and Natural Language Processing (NLP) techniques to extract and analyze information from documents.

## Project Structure

```
document-analyzer
├── src
│   ├── ocr
│   ├── ai
│   ├── utils
│   └── app.py
├── tests
├── requirements.txt
├── setup.py
├── .gitignore
└── README.md
```

## Setup Instructions

To set up the project, follow these steps:

1. Open your terminal.
2. Navigate to the project directory:
   ```
   cd path/to/document-analyzer
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the Streamlit application, execute the following command in your terminal:

```
streamlit run src/app.py
```

After running the command, open the provided local URL in your web browser to access the application.

## Usage

Once the application is running, you can upload documents for analysis. The application will extract text using OCR and analyze the content to identify important fields such as Vendor, Date, Invoice Number, and Total Amount.

## Dependencies

The project requires the following Python packages:

- `pytesseract`
- `streamlit`
- `pandas`
- `openpyxl`
- `nltk`
- `spacy`

## License

This project is licensed under the MIT License.