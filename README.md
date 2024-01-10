# Book Crawler

Welcome to the book crawler repository!

## Instalation

Follow these steps to set up and run the project on your local machine:

**Install Python 3.10+**

**Create a Virtual Environment:**

```sh
 python3 -m venv venv
```

**Activate the Virtual Environment:**

```sh
 source venv/bin/activate
```

**Install Dependencies:**

```sh
 pip install -r requirements.txt
```

**Run the Project:**

```sh
 cd scrapy_book_crawler
 scrapy crawl books -o books.json
 scrapy crawl quotes -o authors.json
```
