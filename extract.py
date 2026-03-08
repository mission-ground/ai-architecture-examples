import fitz

def extract_korean_english_text(file_path):
    text_data = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            # 기본 추출 방식으로 한글과 영어 모두 유니코드로 정상 추출됨
            text_data += page.get_text("text") + "\n"
    return text_data

pdf_text = extract_korean_english_text("북브리프_돈의심리학.pdf")
print(pdf_text)

# 추출된 텍스트가 한국어로추출되지만 글자의 위치가 일부 불안정하게 나타남
