import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('kc_house_data.csv')

f1, f2, f3 = data['grade'], data['sqft_above'], data['sqft_living']

x1 = (f1 - f1.mean()) / f1.std()
x2 = (f2 - f2.mean()) / f2.std()
x3 = (f3 - f3.mean()) / f3.std()
y = data['price']

m1 = m2 = m3 = c =  0
epochs = 1000
L = 0.02
n = len(data)

for epoch in range(epochs):
    y_ = m1 * x1 + m2 * x2 + m3 * x3 + c
    m1 += (-2/n) * ((y_ - y) * x1).sum() * L
    m2 += (-2/n) * ((y_ - y) * x2).sum() * L
    m3 += (-2/n) * ((y_ - y) * x3).sum() * L
    c += (-2/n) * (y_ - y).sum() * L
    
    if epoch % 100 == 0:
        msr = (1/n) * ((y_ - y)**2).sum()
        print(f"Loss at {epoch} processes is {msr**0.5}")

def plot_regression_line(x1_t, x2_t, x3_t, y_t):
    plt.scatter(x1_t, y_t, alpha=0.3)
    norm_x1 = (x1_t - f1.mean()) / f1.std()
    norm_x2 = (x2_t - f2.mean()) / f2.std()
    norm_x3 = (x3_t - f3.mean()) / f3.std()
    y_pred = m1*norm_x1 + m2*norm_x2 + m3*norm_x3 + c
    plt.plot(x1_t, y_pred, color='red')
    plt.xlabel("Grade")
    plt.ylabel("Price")
    plt.show()

def test_regression():
    test_data = pd.read_csv('kc_house_test_data.csv')
    plot_regression_line(test_data['grade'], test_data['sqft_above'], test_data['sqft_living'], test_data['price'])

def predict_price(grade, sqft_above, sqft_living):
    norm_grade = (grade - f1.mean()) / f1.std()
    norm_sqft_above = (sqft_above - f2.mean()) / f2.std()
    norm_sqft_living = (sqft_living - f3.mean()) / f3.std()
    price = m1 * norm_grade + m2 * norm_sqft_above + m3 * norm_sqft_living + c
    return price

if __name__ == "__main__":
    isRunning = True
    while isRunning:
        print("1. Test Regression Model")
        print("2. Predict House Price")
        print("3. Exit")
        choice = input("Enter your choice: ")
    
        if choice == '1':
            test_regression()
        elif choice == '2':
            grade = float(input("Enter Grade: "))
            sqft_above = float(input("Enter Sqft Above: "))
            sqft_living = float(input("Enter Sqft Living: "))
            predicted_price = predict_price(grade, sqft_above, sqft_living)
            print(f"Predicted House Price: ${predicted_price:,.2f}")
        elif choice == '3':
            isRunning = False
        else:
            print("Invalid choice. Please try again.")