from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, T5ForConditionalGeneration

app = FastAPI()

model_name = "IlyaGusev/rut5_base_sum_gazeta"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

class Article(BaseModel):
    text: str

@app.post("/summarize/")
async def summarize(article: Article):
    input_ids = tokenizer(
        [article.text],
        add_special_tokens=True,
        padding="max_length",
        truncation=True,
        max_length=400,
        return_tensors="pt"
    )["input_ids"]

    output_ids = model.generate(
        input_ids=input_ids,
        no_repeat_ngram_size=3,
        num_beams=5,
        early_stopping=True
    )[0]

    summary = tokenizer.decode(output_ids, skip_special_tokens=True)
    return {"summary": summary}
