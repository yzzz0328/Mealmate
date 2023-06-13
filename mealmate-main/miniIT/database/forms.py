from django import forms
from .models import foodinfo



class addfoodform(forms.ModelForm):

    class Meta:
        model = foodinfo

        # Fields to get user's input
        fields = [
            'name',
            'description',
            'mealtype',
            'calories',
            'carbs',
            'protein',
            'fat',
            'fibre',
            'size',
        ]
        
        # Styling add food form
        labels = {
            'name': 'Food Name:',
            'mealtype': "Meal Type",
            'calories': 'Calories (kcal) :',
            'carbs': 'Carbohydrates',
            'protein': 'Protein',
            'fat': 'Fat',
            'fibre': 'Fibre',
            'size': 'Size',
        }

        help_texts = {
            'calories': 'Click here to calculate the calories of your food.',
            'mealtype': 'Leave blank if it is an ingredient.',
            'carbs': 'grams',
            'protein': 'grams',
            'fat': 'grams',
            'fibre': 'grams',
            'size': 'grams',
        }

        error_messages = {

        }

        widgets = { 
            'name' : forms.TextInput(                            
                            attrs={
                                'class' : 'form-control', # Adds Crispy Form styling
                                "labels" : "Food Name:",
                                },
                             ),
        
            'description' : forms.Textarea(
                                attrs={
                                    'class': 'form-control',
                                    'placeholder' : "Tell us more about your food!",
                                    },
                                    ),

            'mealtype' : forms.Select(
                                attrs={
                                        'class': 'form-control',
                                    },
                                    ),

            'calories' : forms.NumberInput(
                                attrs={
                                        'class': 'form-control',
                                        'min': 0,
                                    },
                                    ),

            'carbs' : forms.NumberInput(
                                attrs={
                                        'class': 'form-control',
                                        'min': 0,
                                    },
                                    ),

            'protein' : forms.NumberInput(
                                attrs={
                                        'class': 'form-control',
                                        'min': 0,
                                    },
                                    ),

            'fat' : forms.NumberInput(
                                attrs={
                                        'class': 'form-control',
                                        'min': 0,
                                    },
                                    ),

            'fibre' : forms.NumberInput(
                                attrs={
                                        'class': 'form-control',
                                        'min': 0,
                                    },
                                    ),  

            'size' : forms.NumberInput(
                                attrs={
                                        'class': 'form-control',
                                        'min': 0,
                                    },
                                    ),  
        }
        

