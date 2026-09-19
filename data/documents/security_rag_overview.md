# Security-aware RAG overview

Retrieval augmented generation combines a user query, retrieved documents, and an answer generator. Security evaluation should treat retrieved content as untrusted data and test for prompt injection, context manipulation, data leakage, and jailbreak attempts.

AegisRAG is a proposed security-aware research pipeline. Its demonstration security layer analyzes input and retrieved context with transparent rules before response generation and validation.
