# Empório da Música — AI Customer Support Agent

**Artefact AI Engineer Technical Challenge**

A functional AI customer support prototype for a fictional musical instrument store, built with **Python, Google Gemini, Function Calling, and Streamlit**.

The assistant uses structured product, order, and promotion data, together with store policy documents, to answer customer questions.

Rather than relying only on the language model's internal knowledge, the application provides Python tools that retrieve relevant information from the available dataset.

## 1. Project Overview

The AI agent can:

- Search musical instruments by product name, category, and price.
- Recommend products using the available catalog.
- Report product prices and availability from CSV snapshots.
- Retrieve active promotions and discounted prices.
- Look up orders using an order ID and matching customer email.
- Answer store policy questions using the supplied reference material.
- Maintain conversational context across multiple messages.
- Respond in Portuguese or English.
- Handle certain API failures without exposing technical exceptions to customers.

The project is intended as a technical demonstration, not a production-ready e-commerce customer support system.

## 2. Technology Stack

| Component | Technology |
|---|---|
| Programming language | Python 3.10 |
| Generative AI | Google Gemini |
| AI integration | Google Gen AI SDK |
| Tool execution | Gemini Automatic Function Calling |
| User interface | Streamlit |
| Structured data | CSV files |
| Policy document processing | pypdf |
| Configuration | python-dotenv |
| Automated testing | pytest |
| Version control | Git and GitHub |

## 3. Architecture

The application follows a tool-based architecture that separates the language model from the data access and business logic layers.

```text
                         Customer
                            |
                            v
                    Streamlit Chat UI
                       app/chat.py
                            |
                            v
                    Gemini AI Agent
                      app/agent.py
                            |
               Automatic Function Calling
                            |
          +-----------------+------------------+
          |                 |                  |
          v                 v                  v
    Product Search      Order Lookup      Promotions
     app/tools.py       app/orders.py    app/promotions.py
          |                 |                  |
          +-----------------+------------------+
                            |
                            v
                       Data Layer
                    app/database.py
                            |
                            v
                      CSV Dataset

                    Policy Reference
                    app/policies.py
                            |
                            v
                   PDF or Demo Policy
```

### Request Processing

1. The customer sends a message through the Streamlit interface.
2. The agent receives the message and recent conversation history.
3. The system provides Gemini with behavioral instructions and relevant store policies.
4. Gemini determines whether a Python tool is required.
5. The selected tool queries the available CSV dataset.
6. The tool returns structured information.
7. Gemini uses the tool result to generate a customer-facing response.
8. Streamlit displays the response.

The application uses the Gemini SDK's automatic function-calling functionality to execute registered Python functions.

## 4. Agent Tools

Three tools are exposed to the language model.

### `find_products()`

Searches the musical instrument catalog using optional filters.

**Parameters:**

- `keyword`: product name or search term.
- `max_price`: maximum price in Brazilian reais.
- `category_id`: category identifier.
- `limit`: maximum number of returned products.

The underlying search function filters products according to the catalog's availability and status information.

**Example customer question:**

> Do you have acoustic guitars under R$ 1,000?

The agent can call `find_products()` to identify matching products.

### `check_order()`

Retrieves an order after checking two supplied fields:

- Order ID.
- Customer email associated with the order.

**Example conversation:**

Customer:

> Can you check order 100?

Assistant:

> Sure. Could you provide the email address associated with the order?

Customer:

> customer@example.com

The assistant can then call the order lookup tool using both values.

**Security limitation:** Matching an email address is not sufficient authentication for production use. This prototype demonstrates data matching only. A real system would require authenticated customer sessions or another secure verification mechanism.

### `list_promotions()`

Retrieves currently active promotions recorded in the dataset and calculates or returns their corresponding discounted prices.

**Example customer question:**

> What promotions are currently active?

The agent calls the promotion tool rather than inventing offers.

The data represents a snapshot and should not be interpreted as a live promotional system.

## 5. Project Structure

```text
artefact-ai-engineer/
|
|-- app/
|   |-- agent.py
|   |-- chat.py
|   |-- database.py
|   |-- orders.py
|   |-- policies.py
|   |-- promotions.py
|   `-- tools.py
|
|-- data/
|   `-- .gitkeep
|
|-- demo_data/
|   |-- desafio_tecnico_ai_eng - categories.csv
|   |-- desafio_tecnico_ai_eng - customers.csv
|   |-- desafio_tecnico_ai_eng - order_items.csv
|   |-- desafio_tecnico_ai_eng - orders.csv
|   |-- desafio_tecnico_ai_eng - products.csv
|   |-- desafio_tecnico_ai_eng - promotions.csv
|   `-- demo_policies.txt
|
|-- tests/
|   |-- test_demo.py
|   `-- test_tools.py
|
|-- .env.example
|-- .gitignore
|-- generate_demo.py
|-- pytest.ini
|-- requirements.txt
`-- README.md
```

## 6. Dataset Configuration

The application supports two modes:

- `demo`: a public, fictional dataset.
- `original`: the dataset supplied for the technical challenge.

The active mode is controlled by the `DATA_MODE` environment variable.

### 6.1 Demo Mode

Demo mode is the default configuration for public evaluation.

```dotenv
DATA_MODE=demo
```

The `demo_data/` directory includes:

| Data | Contents |
|---|---|
| Products | Four fictional musical instruments |
| Customers | One fictional customer |
| Orders | One fictional order |
| Order items | Items associated with the fictional order |
| Promotions | One active fictional promotion |
| Categories | Demonstration product categories |
| Policies | A fictional text document |

This dataset allows reviewers to run the application without access to the original challenge files.

The demonstration data can be regenerated using:

```bash
python generate_demo.py
```

### 6.2 Original Challenge Mode

To use the original challenge dataset:

```dotenv
DATA_MODE=original
```

Place the supplied CSV files and policy PDF in the local `data/` directory, preserving the filenames expected by the application.

The original files are intentionally excluded from this public repository because the supplied policy document is labeled for internal team use.

The application does not automatically download or reconstruct the original challenge dataset.

### 6.3 Data Limitations

The application works with static files.

Consequently:

- Stock information is not updated in real time.
- Orders are not synchronized with shipping providers.
- Promotions are evaluated using the available records.
- Product availability reflects the dataset snapshot.
- No real customer account authentication is implemented.

These limitations are intentional for the scope of the prototype.

## 7. Installation and Setup

### Prerequisites

- Python 3.10 or a compatible Python version.
- A Google Gemini API key.
- Git, if cloning the repository.

### Step 1 — Clone the Repository

```bash
git clone https://github.com/palomaventura-spec/artefact-ai-engineer.git
cd artefact-ai-engineer
```

### Step 2 — Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### Step 3 — Install Dependencies

```bash
python -m pip install -r requirements.txt
```

The project uses the following main dependencies:

- `google-genai`
- `streamlit`
- `pypdf`
- `python-dotenv`
- `pytest`

### Step 4 — Configure Environment Variables

Create a `.env` file in the project root.

You can copy `.env.example` and fill in your own API key:

```dotenv
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.5-flash-lite
DATA_MODE=demo
```

Choose a Gemini model available to your API account that supports function calling.

Model availability, quotas, pricing, and API behavior may change. The configured model should be verified against the current Google AI documentation.

**Never commit a real API key to the repository.**

### Step 5 — Run the Application

```bash
python -m streamlit run app/chat.py --server.port 8505
```

Open the application in your browser:

http://localhost:8505

The application will load the selected dataset and start the customer support interface.

## 8. Demonstration Scenarios

The public dataset contains fictional information designed for reproducible testing.

### Scenario 1 — Product Search

**Customer:**

> I'm looking for an acoustic guitar under R$ 1,000. What do you recommend?

**Expected behavior:**

The agent calls the product search tool and recommends matching products from the catalog.

The demo dataset includes:

- Demo Classic Guitar — R$ 599.90.
- Demo Acoustic Guitar — R$ 899.00.

The exact result depends on the search filters selected by the model.

### Scenario 2 — Promotions

**Customer:**

> What promotions are currently active?

**Expected behavior:**

The agent calls `list_promotions()`.

The demo dataset contains an active promotion for:

| Item | Value |
|---|---:|
| Product | Demo Acoustic Guitar |
| Original price | R$ 899.00 |
| Discount | 10% |
| Discounted price | R$ 809.10 |

The assistant should not combine this promotion with additional discounts unless explicitly supported by the data and store policies.

### Scenario 3 — Order Status

**Customer:**

> Can you check order number 100?

**Expected behavior:**

The assistant requests the email address if it has not already been provided.

**Customer:**

> customer@example.com

The agent can then call `check_order()`.

The fictional order contains:

- Order ID: `100`.
- Product: Demo Classic Guitar.
- Total: R$ 599.90.
- Status: Delivered.

### Scenario 4 — Policy Question

**Customer:**

> What is the return policy?

**Expected behavior:**

The agent uses the policy reference supplied in the selected dataset to answer the customer's question.

It should not invent additional deadlines, conditions, or legal exceptions.

### Scenario 5 — Invalid Order Verification

**Customer:**

> Can you check order 100 using another@example.com?

**Expected behavior:**

The order lookup tool should reject the unmatched combination.

The assistant should not disclose the order's contents or personal customer information.

These scenarios describe intended behavior. Actual model responses may vary and must be checked through interactive testing.

## 9. Automated Tests

The project includes automated tests for both dataset configurations.

### Public Demo Tests

Run:

```bash
python -m pytest -m demo -v
```

The four demonstration tests check:

1. Product dataset integrity.
2. Customer and order relationships.
3. Promotional price calculation.
4. Presence and basic structure of the demonstration policy document.

**Latest local result: 4 passed.**

These tests validate selected demonstration data conditions; they do not yet test every customer-facing tool in demo mode.

### Original Dataset Tests

With the original files available, configure:

```dotenv
DATA_MODE=original
```

Then run:

```bash
python -m pytest -m original -v
```

The five original dataset tests cover:

- Product filtering by category and price.
- Rejection of an unmatched customer email.
- Successful lookup with matching order information.
- Active promotion retrieval.
- Discount calculation.

**Latest local result: 5 passed.**

### Running the Default Test Suite

The repository's `pytest.ini` is configured to select public demo tests by default:

```bash
python -m pytest -v
```

The original dataset tests can be selected explicitly using `-m original`, provided the original files are available and the environment is configured accordingly.

### Testing Scope

The automated tests currently focus on the data and tool logic.

They do not fully validate:

- Model reasoning quality.
- Consistency across different model versions.
- Security against all prompt-injection attempts.
- Gemini service availability.
- End-to-end behavior under production traffic.

These areas would require additional evaluation and testing.

## 10. Prompt Engineering and Agent Behavior

The system prompt provides instructions designed to make the assistant more reliable.

Key principles include:

**Grounded answers**

The assistant is instructed to consult Python tools before providing product, order, or promotional details.

**No invented information**

The agent is instructed not to fabricate catalog entries, product availability, discounts, tracking events, or store policies.

**Order verification**

The assistant must obtain the order ID and associated email before attempting an order lookup.

**Context awareness**

Recent customer and assistant messages are provided to the model so it can follow multi-turn conversations.

**Language adaptation**

The agent attempts to identify whether the customer is communicating in Portuguese or English and replies in the corresponding language.

**Policy grounding**

Policy text is supplied as context to help the assistant answer store-related questions.

**Instructions versus data**

The prompt explicitly instructs the model to treat customer messages and retrieved documents as data rather than allowing them to override system-level behavior.

These instructions reduce some common risks but do not provide a formal guarantee against hallucinations or prompt injection.

## 11. Design Decisions and Trade-offs

### Why Gemini?

Gemini provides a generative AI interface with support for function calling, allowing the model to select and invoke Python functions.

This makes it possible to combine natural-language conversations with structured business data.

### Why Function Calling?

Directly asking a language model to remember product catalogs, order records, and promotions can lead to unsupported answers.

Function calling allows the model to request information from deterministic Python functions.

The business data remains in the data layer, rather than being treated as knowledge the model should invent.

### Why CSV Instead of a Database?

The challenge supplies structured CSV files.

For this prototype, reading them directly reduces setup complexity and allows the core business logic to be demonstrated without introducing a database server.

For production, a relational database and properly authenticated APIs would be more appropriate.

### Why Streamlit?

Streamlit provides a lightweight interface for demonstrating the conversational workflow.

It allows more time to be spent on the agent architecture, tool integration, and validation.

A production application could use a separate frontend and API backend.

### Why Include Demo Data?

The demonstration dataset makes the public repository runnable without distributing potentially restricted materials.

It also provides predictable records for evaluation and testing.

### Why Separate Business Logic From the Agent?

The tools are regular Python functions that can be tested independently of the language model.

This separation helps with:

- Testability.
- Debugging.
- Maintenance.
- Reproducibility.
- Future integration with other AI providers.

## 12. Safety, Security, and Privacy

This prototype includes several basic protections and explicit limitations.

### API Key Management

The Gemini API key is read from environment variables.

The real `.env` file is excluded from version control.

### Source Data

The original challenge dataset is not included in the public repository.

Public demonstration records are fictional.

### Order Information

The order lookup requires a matching order ID and email address.

This is a demonstration-level verification mechanism, not a replacement for secure authentication.

### Prompt Injection

The agent is instructed not to follow malicious instructions found in customer content or source material.

However, prompt-based defenses alone are not sufficient for a production security boundary.

### Model Reliability

The application may experience temporary errors caused by the external Gemini API.

The Streamlit interface handles certain API exceptions and displays a customer-friendly message.

### Production Security Requirements

A production version would require:

- Secure customer authentication and authorization.
- Protection against excessive requests and abuse.
- Appropriate logging and monitoring.
- Rate limiting.
- Secret management.
- Secure data storage.
- Personal data protection controls.
- Additional testing of prompt injection and data leakage.

## 13. Known Limitations

The current implementation has several limitations:

1. The catalog and order data are static snapshots.
2. There is no connection to a live payment or shipping service.
3. Email matching is not secure customer authentication.
4. Product search relies on structured field filtering rather than semantic vector search.
5. Language detection uses lightweight heuristics and is primarily designed for Portuguese and English.
6. Policies are supplied as reference text rather than retrieved from a vector database.
7. The assistant depends on the external Gemini API.
8. Automated tests do not yet provide complete end-to-end AI evaluation.
9. The Streamlit interface is intended for demonstration rather than production-scale deployment.

These limitations are documented to clarify the scope of the solution.

## 14. Future Improvements

If this prototype were developed further, the following improvements would be prioritized:

**1. Secure authentication**

Replace email matching with authenticated customer sessions.

**2. Database integration**

Move product, customer, order, and promotion records into a managed relational database.

**3. API-based data retrieval**

Connect the assistant to live inventory, order management, and shipping services.

**4. Retrieval-Augmented Generation**

Implement document retrieval with relevant passages, metadata, and source references for larger policy collections.

**5. Automated AI evaluations**

Build a set of repeatable conversational tests covering tool selection, factual correctness, multi-turn context, and policy compliance.

**6. Observability**

Record tool execution, latency, errors, model usage, and evaluation outcomes without exposing sensitive customer information.

**7. Stronger language handling**

Improve multilingual behavior using more robust language identification and evaluation.

**8. Deployment**

Package the application for reproducible deployment with appropriate security and configuration management.

## 15. Reproducibility

To reproduce the public demonstration:

```bash
git clone https://github.com/palomaventura-spec/artefact-ai-engineer.git

cd artefact-ai-engineer

python -m venv .venv

python -m pip install -r requirements.txt

python generate_demo.py

python -m pytest -m demo -v

python -m streamlit run app/chat.py --server.port 8505
```

Before starting the application, create a `.env` file with a valid Gemini API key and the demo configuration.

The demonstration data is included in the repository, so running the generator is optional unless the dataset needs to be recreated.

## 16. Project Summary

This project demonstrates the integration of a generative AI model with structured business data and Python tools.

The key technical objective is not simply to generate conversational responses, but to create an assistant that retrieves information from defined data sources and uses that information to support customer service interactions.

The implementation emphasizes:

- Tool-based AI architecture.
- Separation of model reasoning and business logic.
- Structured data integration.
- Multi-turn conversational context.
- Policy-grounded responses.
- Testable Python functions.
- Reproducible public demonstration data.
- Clear documentation of security and technical limitations.

The resulting prototype provides a foundation for a more complete AI-powered customer support application.

---

**Built for the Artefact AI Engineer Technical Challenge.**

**Repository:** https://github.com/palomaventura-spec/artefact-ai-engineer