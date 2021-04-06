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
$ git clone https://github.com/Domasniy/GB_ML_in_business_project.git
$ cd GB_ML_in_business_project
$ docker build -t gbml/gb_docker_flask_churn .
```

### Запускаем контейнер

```
$ docker run -d -p 8020:8020 gbml/gb_docker_flask_churn
```

