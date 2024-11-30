import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json


# テキストの類似度を計算
def calculate_similarity(query, texts):
    vectorizer = TfidfVectorizer()

    # クエリと参照テキストを一緒にベクトル化
    all_texts = [query] + texts
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    
    # クエリと各テキストのコサイン類似度を計算
    similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
    return similarities


def lambda_handler(event, context):
    try:
        # リクエストボディからデータを取得
        body = json.loads(event.get('body', '{}'))
        query = body.get('query', '')
        texts = body.get('texts', [])
        
        # 類似度計算
        similarities = calculate_similarity(query, texts)
        
        # 結果の作成
        results = [
            {'text': text, 'score': float(score)} 
            for text, score in zip(texts, similarities)
        ]
        
        # 最も類似度が高いものを取得
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
