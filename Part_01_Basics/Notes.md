## Search can be:- Text Search and Vector/Semantic Search
1. <b style="font-size:1.5em"> TEXT SEARCH:</b>
 Suppose we have a file containing several Q/A, and based on our query, we need the Answer from that data file.

     * Consider user asked the question=>  I just <span style="color:orange">discovered</span> the <span style="color:orange">course</span>, can I still <span style="color:orange">join</span> it?

     * Here the program will search the exact important keywords (highlighted ones) in the document, and will return the answer to the user.

    <span style="color:green; font-size:1.5em">Limitations:=> </span> If instead of <span style="color:orange">`join`</span>, user writes <span style="color:orange">`enroll`</span>, then in that case our program of text search will fail.

    <span style="color:green; font-size:1.5em">Text Search Techniques:=> </span> `CountVectorizer` and `TF-IDF`
<br>
<br>

2. <b style="font-size:1.5em"> VECTOR SEARCH EMBEDDINGS:</b> In this search, the semantics will be captured rather than the words i.e, unlike Text Search which when executed creates a large vector of words from the documents passed, here compression of large vector into small happen and small vector will be created and each value in that vector will resemble a semantic or a topic, so everything like synonyms, antonyms, etc will be captured. 

    * Suppose user asks=> I just <span style="color:orange">discovered</span> the <span style="color:orange">course</span>, can I still <span style="color:orange">join</span> it?

    * Here as semantic is captured, so if in all our documents only `join` word is there and if user mentions `enroll` in his question, then also it will be captured since join and enroll belong to the same semantics.  

    * <b style="color:orange">In this first Bag of Words are created and then it iscompressed to create embeddings.</b>

    <span style="color:green; font-size:1.5em">Problem with text:=> </span> - Text Search only concerns about exact matches of the terms, but not the synonyms. So, deal with semantics like synonyms, etc. we use Vector Search Embeddings.

    <span style="color:green; font-size:1.5em">Vector Search EMbedding Techniques:=> </span> `SVD`, `NMF`, `BERT`, etc.
<br>
<br>

3. <b style="font-size:1.5em"> What are Embeddings? </b>

    * <b>Conversion to Numbers:</b> Embeddings transform different words, sentences and documents into dense vectors (arrays with numbers) of semantics unlike sparse matrix in Text Search.

    * <b>Capturing Similarity:</b> They ensure similar items have similar numerical vectors, illustrating their closeness in terms of characteristics.

    * <b>Dimensionality Reduction:</b> Embeddings reduce complex characteristics (i.e., `Bag of Words` having high dimension) `into` vectors of semantics (Low dimension of `semantics or topics`).
    
    * <b>Use in Machine Learning:</b> These numerical vectors are used in machine learning models for tasks such as recommendations, text analysis,  text similarity and pattern recognition.
<br>
<br>

4. <b style="font-size:1.5em"> SVD (Singular Value Decomposition) </b>

    * Singular Value Decomposition is the simplest way to turn Bag-of-Words representation into embeddings.

    * This way we still don't preserve the word order (because it wasn't in the Bag-of-Words representation) but we reduce dimensionality and capture synonyms.

    * SVD "compresses" our input vectors in such a way that as much as possible of the original information is retained.

    * This compression is lossy compression - meaning that we won't be able to restore the 100% of the original vector, but the result is close enough.


5. <b style="font-size:1.5em"> Installation of Vector database: ElasticSearch </b>

    ```bash
    docker run -it \
        --rm \
        --name elasticsearch \
        -m 4GB \
        -p 9200:9200 \
        -p 9300:9300 \
        -e "discovery.type=single-node" \
        -e "xpack.security.enabled=false" \
        docker.elastic.co/elasticsearch/elasticsearch:8.4.3

    ```

6. <b style="font-size:1.5em"> When querying the ElasticSearch Vector DB, there are several options to be put in the `type` attribute that is present under `multi-match` key as can be seen from the <span style="color:green; font-size:1.5em">Query</span> syntax below:</b>

    ```python
    {
        "size": 5,
        "query": {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": query,
                        "fields": ["question^3", "text", "section"],
                        "type": "best_fields"
                    }
                },
                "filter": {
                    "term": {
                        "course": "data-engineering-zoomcamp"
                    }
                }
            }
        }
    }
    ```

    * The `multi_match` query is used to search for a given text across multiple fields in an Elasticsearch index.

       - It provides various types to control how the matching is executed and scored.

        - There are multiple types of multi_match queries:

            `best_fields`: Returns the highest score from any one field. <br>
            `most_fields`: Combines the scores from all fields. <br>
            `cross_fields`: Treats fields as one big field for scoring. <br>
            `phrase`: Searches for the query as an exact phrase. <br>
            `phrase_prefix`: Searches for the query as a prefix of a phrase. <br><br>

    *  <b style="color:green; font-size:1.5em"> 6.1. best_fields </b>
        - The `best_fields` type searches each field separately and returns the highest score from any one of the fields.

        - This type is useful when you want to find documents where at least one field matches the query well.

    *  <b style="color:green; font-size:1.5em"> 6.2. most_fields </b>
        - The `most_fields` type searches each field and combines the scores from all fields.

        - This is useful when the relevance of a document increases with more matching fields.

    *  <b style="color:green; font-size:1.5em"> 6.3. cross_fields </b>
        - The `cross_fields` type treats fields as though they were one big field.

        - It is suitable for cases where you have fields representing the same text in different ways, such as synonyms.

    *  <b style="color:green; font-size:1.5em"> 6.4. phrase </b>
        - The `phrase type` looks for the query as an exact phrase within the fields.

        - It is useful for exact match searches.

    *  <b style="color:green; font-size:1.5em"> 6.5. phrase_prefix </b>
        - The `phrase_prefix` type searches for documents that contain the query as a prefix of a phrase.

        - This is useful for autocomplete or typeahead functionality.