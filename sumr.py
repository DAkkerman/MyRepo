# Убедитесь, что все необходимые библиотеки установлены
# !pip install transformers sentencepiece datasets

from transformers import AutoTokenizer, T5ForConditionalGeneration

model_name = "IlyaGusev/rut5_base_sum_gazeta"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

article_text = "Высота башни составляет 324 метра (1063 фута), примерно такая же высота, как у 81-этажного здания, и самое высокое сооружение в Париже. Его основание квадратно, размером 125 метров (410 футов) с любой стороны. Во время строительства Эйфелева башня превзошла монумент Вашингтона, став самым высоким искусственным сооружением в мире, и этот титул она удерживала в течение 41 года до завершения строительство здания Крайслер в Нью-Йорке в 1930 году. Это первое сооружение которое достигло высоты 300 метров. Из-за добавления вещательной антенны на вершине башни в 1957 году она сейчас выше здания Крайслер на 5,2 метра (17 футов). За исключением передатчиков, Эйфелева башня является второй самой высокой отдельно стоящей структурой во Франции после виадука Мийо."

input_ids = tokenizer(
[article_text],
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
print(summary)