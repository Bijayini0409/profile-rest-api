from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test API View"""
    def get(self, request, format=None):
        """Return a list of APIView Feauture"""

        an_apiview=[
            'Uses HTTP methods as function(get, post, patch, put,delete)',
            'Is similar to a traditional Djnago View',
            'Gives you the most control over your Application logic',
            'Is mapped manaually to URLs',
        ]

        return Response({'message':'Hello', 'an_apiview':an_apiview})
