import fitz

def extract_korean_english_text(file_path):
    text_data = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            # 기본 추출 방식으로 한글과 영어 모두 유니코드로 정상 추출됨
            text_data += page.get_text("text", sort = True) + "\n"
    return text_data

pdf_text = extract_korean_english_text("북브리프_돈의심리학.pdf")
# print(type(pdf_text.split("\n")))
# print(pdf_text)

# 추출된 텍스트가 한국어로추출되지만 글자의 위치가 일부 불안정하게 나타남

# https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 사용해서 임베딩 수행
from sentence_transformers import SentenceTransformer

documents = pdf_text.split("\n")
model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
embeddings = model.encode(documents)
print(type(embeddings) ,len(embeddings))

import chromadb

client = chromadb.PersistentClient(path="./my_vector_db")
collection = client.get_or_create_collection(name="money_psychology_docs")
ids = [f"doc_{i}" for i in range(len(documents))]

if collection.count() == 0:
    collection.add(
        documents=documents,
        embeddings=embeddings.tolist(), # numpy 배열을 파이썬 리스트로 변환
        ids=ids
    )
    print(f"총 {collection.count()}개의 데이터가 벡터 DB에 성공적으로 저장되었습니다!")
else:
    print(f"이미 {collection.count()}개의 데이터가 벡터 DB에 성공적으로 저장되었있습니다!")
    