from flask import Flask, request
import pickle

app = Flask(__name__)

# Загрузка модели из файла
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/predict', methods=['POST'])
def predict():
    # Получаем входные данные о недвижимости из запроса
    data = request.get_json()  
    # Передаем данные в вашу модель для получения прогноза стоимости
    prediction = model.predict(data)
    # Возвращаем прогноз стоимости в ответ на запрос
    return {'prediction': prediction}


if __name__ == 'main':
    app.run()