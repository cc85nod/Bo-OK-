# Bo OK!
A web site about ordering book

## How do use
### settings
1. Copy .env.example to .env and set gmail account and password
2. Open goolge lesssecureapps
3. Copy `book.env.db` to `book.db`
4. Run `python bgCrawling.py` to update newbook and hotbook
5. Run `python app.py` to run server !

### run web server
```
1. pip3 install -r requirements.txt
2. python3 app.py
```

### background crawler
- You can set update time in `bgCrawling.py`
```
python3 bgCrawling.py
```

## Environment
1. python3