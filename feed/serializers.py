from rest_framework import serializers
from django.utils.html import strip_tags
from bs4 import BeautifulSoup

class WordPressSerializer(serializers.Serializer):
    title = serializers.CharField(source="title.rendered")
    slug = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()

    def get_content(self, obj):
    # Use BeautifulSoup to parse the WordPress HTML content
        soup = BeautifulSoup(obj['content']['rendered'], 'html.parser')

        # Initialize an empty list to store the JSON objects for each heading
        headings = []

        # Find all heading elements (h1, h2, h3, etc.) in the parsed HTML
        for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            # Create a JSON object for the heading with the tag and text attributes
            heading_json = {
                'tag': heading.name,
                'text': heading.get_text(strip=True),
                'paragraphs': []
            }

            # Find all paragraph elements following the current heading element
            next_element = heading.find_next_sibling()
            while next_element is not None and next_element.name not in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                # Extract the plain text from the paragraph element
                plain_text = next_element.get_text(strip=True)

                # Use strip_tags to remove any remaining HTML tags
                paragraph = strip_tags(plain_text)

                # Replace all instances of "\n" with an empty string
                paragraph = paragraph.replace("\n", " ")

                # Add the paragraph to the current heading's list of paragraphs
                heading_json['paragraphs'].append(paragraph)

                # Move to the next sibling element
                next_element = next_element.find_next_sibling()

            # Add the current heading to the list of headings
            headings.append(heading_json)

        # Create a JSON object for the content with the headings and paragraphs
        content_json = {
            'headings': headings
        }

        # Return the content JSON object
        return content_json



    def get_slug(self, obj):
        # Retrieve the slug value from the WordPress API response
        return obj['slug']


