└─backend
    ├─api
    │  └─routes
    │          chat.py
    │
    ├─core
    │      config.py
    │
    ├─data
    │  ├─chunks
    │  ├─processed
    │  │  └─text
    │  └─raw
    │      └─pdf
    │              대학생을 위한 실용 금융_제4판 3쇄_금융감독원_(책갈피).pdf
    │              북브리프_돈의심리학.pdf
    │
    ├─docs
    │      a.text
    │
    └─service
        └─rag
            │  rag_pipeline.py
            │
            ├─components
            │  ├─embedding
            │  │      embedder.py
            │  │
            │  └─vectorstore
            │      └─faiss
            │              vector_store.py
            │
            ├─generation
            │      generator.py
            │
            ├─ingestion
            │      chunker.py
            │      index_builder.py
            │
            └─retrieval
                    retriever.py
