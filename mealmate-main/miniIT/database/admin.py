from django.contrib import admin
from .models import foodinfo
from import_export.admin import ImportExportModelAdmin
# Register your models here.
# This can make the users import the csv file created by us to be imported to the database
@admin.register(foodinfo)
class Viewadmin(ImportExportModelAdmin):
    pass