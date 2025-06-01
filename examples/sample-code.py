import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def analyze_data(filename):
    # Load dataset
    data = pd.read_csv(filename)
    
    # Basic analysis
    print(data.describe())
    
    # Simple ML model
    X = data.drop('target', axis=1)
    y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    
    # Visualization
    plt.scatter(y_test, model.predict(X_test))
    plt.show()
    
    return score

result = analyze_data('data.csv')
print(f"Model accuracy: {result}")
