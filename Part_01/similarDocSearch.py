import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class similarDocSearch:
    """
    A simple search document index using TF-IDF and cosine similarity for text fields and exact matching for keyword fields.

    Attributes:
        text_fields (list): List of text field names to index.
        vectorizers (dict): Dictionary of TfidfVectorizer instances i.e., cv for each text field.
        matrices (dict): Dictionary of TF-IDF matrices for each text field.
        documents (list): List of documents indexed.
    """

    # Constructor
    def __init__(self, text_fields):
        self.text_fields = text_fields
        self.matrices = {}
        self.vectorizers = {}
        self.documents = None
        self.documents_df = None

    # Training vectorizers on data
    def fit(self, documents):
        # Creating a dataframe out of documents which contains dictionary of 
        # {course_name, section, question, text} for every document
        self.documents = documents
        self.documents_df = pd.DataFrame(documents)
        for field in self.text_fields:
            # Vector creation
            cv = TfidfVectorizer(stop_words='english', min_df=3)
            # Weighted Matrix formation for the field
            X = cv.fit_transform(self.documents_df[field] )
            # Storing the vectorizer i.e, cv corresponding to the field
            self.vectorizers[field] = cv
            # Storing the weight matrix formed for the field
            self.matrices[field] = X
        return self

    # Function that will search and give the similar documents
    def search(self, query, boosts={}, filter_course="", num_results=10):
        # To store similarity score across all the fields
        sim_score = {}
        for field in self.text_fields:
            # Creating vector for the query for every field
            q = self.vectorizers[field].transform([query])
            # Weighted matrix corresponding to the field
            X = self.matrices[field]
            # Doing cosine similarity
            sim_score[field] = X.dot(q.T).toarray().flatten()

        # Summing all the similarity score across all the fields for every document
        # Considering the boosts parameter that tell us which field to give what weightage
        sim_score_result = 0
        for field in self.text_fields:
            sim_score_result += sim_score[field] * boosts.get(field, 1)
        
        # Creating a mask to get the result based on user provided prefernce of the field values
        reqd_mask = (self.documents_df['course']==filter_course).apply(int)

        # If we multiply both the reqd_mask and sim_score_result, All the required course 
        # rows will be multiplied by 1 and rest will be by 0
        resultant_sim_score = sim_score_result * reqd_mask

        # Checking which document has maximum sum of similarity score
        doc_index_similarity_order = np.argsort(resultant_sim_score)[::-1] # argsort return the o/p in ascending order so we have reversed using [::-1]
        
        # Getting top required number of documents similar to our query
        top_docs = [self.documents[i] for i in doc_index_similarity_order[:num_results]]
        return top_docs


