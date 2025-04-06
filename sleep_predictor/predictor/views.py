from django.shortcuts import render
from .forms import SleepForm
import joblib
import pandas as pd

model = joblib.load('sleep_model.joblib')

def predict_sleep_disorder(request):
    prediction = None
    if request.method == 'POST':
        form = SleepForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            df = pd.DataFrame([data])
            df = pd.get_dummies(df)
            df = df.reindex(columns=model.feature_names_in_, fill_value=0)
            prediction = model.predict(df)[0]
    else:
        form = SleepForm()
    return render(request, 'predictor/predict.html', {'form': form, 'prediction': prediction})
