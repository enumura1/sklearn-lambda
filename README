# Text Similarity Calculator with AWS Lambda

This project implements a text similarity calculator using scikit-learn, deployed as an AWS Lambda function via Docker container.

# Overview

Calculates text similarity using TF-IDF and cosine similarity
Deployed as a containerized Lambda function
Returns similarity scores and best matching text

# Project Structure

```
text-similarity/
├── Dockerfile
├── app.py
└── README.md
```

# Example

- request

```
{
  "body": {
    "query": "How is the weather forecast for this weekend?",
    "texts": [
      "This weekend will be sunny with high temperatures.",
      "Next week will be rainy due to low pressure.",
      "Saturday will be clear and comfortable."
    ]
  }
}
```

- response

```
{
  "statusCode": 200,
  "body": {
    "results": [
      {
        "text": "This weekend will be sunny with high temperatures.",
        "score": 0.2393
      },
      {
        "text": "Next week will be rainy due to low pressure.",
        "score": 0.0
      },
      {
        "text": "Saturday will be clear and comfortable.",
        "score": 0.1213
      }
    ],
    "best_match": {
      "text": "This weekend will be sunny with high temperatures.",
      "score": 0.2393
    }
  }
}
```
