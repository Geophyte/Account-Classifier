import random
import joblib

class MockModel:
    def predict(self, input_data):
        # Check if input_data has 5 elements
        if len(input_data) != 5:
            print((input_data))
            raise ValueError("Input data should have 5 elements")

        # Check if all elements in input_data are floats
        if not all(isinstance(item, float) for item in input_data):
            raise ValueError("All elements in input data should be floats")

        # Return a random float between 0 and 1
        return random.random()
    
if __name__ == "__main__":
    model = MockModel()

    joblib.dump(model, 'model.pkl')
