# News-API

### Description

A simple web application built with Flask that displays news and updates feeds sourced from [NewsApi](https://newsapi.org/)

### Technologies Used

- Python
- Flask

### Prerequisites
- git
- Package manager - pip
- Environment manager - virtual env

### Setup Instructions and Installation
- In your preferred location in your file system, create a virtual environment and activate it
- Launch your terminal and paste the following command: `git clone https://github.com/BrianMwevi/news-flash.git`
- Change directory to news-flash `cd news-flash`
- Open the project with your preferred IDE and run the following command in the terminal: `pip install -r requirements.txt`
- Go to [NewsApi](https://newsapi.org/) and generate an API Key for your application
- create a file named `start.py` in the root of your application and change it's permissions: `chmod a+x start.py`
- Create two variables in the start.py file:
    >>> `export NEWS_API_KEY='your apikey'` <br>
    >>> `export SECRET_KEY='your secret key'`
- Run the application by typing the following in the terminal: `./start.py`

### User Stories
<ul>
  <li>The user is able to see various news sources on the homepage of the application.</li>
  <li>The user is also able to select a news source and see all news articles from the selected news source in the application.</li>
  <li>The user is able to see the image, description and the time a news article was created.</li>
  <li>The user is to click on an article and read the full article on the source website.</li>
 </ul>

### Known Bugs

No known bugs.


### License

_MIT Licence_
Copyright (c) 2022 **Ian Sang**<br>
Email: ianosang18@gmail.com<br>
[Read More](https://github.com/IanoSang/News-API/blob/main/LICENSE)


[Go Back To Top](#F-news)
