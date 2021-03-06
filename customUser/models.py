from django.db import models

# Create your models here.

# 차 스펙 갖는 모델 작성해보기
class CarSpecs(models.Model):
    car_brand = models.CharField(max_length=50)
    car_model = models.CharField(max_length=100)
    production_year = models.CharField(max_length=10)
    car_body = models.CharField(max_length=50)
    engine_type = models.CharField(max_length=50)

    # 출력될 데이터 결정하기!
    # 구현되어있지 않으면 클래스이름 object (번호) 형식으로 출력된다!
    def __str__(self):
        return self.car_model
