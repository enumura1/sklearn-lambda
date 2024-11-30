import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json


# Calculate text similarity
def calculate_similarity(query, texts):
    vectorizer = TfidfVectorizer()

    # Vectorize query and reference text together
    all_texts = [query] + texts
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    
    # Calculate the cosine similarity between the query and each text
    similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    return similarities


def lambda_handler(event, context):
    try:
        # Get data from request body
        body = event['body']
        query = body.get('query', '')
        texts = body.get('texts', [])
        
        # Similarity calculation
        similarities = calculate_similarity(query, texts)
        
        # Create result
        results = [
            {'text': text, 'score': float(score)} 
            for text, score in zip(texts, similarities)
        ]
        
        # Get the most similar
        best_match = max(results, key=lambda x: x['score'])
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'results': results,
                'best_match': best_match
            }, ensure_ascii=False)
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }
