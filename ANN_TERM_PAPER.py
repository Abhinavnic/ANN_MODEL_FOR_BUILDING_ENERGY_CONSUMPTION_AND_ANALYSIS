import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score,accuracy_score

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

from google.colab import files

upload=files.upload()

da = pd.read_excel("dataset for buildings energy consumption of 3840 records (1).xlsx")
da

x = da.iloc[:, list(range(0, 10)) + list(range(15, 23))]
x

y = da.iloc[:, 13]
y

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=2529)

model = Sequential()

model.add(Dense(units=64, activation='relu', input_dim=x_train.shape[1], kernel_initializer='he_uniform'))
model.add(Dense(units=32, activation='relu', kernel_initializer='he_uniform'))
model.add(Dense(units=1, activation='linear'))

model.summary()

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

model.fit(x_train, y_train, validation_split=0.2, epochs=50, batch_size=32, verbose=1)

y_pred=model.predict(x_test)
y_pred

threshold = y_test.mean()
y_test_binary = (y_test > threshold).astype(int)
y_pred_binary = (y_pred > threshold).astype(int)
accuracy = accuracy_score(y_test_binary, y_pred_binary)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error (MSE): {mse:.4f}")
print(f"Mean Absolute Error (MAE): {mae:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
print(f"R-squared (R2 Score): {r2:.4f}")
print(f"Accuracy: {accuracy:.4f}")

