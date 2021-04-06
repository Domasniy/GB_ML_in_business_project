# python-flask-docker
Итоговый проект курса "Машинное обучение в бизнесе"

Стек:

ML: sklearn, pandas, numpy, xgboost
API: flask
Данные: с kaggle - https://www.kaggle.com/blastchar/telco-customer-churn

Задача: предсказать по признаком отток клиентов. Бинарная классификация

Используемые признаки:

Numerical:
- 'TotalCharges'
- 'MonthlyCharges'
- 'tenure'

Categorical:
'gender','SeniorCitizen', 'Partner', 'Dependents','PhoneService', 'MultipleLines', 'InternetService',
'OnlineSecurity', 'OnlineBackup', 'DeviceProtection','TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract',
'PaperlessBilling', 'PaymentMethod'

Преобразования признаков: OneHot

Модель: XGBoost

### Клонируем репозиторий и создаем образ
```
$ git clone https://github.com/fimochka-sudo/GB_docker_flask_example.git
$ cd GB_docker_flask_example
$ docker build -t fimochka/gb_docker_flask_example .
```

### Запускаем контейнер

Здесь Вам нужно создать каталог локально и сохранить туда предобученную модель (<your_local_path_to_pretrained_models> нужно заменить на полный путь к этому каталогу)
```
$ docker run -d -p 8180:8180 -p 8181:8181 -v <your_local_path_to_pretrained_models>:/app/app/models fimochka/gb_docker_flask_example
```

### Переходим на localhost:8181
