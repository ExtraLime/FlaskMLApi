## What Did you Say?

#### A small example of to use Flask as a REST Api for ML Model inference

This project can be run locally or in a Docker Container.
(Before building the docker container)<br>
To get started, navigate to the models directory:<br>
```cd wdys/blueprints/language/models``` <br>
and run (important):<br>
```python3 setup_models.py``` <br>
This will download the necessary model metadata and save the files in the necessary location.<br>

### To run locally in develop mode:
Navigate to the wdys directory and run:<br>
```bash serve.sh```

### To run as a docker instance:
From the root directory, after running setup_models.py:<br>
```docker-compose up --build```<br>
This assumes you already have docker installed and can compose

### Once the app is running:
visit localhost:8000 in your browser to verify the api is working<br>

#### For Entity Recognition:

You can send either a POST with request with a 'sentence' key and some text as a value or a GET request with a parameter string.<br>

example:<br>
```http://localhost:8000/ner?sentence=My name is Will and this is hosted on Github!```

response:
[
  {
    "Will": "I-PER"
  }, 
  {
    "##ithub": "I-ORG"
  }
]

### Tests

This repo is also equipped with pytest to test the endpoints.
run ```py.test wdys/tests``` from the root directory
