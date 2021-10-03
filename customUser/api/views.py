# url에 따라 안내된 request들을 처리하기 위한 파일\

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

@api_view(['GET']) # 어떤 request 함수가 사용될 지 결정
@permission_classes([AllowAny]) # 모든 사람에게 허용하는 함수
def hello_world(request):
    return Response({"message": "Hello, world!"})