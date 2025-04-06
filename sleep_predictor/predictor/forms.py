from django import forms

class SleepForm(forms.Form):
    Age = forms.IntegerField()
    Gender = forms.ChoiceField(choices=[("Male", "Male"), ("Female", "Female")])
    BMI_Category = forms.ChoiceField(choices=[("Normal", "Normal"), ("Overweight", "Overweight"), ("Obese", "Obese")])
    Sleep_Duration = forms.FloatField()
    Physical_Activity_Level = forms.FloatField()
    Stress_Level = forms.IntegerField()
    Blood_Pressure = forms.CharField()
    Heart_Rate = forms.IntegerField()
    Daily_Steps = forms.IntegerField()
    Occupation = forms.CharField()
    Smoking_Status = forms.ChoiceField(choices=[("Yes", "Yes"), ("No", "No")])
