from django import forms

class mealplanform(forms.Form):
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        )
    
    atvt = (
    ('bmr', 'Basal Metabolic Rate (BMR)'),
    ('sedentary', 'Little or no exercise'),
    ('light', 'Sports 1-3 days/week'),
    ('moderate', 'Sports 3-5 days/week'),
    ('very', 'Sports 6-7 days a week'),
    )


    gender = forms.ChoiceField(choices = gender_choices)
    age = forms.IntegerField(max_value=100)
    weight = forms.FloatField(label = 'Weight (kg)',max_value=150)
    height = forms.FloatField(label = 'Height (cm)',max_value=200)
    activity = forms.ChoiceField(choices = atvt, label = 'Level of activity')

