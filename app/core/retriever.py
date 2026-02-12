import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.config import TOP_K


class Retriever:

    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.matrix = None
        self.documents = []

    def rebuild_index(self):
        if not self.documents:
            self.matrix = None
            return
        corpus = [doc["text"] for doc in self.documents]
        self.matrix = self.vectorizer.fit_transform(corpus)

    def add_document(self, chunks, file_name):
        for i, chunk in enumerate(chunks):
            self.documents.append({
                "text": chunk,
                "file_name": file_name,
                "chunk_id": i
            })
        self.rebuild_index()

    def remove_document(self, file_name):
        self.documents = [
            doc for doc in self.documents
            if doc["file_name"] != file_name
        ]
        self.rebuild_index()

    def search(self, query):
        if self.matrix is None:
            return []

        query_vec = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vec, self.matrix)
        top_indices = np.argsort(similarities[0])[-TOP_K:][::-1]
        return [self.documents[i] for i in top_indices]


retriever = Retriever()
