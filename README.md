# Empório da Música — AI Customer Support Agent

## Overview

This project is a functional AI-powered customer support prototype developed for the Artefact AI Engineer technical challenge.

The assistant helps customers find musical instruments, check product availability, view active promotions, understand store policies, and retrieve order information.

The application uses Google Gemini for natural-language understanding and function calling, Python for structured data retrieval, and Streamlit for the user interface.

## Technology Stack

- Python 3.10
- Google Gemini API (`google-genai`)
- Streamlit
- PyPDF
- Python CSV module
- Pytest
- Python Dotenv

## Architecture

The solution separates the conversational AI layer from deterministic business logic.

**User → Streamlit Chat → Gemini Agent → Python Tools → CSV/PDF Data → Customer Response**

The Gemini model selects the appropriate Python function according to the user's request.

Available tools:

- `find_products`: Searches the catalog by keyword, category, price and stock availability.
- `check_order`: Retrieves order information after matching the order ID and customer email.
- `list_promotions`: Retrieves active promotions and calculates discounted prices.

Store policies are extracted from a PDF document and provided as contextual reference material.

## Project Structure

```text
artefact-ai-engineer/
├── app/
│   ├── agent.py
│   ├── chat.py
│   ├── database.py
│   ├── orders.py
│   ├── policies.py
│   ├── promotions.py
│   └── tools.py
├── data/
├── tests/
│   └── test_tools.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

Clone the repository and create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Configuration

Create a `.env` file based on `.env.example`.

```dotenv
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-3.1-flash-lite
```

A valid Gemini API key is required to execute the conversational agent.

Never commit API keys or other credentials to version control.

## Dataset

The application uses the original CSV and PDF files supplied with the technical challenge.

The dataset contains products, categories, customers, orders, order items, promotions, and store policies.

The original challenge files are excluded from the public repository pending confirmation of redistribution permission.

To execute the application, place the original dataset files in the `data/` directory without changing their filenames.

## Run the Application

From the project root:

```bash
python -m streamlit run app/chat.py
```

Open the local URL displayed by Streamlit.

## Automated Tests

Run:

```bash
python -m pytest tests/ -v
```

Five tests passed during local development, covering product filtering, order verification, active promotions, and discount calculations.

## Engineering Decisions

**Function Calling:** The model uses Python functions instead of inventing structured business information.

**Deterministic Calculations:** Prices, stock quantities and promotional discounts are retrieved or calculated in Python.

**Multilingual Support:** The assistant is designed to respond in the customer's language while preserving the original Portuguese dataset.

**Error Handling:** Temporary model-service failures are handled without displaying internal stack traces to the customer.

**Data Protection:** Order lookups require a matching order ID and customer email. This is a simplified demonstration check and is not production-grade authentication.

## Limitations

- The application uses static datasets rather than live inventory or shipping systems.
- Email matching does not establish ownership of an email address.
- Generative responses may require additional validation against the source documents.
- API availability and rate limits depend on the selected model and provider.
- Product search relies partly on literal text matching and predefined category identifiers.
- The prototype does not support purchases, payments or order modifications.
- Production deployment would require authentication, authorization, monitoring and stronger security controls.

## Use of AI Development Tools

AI coding assistance was used to support implementation, debugging, technical documentation and test preparation.

The solution was developed incrementally, using local execution and automated tests to validate core business functions.

## Future Improvements

Potential improvements include automated evaluation of conversational responses, structured policy retrieval, stronger identity verification, request logging, improved search relevance and a production-ready deployment.

## Project Status

Functional prototype with locally validated business tools and initial Gemini function-calling integration. Further end-to-end evaluation is required before production use.
