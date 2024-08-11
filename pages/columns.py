import streamlit as st


# Создаем три колонки
col1, col2, col3 = st.columns(3)

# Добавляем содержимое в каждую колонку
with col1:
    st.header("Колонка 1")
    st.write("Это содержимое первой колонки.")
    st.button("Кнопка 1")

with col2:
    st.header("Колонка 2")
    st.write("Здесь находится вторая колонка.")
    st.checkbox("Чекбокс")

with col3:
    st.header("Колонка 3")
    st.write("А это уже третья колонка.")
    st.selectbox("Выберите опцию", ["A", "B", "C"])

