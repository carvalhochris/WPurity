# Sanitise your WordPress posts for modern front-end development

This app provides a RESTful API for retrieving WordPress posts and sanitises them of HTML tags. The API endpoint returns data in JSON format and is built using Python 3, Django Rest Framework, and BeautifulSoup.

## Test with curl

```
curl -X GET 'https://wp-purity.herokuapp.com/wordpress/?wp_rest_endpoint=https://unlockyoursound.com/wp-json/wp/v2/posts'
```

Replace 'unlockyoursound.com' with your Wordpress domain

## Test with Postman

* Open Postman and create a new request.
* Set the request method to GET.
* Enter the following URL in the request URL field:
```
https://wp-purity.herokuapp.com/wordpress/
```
* Click on the Params button to add a new query parameter to the request and enter the following values:

| KEY | VALUE |
| --- | --- |
| wp_rest_endpoint | https://unlockyoursound.com/wp-json/wp/v2/posts |

* You might replace 'unlockyoursound.com' with your own Wordpress domain
* Click the Send button to send the request to the demo app's API endpoint.
* The response will be a list of JSON objects containing the sanitized list of posts from the https://unlockyoursound.com/wp-json/wp/v2/posts endpoint. Looking a little something like this:

```
[
    {
        "title": "DIY Diaries: Cheri Lyn",
        "slug": "cheri-lyn",
        "content": {
            "headings": [
                {
                    "tag": "h2",
                    "text": "What got you started in music?",
                    "paragraphs": [
                        "I was born into a family of musicians – both of my parents were successful musicians.",
                        "I have always been surrounded by music and business. My mom was a successful singer and for me, it was normal that she would do gigs on the weekends or invite her music friends over to our house, where we had many table music sessions.",
                        "For me therefore I think my path was already clear. I realised very early in my childhood how music can connect people. I could always feel what (live) music did to me.",
                        "Therefore, music has always been my anchor and I never doubted doing anything else."
                    ]
                },
            ]
        }
    },
]
```

## Use the Live API

Now that you have tested the API, you can now use it in your own frontend projects. 

### Example with React

[Live Demo](https://test-purity.vercel.app/)

```
import React, { useState, useEffect } from "react";

function Posts() {
  const [posts, setPosts] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(
        "https://wp-purity.herokuapp.com/wordpress/?wp_rest_endpoint=https://unlockyoursound.com/wp-json/wp/v2/posts?categories=322"
      );
      const data = await response.json();
      setPosts(data);
      setIsLoading(false); // set isLoading to false once data is fetched
    };
    fetchData();
  }, []);

  if (isLoading) {
    return (
      <div style={{ maxWidth: 500, margin: "0 auto" }}>Loading...</div>
    );
  }

  return (
    <div style={{ maxWidth: 500, margin: "0 auto" }}>
      {posts.map((post) => (
        <div key={post.slug}>
          <h2>{post.title}</h2>
          {post.content.headings.map((heading) => (
            <div key={heading.text}>
              <h3>{heading.text}</h3>
              {heading.paragraphs.map((paragraph) => (
                <p key={paragraph}>{paragraph}</p>
              ))}
            </div>
          ))}
          <br></br>
          <hr></hr>
        </div>
      ))}
    </div>
  );
}

export default Posts;
```

## Spin up your own instance

### Installation
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

This app was inspired by the [WordPress REST API](https://developer.wordpress.org/rest-api/) and [Django Rest Framework](https://www.django-rest-framework.org/).

## Issues

Any issues with this code should be reported in the Issues section of this repository.