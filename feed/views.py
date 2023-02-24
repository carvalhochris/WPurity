from rest_framework import viewsets
from .serializers import WordPressSerializer
import requests
from rest_framework.response import Response


class WordPressViewSet(viewsets.ViewSet):
    def list(self, request):
        url = "https://unlockyoursound.com/wp-json/wp/v2/posts"

        try:
            # Make a GET request to your WordPress endpoint
            response = requests.get(url)

            # If the response was successful, serialize the data to pure JSON
            if response.status_code == 200:
                serializer = WordPressSerializer(response.json(), many=True)
                return Response(serializer.data)

        except requests.exceptions.RequestException as e:
            # If there was an error with the request, return a 500 error response
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)