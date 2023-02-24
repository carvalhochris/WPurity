# WordPress API with Django Rest Framework

This app provides a RESTful API for retrieving WordPress posts using Django Rest Framework and sanitising them of HTML tags. The API endpoint returns data in JSON format and is built using Python 3.

## Installation

1. Clone the repository

```$ git clone https://github.com/carvalhochris/WPurity.git```

2. Create a virtual environment

```$ python3 -m venv env```

3. Activate the virtual environment

```$ source env/bin/activate```

4. Install the requirements

```$ pip install -r requirements.txt```

5. Run the server

```$ python manage.py runserver```

## Usage

### Retrieving WordPress Posts

To retrieve WordPress posts, make a GET request to the API endpoint:

`GET /wordpress/`

The response will be a list of JSON objects containing the post title and content.

<!-- ## Contributing

Contributions to this project are welcome. To contribute, follow these steps:

Fork the repository
Create a new branch (git checkout -b feature)
Commit your changes (git commit -am 'Add feature')
Push the branch (git push origin feature)
Create a Pull Request -->

## License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
This app was inspired by the [WordPress API](https://developer.wordpress.org/rest-api/) and [Django Rest Framework.](https://www.django-rest-framework.org/)

