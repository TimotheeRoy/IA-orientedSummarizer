from summarizeTxt import query
from readTxt import extract_text_from_pdf

txt = extract_text_from_pdf('manteau.pdf', [4,58])

print(
    query({"inputs" :
        f"{txt}"})
)