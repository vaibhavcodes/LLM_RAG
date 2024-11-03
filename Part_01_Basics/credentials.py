class Credentials:
    def __init__(self):
        self.RAG_OPENAI_KEY="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"
        self.MISTRAL_KEY="rtcmWWJxlt0Fq84Z6qvhXQNu5JuSMgiX"
    def get_credential(self):
        cred = {"RAG_OPENAI_KEY": self.RAG_OPENAI_KEY,
                "MISTRAL_KEY": self.MISTRAL_KEY
                }

        return cred