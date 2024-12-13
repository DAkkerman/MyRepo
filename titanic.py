import pandas as pd
import streamlit as st
from PIL import Image

# Загружаем и отображаем изображение Титаника
image = Image.open('titaniс.jpg')
st.image(image, use_column_width=True)

# Загружаем данные
data = pd.read_csv('titaniс.csv')

# Создаем категории возраста
bins = [0, 30, 60, 100]
labels = ['Young', 'Middle-aged', 'Old']
data['AgeGroup'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)

# Выпадающее меню для выбора статуса выживших
survival_status = st.selectbox("Выберите статус выживших", ["Survived", "Not Survived"])

# Фильтруем данные на основе статуса выживших
if survival_status == "Survived":
    filtered_data = data[data['Survived'] == 1]
else:
    filtered_data = data[data['Survived'] == 0]

# Вычисляем показатели выживания для отфильтрованных данных
survival_rates = filtered_data.groupby('AgeGroup')['Survived'].count()

# Общее количество пассажиров в каждой возрастной группе, независимо от статуса выживших
total_passengers = data['AgeGroup'].value_counts()

# Вычисляем проценты
survival_percentages = (survival_rates / total_passengers) * 100

# Создаем DataFrame для результатов
results = pd.DataFrame({
    'Возрастная группа': survival_percentages.index,
    'Показатель выживания (%)': survival_percentages.values
})

# Отображаем результаты в таблице
st.table(results)