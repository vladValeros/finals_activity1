# Django Sleep Disorder Predictor

A web-based machine learning app using Django and scikit-learn that predicts potential sleep disorders based on user health and lifestyle inputs. Built for CC105 Final Laboratory Requirement.

The app uses a trained Random Forest Classifier model to make predictions based on user inputs through a Bootstrap-styled form interface.

## Features

✔ Django-powered form for user input
✔ Random Forest machine learning model for prediction
✔ Pandas preprocessing with one-hot encoding
✔ Automatic feature alignment with model input
✔ Bootstrap-styled UI for better user experience

## Prerequisites
Ensure you have the following installed:
- **Python** 3.13.1
- **Django** 5.1.7
- **pandas** 2.2.2
- **scikit-learn** 1.5.0
- **joblib** 1.4.2

## Setup Instructions

### 1. Clone the Repository
```sh
git clone https://github.com/your-username/sleep-predictor.git
cd sleep-predictor
```

### 2. Create a Virtual Environment and Install Dependencies
```sh
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On Mac/Linux

pip install django pandas scikit-learn joblib
```

### 3. Train the Machine Learning Model (Optional)
The repository includes a script `train_model.py` that:
- Loads `Sleep_health_and_lifestyle_dataset.csv`
- Drops nulls and encodes data
- Trains a Random Forest model
- Saves the model as `sleep_model.joblib`

```sh
python train_model.py
```
> Make sure `Sleep_health_and_lifestyle_dataset.csv` is in the project root directory before running.

### 4. Project Structure
```
sleep_predictor/
├── manage.py
├── train_model.py
├── Sleep_health_and_lifestyle_dataset.csv
├── sleep_model.joblib         # (Copy this here manually after training)
├── sleep_predictor/
│   └── settings.py ...
├── predictor/
│   ├── forms.py
│   ├── views.py
│   ├── templates/
│   │   └── predictor/
│   │       └── predict.html
│   └── urls.py
```

### 5. Run Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### 6. Start the Development Server
```sh
python manage.py runserver
```
Visit http://127.0.0.1:8000/predict/ to test the form and prediction.

---
