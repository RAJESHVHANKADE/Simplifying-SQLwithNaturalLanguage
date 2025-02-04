# Simplifying SQL with Natural Language

## Overview

This project implements a text-to-SQL system that allows users to interact with databases using natural language queries. It leverages transformer-based models like BERT and T5 to convert user queries into accurate SQL statements. The system is integrated with Flask/FastAPI for real-time query execution.

## Features

- Converts natural language queries into SQL statements.
- Built with transformer-based architectures like BERT and T5 for natural language understanding and SQL generation.
- Integrated with Flask/FastAPI for real-time query execution.
- Supports complex SQL queries and domain-specific use cases.
- Uses techniques like beam search and attention mechanisms to enhance performance and accuracy.
- Trained on the Spider dataset for a wide range of SQL queries.

## Installation

### Prerequisites

- Python 3.7+
- Flask or FastAPI
- PyTorch (for model implementation)
- Hugging Face Transformers library

### Steps

1. Clone this repository:

    ```bash
    git clone https://github.com/yourusername/simplifying-sql-with-nl.git
    cd simplifying-sql-with-nl
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the server:

    For Flask:

    ```bash
    python app.py
    ```

    For FastAPI:

    ```bash
    uvicorn app:app --reload
    ```

## Usage

1. Start the backend server (Flask or FastAPI).
2. Send a POST request to the `/query` endpoint with a natural language query:

    Example input:
    ```json
    {
      "query": "What is the total revenue for the last quarter?"
    }
    ```

3. The response will be the corresponding SQL query:
    ```sql
    SELECT SUM(revenue) FROM sales WHERE quarter = 'last' AND year = CURRENT_YEAR;
    ```

## Model Training

- The model is trained on the Spider dataset, which contains diverse SQL queries and schemas.
- Fine-tuned with domain-specific data to improve performance for complex queries.

## Technologies Used

- **Natural Language Processing (NLP)**: BERT, T5
- **Backend Frameworks**: Flask/FastAPI
- **Modeling Framework**: PyTorch, Hugging Face Transformers
- **Dataset**: Spider dataset

## Contributing

Feel free to open issues or submit pull requests. Contributions are always welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
