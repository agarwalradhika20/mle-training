import os

path = os.getcwd()


def test_ingestion():
    raw_datapath = path + "/data/raw/"
    processed_path = path + "/data/processed/"
    assert os.path.isfile(f"{raw_datapath}housing.csv")
    assert os.path.isfile(f"{processed_path}train_x.csv")
    assert os.path.isfile(f"{processed_path}train_y.csv")
    assert os.path.isfile(f"{processed_path}test_x.csv")
    assert os.path.isfile(f"{processed_path}test_y.csv")


def test_training():
    model_path = path + "/artifacts/"
    assert os.path.isfile(f"{model_path}LinearRegression")
    assert os.path.isfile(f"{model_path}DecisionTreeRegression")
    assert os.path.isfile(f"{model_path}RandomForestRegressor_RandomSearch")
    assert os.path.isfile(f"{model_path}randomForestRegressor_GridSearch")


if __name__ == "__main__":
    test_ingestion()
    test_training()
