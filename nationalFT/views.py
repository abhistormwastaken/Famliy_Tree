from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .internal import Driver

class FamilyTree(APIView):
    def get(self, request) -> Response:

        params = self.get_params(request)

        # some_json_data = {"data":"temp"}
        some_json_data = get_family_tree(params.get("name"), params.get("age"))

        return Response(some_json_data)

    @staticmethod
    def get_params(request) -> dict:
        params: dict = {k: v[0] for k, v in dict(request.query_params).items()}
        return params

def get_family_tree(name, age):
    return Driver(name,age)
    