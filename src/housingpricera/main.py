import os
import warnings

import mlflow
import numpy as np

from housing.ingest_data import fetch_housing_data, load_housing_data, preprocess, split
from housing.score import score
from housing.train import train, dump_model

np.random.seed(40)
warnings.filterwarnings("ignore")

model_path = ".\\artifacts"
data_path = ".\\data\\processed"
HOUSING_PATH = ".\\data\\raw"
# mlflow server --backend-store-uri artifacts/mlruns/ --default-artifact-root artifacts/mlruns/ --host 0.0.0.0 --port 5000
remote_server_uri = "http://127.0.0.1:5000/"  # set to your server URI
mlflow.set_tracking_uri(remote_server_uri)  # or set the MLFLOW_TRACKING_URI in the env

exp_name = "HousingPrice"
mlflow.set_experiment(exp_name)


def housing_flow():
    # Download dataset
    fetch_housing_data(housing_path=HOUSING_PATH)
    # loading data
    data = load_housing_data(housing_path=HOUSING_PATH)
    training_set, testing_set = split(data)

    with mlflow.start_run(run_name="HOUSING") as parent_run:
        # mlflow.log_param("parent", "no")

        with mlflow.start_run(run_name="Data_Preprocessing", nested=True) as child_run:
            # mlflow.log_param("child_preprocess", "no")
            train_x, train_y = preprocess(training_set)
            test_x, test_y = preprocess(testing_set)
            # mlflow.sklearn(data_path)

        lin_reg, tree_reg, forest_reg, grid_search = train(train_x, train_y)

        for model in [
            ["LinearRegression", lin_reg],
            ["DecisionTreeRegression", tree_reg],
            ["RandomForestRegressor_RandomSearch", forest_reg],
            ["randomForestRegressor_GridSearch", grid_search],
        ]:
            dump_model(model[1], model_path, model[0])
            with mlflow.start_run(run_name=model[0], nested=True) as child_run:
                mlflow.log_param("Param", model[1].get_params())
                mlflow.sklearn.log_model(model[1], "model")
                mse, rmse, mae = score(
                    os.path.join(model_path, model[0]), test_x, test_y
                )
                # Print out metrics
                # print("Housing model :" % )
                print("  RMSE: %s" % rmse)
                print("  MSE: %s" % mse)
                print("  MAE: %s" % mae)

                # Log parameter, metrics, and model to MLflow
                mlflow.log_metric(key="rmse", value=rmse)
                mlflow.log_metrics({"mae": mae, "mse": mse})
                # mlflow.log_artifact(data_path)


if __name__ == "__main__":
    try:
        housing_flow()
    except Exception as e:
        print(e.args, e.with_traceback)