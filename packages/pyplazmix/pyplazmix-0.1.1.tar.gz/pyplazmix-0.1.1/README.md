# PyPlazmix - A python wrapper for PlazmixAPI
# Installing
**Python 3.9 or higher is required**
## For windows
```py
pip install pyplazmix
```
## For Linux/macOS
```py
python3 -m pip install pyplazmix
```
# Examples
## Client
```py
from pyplazmix import ApiClient

client = ApiClient("TOKEN HERE")
```
## Get user
```py
user = client.get_user(nickname="nickname")  # or uuid="uuid" or _id=id
print(user)
```