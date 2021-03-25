# etl-pipeline

## Notes
The `requirements.txt` file should list all Python libraries that your notebooks
depend on, and they will be installed using:

```
pip install -r requirements.txt
```
[ETl Pipeline Script](main.py) - This script is for ETL to filter words that contain Chilies in the ingredients. After it's filtered, it's classified into 4 levels (Hard, Medium, Easy, Unknown) based on the difficulty of recipes. The difficulty is determined by the number of preparation time and cooking time.
