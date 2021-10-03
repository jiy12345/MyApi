from django.contrib import admin
from .models import CarSpecs # admin 패널에서 이용하기 위해 모델 가져오기

# Register your models here.
admin.site.register(CarSpecs) # admin 패널에 등록


