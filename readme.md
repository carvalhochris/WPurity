# Sanitise your WordPress posts with Django Rest Framework

This app provides a RESTful API for retrieving WordPress posts using Django Rest Framework and sanitises them of HTML tags. The API endpoint returns data in JSON format and is built using Python 3.

## Live demo

```
https://wp-purity.herokuapp.com/wordpress/
```

## Example curl request

```
curl -X GET 'https://wp-purity.herokuapp.com/wordpress/?wp_rest_endpoint=https://unlockyoursound.com/wp-json/wp/v2/posts'
```

## Postman usage

* Open Postman and create a new request.
* Set the request method to GET.
* Enter the following URL in the request URL field:
```
https://wp-purity.herokuapp.com/wordpress/
```
* Click on the Params button to add a new query parameter to the request.
* Enter wp_rest_endpoint as the key and https://unlockyoursound.com/wp-json/wp/v2/posts as the value.
* Click the Send button to send the request to the demo app's API endpoint.
* The response will be a list of JSON objects containing the sanitized list of posts from the https://unlockyoursound.com/wp-json/wp/v2/posts endpoint.

Note that you'll need to replace https://unlockyoursound.com/wp-json/wp/v2/posts with the actual URL of the WordPress REST API endpoint you want to retrieve the sanitized list of posts from.

## Installation
Clone the repository

```
git clone https://github.com/carvalhochris/WPurity.git
```

Create a virtual environment

```
python3 -m venv env
```
Activate the virtual environment
```
source env/bin/activate
```
Install the requirements

```
pip install -r requirements.txt
```
Run the server
```
python manage.py runserver
```
## Local Usage

Retrieving WordPress Posts

To retrieve WordPress posts, make a GET request to the API endpoint with the wp_rest_endpoint query parameter set to the URL of the WordPress REST API endpoint you want to retrieve the sanitized list of posts from:

```
curl -X GET 'http://localhost:8000/wordpress/?wp_rest_endpoint=https://unlockyoursound.com/wp-json/wp/v2/posts'
```

Replace https://example.com/wp-json/wp/v2/posts with the actual URL of the WordPress REST API endpoint you want to retrieve the sanitized list of posts from.

The response will be a list of JSON objects containing the post title and content, with all HTML tags removed from the content.

## Contributing

Contributions to this project are welcome. To contribute, follow these steps:

* Fork the repository
* Create a new branch (git checkout -b feature)
* Commit your changes (git commit -am 'Add feature')
* Push the branch (git push origin feature)
* Create a Pull Request

## Acknowledgments

This app was inspired by the WordPress API and Django Rest Framework.

## Issues

Any issues with this code should be reported in the Issues section of this repository.