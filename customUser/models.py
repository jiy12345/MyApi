from django.db import models

# Create your models here.

# 차 스펙 갖는 모델 작성해보기
class CarSpecs(models.Model):
    car_brand = models.Charfield(max_length=50)
    car_model = models.CharField(max_length=100)
    production_year = models.CharField(max_length=10)
    car_body = models.CharField(max_length=50)
    engine_type = models.CharField(max_length=50)

    # 출력될 데이터 결정하기!
    def __str__(self):
        return self.car_brand
