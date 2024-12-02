import joblib
model = joblib.load('best_rf_model.pkl')
def predict(data):
    return model.predict(data)
