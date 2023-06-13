from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator

class Entry(models.Model):
# User inputs integers from 0-10 and journal entry into provided text box.
    happiness = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10)])
    energy = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10)])
    hunger = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10)])
    calmness = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10)])
    health = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10)])
    journal = models.TextField()

    date_posted = models.DateTimeField(auto_now_add=True) # Automated date and time.
    author = models.CharField(max_length=15, default='Anonymous') # User input name.
    moodcolor = models.CharField(max_length=10, null=True) # Moodcolor field.

    # Calculation of mood colour! #
    @property
    def moodcolor(self):
        # Individual category ratings set by Author is summed and calculated its average.
        score = (self.happiness + self.energy + self.hunger + self.calmness + self.health)/5
        moodcolor = ''
        if score >= 0 and score < 2:
            moodcolor = 'Red'
        elif score >= 2 and score < 4:
            moodcolor = 'Orange'
        elif score >= 4 and score < 6:
            moodcolor = 'Yellow'
        elif score >= 6 and score < 8:
            moodcolor = 'Green'
        elif score >= 8 and score < 10:
            moodcolor = 'Blue'

        return moodcolor