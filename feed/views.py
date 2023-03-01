from rest_framework import viewsets
from .serializers import WordPressSerializer
import requests
from rest_framework.response import Response


class WordPressViewSet(viewsets.ViewSet):
    def list(self, request):
        # Retrieve the WordPress REST API endpoint URL from the request query parameters
        url = request.query_params.get('wp_rest_endpoint')

        if not url:
            # If the 'wp_rest_endpoint' query parameter is not provided, return a 400 error response
            return Response({'error': 'Missing wp_rest_endpoint query parameter'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Make a GET request to the specified WordPress endpoint URL
            response = requests.get(url)

            # If the response was successful, serialize the data to pure JSON
            if response.status_code == 200:
                serializer = WordPressSerializer(response.json(), many=True)
                return Response(serializer.data)

        except requests.exceptions.RequestException as e:
            # If there was an error with the request, return a 500 error response
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
