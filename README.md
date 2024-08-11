**Activate Virtual Environment**
```
python3 -m venv .blockchainenv
source .blockchainenv/bin/activate
```
**On Windows use:** 
```
.blockchainenv\Scripts\activate
```


**Install Required Packages**
```
pip install -r requirements.txt
```


**Test the Application**

Make sure the virtual environment is activated
```
python -m pytest backend/tests
```