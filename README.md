# streamger-backend
## Installation 

## make sure to install chocolatey in windows

## make virtual environment
```bash
python -m venv venv
```
## activate virtual environment
```bash
venv\Scripts\activate
# for unix 
source venv/bin/activate
```
## install requirements
```bash
pip install -r requirements.txt
```
## make migrations
```bash
make migrations
```
## create super user 
```bash
make superuser
```
## run server
```bash
make run
```
### APIS 
for registration api
```bash
http://localhost:8000/api/register/
```
for login api
```bash
http://localhost:8000/api/login/
```
JWT token api
```bash
http://localhost:8000/api/token/
```
JWT token refresh api
```bash
http://localhost:8000/api/token/refresh/

```
browsable REST_FRAMEWORK login api 
```bash
http://localhost:8000/api-auth/login/

```

## content API is under development 

