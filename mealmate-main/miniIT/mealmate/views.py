from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from mealmate.forms import mealplanform
from database.models import foodinfo  # get foodinfo from database
import random


class mealplan(TemplateView):
    template_name = 'mealmate/mealplan.html'

    # get request to render form
    def get(self,request):
        form = mealplanform()
        args = {'form':form,'title':'MealPlanner'}
        return render(request, self.template_name, args)
    
    # receive data from mealplanform through post request
    def post(self,request):
        form = mealplanform(request.POST)
        if form.is_valid():
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            activity = form.cleaned_data['activity']

            # calculate the daily calorie needs
            if gender == 'M':
                BMR = 10 * weight + 6.25 * height - 5 * age + 5
            else: 
                BMR = 10 * weight + 6.25 * height - 5 * age + 5 -161

            if activity == 'bmr':
                calcountgoal = BMR
            elif activity == 'sedentary':
                calcountgoal = BMR*1.2
            elif activity == 'light':
                calcountgoal = BMR*1.375
            elif activity == 'moderate':
                calcountgoal = BMR*1.55
            elif activity == 'very':
                calcountgoal = BMR*1.725
                
            bf = [] # breatfast mealplan
            lc = [] # lunch mealplan
            dn = [] # dinner mealplan
            calcount = ""

            # when user click on generate button 
            if request.method =='POST' and 'generate' in request.POST:
                mealplan =[]
                calcount = 0 
                
                while calcount <= calcountgoal:
                    # random choose a meal from database 
                    n = random.randint(1,foodinfo.objects.all().count())
                    mealadd = foodinfo.objects.get(id=n)

                    # check whwther the chosen meal already exists in the mealplan
                    if mealadd in mealplan:
                        continue
                    else:
                        mealplan.append(mealadd)
                        cals = int(mealadd.calories)
                        calcount += cals

                        if mealadd.mealtype == 'Breakfast':
                            bf.append(mealadd)

                        elif mealadd.mealtype == 'Lunch':
                            lc.append(mealadd)

                        elif mealadd.mealtype == 'Dinner':
                            dn.append(mealadd)  

        args = {'form':form,'calcountgoal':calcountgoal,'title':'MealPlanner','bf':bf,'lc':lc,'dn':dn,'calcount':calcount}

        return render(request,self.template_name,args)
