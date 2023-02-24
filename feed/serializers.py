from rest_framework import serializers
from django.utils.html import strip_tags
from bs4 import BeautifulSoup

class WordPressSerializer(serializers.Serializer):
    title = serializers.CharField(source="title.rendered")
    content = serializers.SerializerMethodField()

    def get_content(self, obj):
    # Use BeautifulSoup to parse the WordPress HTML content
        soup = BeautifulSoup(obj['content']['rendered'], 'html.parser')

        # Extract the plain text from the parsed HTML
        plain_text = soup.get_text()

        # Use strip_tags to remove any remaining HTML tags
        content = strip_tags(plain_text)

        # Replace all instances of "\n" with an empty string
        content = content.replace("\n", " ")

        # Return the sanitized content
        return content

