from django.shortcuts import render
from .forms import HeartForm
import joblib
import numpy as np
import os
from django.conf import settings
model_path = os.path.join(settings.BASE_DIR, 'predictor', 'ml_model', 'model.joblib')
model = joblib.load(model_path)

def predict(request):
    if request.method == "POST":
        form = HeartForm(request.POST)
        if form.is_valid():
            input_data = np.array([[
                form.cleaned_data["age"],
                int(form.cleaned_data["sex"]),
                form.cleaned_data["cp"],
                form.cleaned_data["trestbps"],
                form.cleaned_data["chol"],
                int(form.cleaned_data["fbs"]),
                form.cleaned_data["restecg"],
                form.cleaned_data["thalach"],
                int(form.cleaned_data["exang"]),
                form.cleaned_data["oldpeak"],
                form.cleaned_data["slope"],
                form.cleaned_data["ca"],
                form.cleaned_data["thal"]
            ]])
            prediction = model.predict_proba(input_data)[0][1] * 100  
            return render(request, "result.html", {"prediction": round(prediction, 2)})
    else:
        form = HeartForm()
    return render(request, "form.html", {"form": form})
