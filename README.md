# Median housing value prediction

The housing data can be downloaded from https://raw.githubusercontent.com/ageron/handson-ml/master/. The script has codes to download the data. We have modelled the median house value on given housing data.

The following techniques have been used:

 - Linear regression
 - Decision Tree
 - Random Forest

## Steps performed
 - We prepare and clean the data. We check and impute for missing values.
 - Features are generated and the variables are checked for correlation.
 - Multiple sampling techinuqies are evaluated. The data set is split into train and test.
 - All the above said modelling techniques are tried and evaluated. The final metric used to evaluate is mean squared error.

## Folder stucture
    ├───artifacts
    ├───data
    │   ├───processed
    │   └───raw
    ├───deploy
    │   ├───conda
    │   └───docker
    ├───dist
    ├───docs
    │   ├───build
    │   │   ├───doctrees
    │   │   └───html
    │   │       ├───_modules
    │   │       │   └───housingpricera
    │   │       ├───_sources
    │   │       └───_static
    │   │           ├───css
    │   │           │   └───fonts
    │   │           └───js
    │   └───source
    │       ├───_static
    │       └───_templates
    ├───logs
    ├───notebooks
    ├───Scripts
    ├───src
    │   ├───housingpricera
    │   │   └───__pycache__
    └───tests
        ├───functional_tests
        └───unit_tests

## Activate Environment
   - cd deploy/conda
   - conda env create --name envname --file=env.yml
   - conda activate envname


## Install Housing Package
    pip install -i https://test.pypi.org/simple/ housingpricera

## Verify Installations
   - cd ./tests/functional_tests
   - python test_installation.py

## Workflow scripts
    - cd src/housingpricera
    - python ingest_data.py
    - python train.py
    - python score.py

## Testing
    - python ./tests/unit_tests/unit_test.py
    - python ./tests/functional_tests/functional_test.py

## For HTML Documentation
    - Open ./docs/_build/html/index.html in browser
