from django import forms

class HeartForm(forms.Form):
    age = forms.IntegerField(label="Age", help_text="Age in years (e.g. 29–77)")
    sex = forms.ChoiceField(choices=[(1, "Male"), (0, "Female")], label="Sex", help_text="1 = Male, 0 = Female")
    cp = forms.ChoiceField(choices=[(0, "Typical Angina"), (1, "Atypical Angina"), (2, "Non-anginal Pain"), (3, "Asymptomatic")], label="Chest Pain Type", help_text="Type of chest pain")
    trestbps = forms.IntegerField(label="Resting BP", help_text="Resting blood pressure in mm Hg")
    chol = forms.IntegerField(label="Cholesterol", help_text="Serum cholesterol in mg/dl")
    fbs = forms.ChoiceField(choices=[(1, "True"), (0, "False")], label="Fasting Blood Sugar > 120", help_text="1 = True, 0 = False")
    restecg = forms.ChoiceField(choices=[(0, "Normal"), (1, "ST-T abnormality"), (2, "LV hypertrophy")], label="Rest ECG", help_text="Resting electrocardiographic results")
    thalach = forms.IntegerField(label="Max Heart Rate", help_text="Maximum heart rate achieved")
    exang = forms.ChoiceField(choices=[(1, "Yes"), (0, "No")], label="Exercise Induced Angina", help_text="1 = Yes, 0 = No")
    oldpeak = forms.FloatField(label="ST Depression", help_text="ST depression induced by exercise")
    slope = forms.ChoiceField(choices=[(0, "Upsloping"), (1, "Flat"), (2, "Downsloping")], label="Slope of ST", help_text="Slope of the peak exercise ST segment")
    ca = forms.ChoiceField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], label="Major Vessels Colored", help_text="Number of major vessels (0–3)")
    thal = forms.ChoiceField(choices=[(1, "Normal"), (2, "Fixed Defect"), (3, "Reversible Defect")], label="Thalassemia", help_text="Type of thalassemia")
