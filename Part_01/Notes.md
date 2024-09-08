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