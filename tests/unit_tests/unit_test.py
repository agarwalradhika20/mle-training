import unittest

import pandas as pd

housing_df = pd.read_csv("./data/raw/housing.csv")
xTrain = pd.read_csv("./data/processed/train_x.csv")
yTrain = pd.read_csv("./data/processed/train_y.csv")
xTest = pd.read_csv("./data/processed/test_y.csv")
yTest = pd.read_csv("./data/processed/test_y.csv")


class MyTest(unittest.TestCase):
    def test_data_shape(self):
        self.assertTrue(xTrain.shape[0] == yTrain.shape[0])
        self.assertTrue(xTest.shape[0] == yTest.shape[0])
        self.assertTrue(yTest.shape[1] == 1)

    def test_split_ratio(self):
        self.assertEqual(housing_df.shape[0] * 0.8, yTrain.shape[0])
        self.assertEqual(housing_df.shape[0] * 0.2, yTest.shape[0])


if __name__ == "__main__":
    unittest.main()
