# Domain Analyzer
Steps required to correctly run app:
*Assume that env is created and all requirements are installed*

**It's necessary to run three independent terminal windows**

### Run backend server
```bash
cd server
source env/bin/activate
flask run
```


### Run client
```bash
cd client
npm run serve
```

### Run background task manager
```bash
cd server
source env/bin/activate
celery worker -A app.celery --loglevel=info
```
