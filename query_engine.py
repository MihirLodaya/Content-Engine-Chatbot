from sklearn.metrics.pairwise import cosine_similarity

def setup_query_engine(embeddings, pdf_texts):
    def query_engine(query_embedding):
        similarities = cosine_similarity(query_embedding, embeddings)
        top_indices = similarities.argsort()[0][-5:][::-1]
        top_texts = [pdf_texts[i] for i in top_indices]
        return similarities[0][top_indices], top_texts
    return query_engine
