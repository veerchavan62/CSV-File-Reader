# CSV File Reader using Python

## 📌 Project Description
This project is a simple Python program that reads and displays data from a CSV file.  
The dataset used in this project is taken from **Kaggle** and contains information about cars such as brand, year, fuel type, price, and efficiency.

The main goal of this project is to understand how to work with large CSV datasets using Python in a clean and simple way.

---

## 📂 Dataset Information
- Source: Kaggle
- File name: `global_cars_data.csv`
- Data includes:
  - Car ID
  - Brand
  - Manufacture Year
  - Body Type
  - Fuel Type
  - Transmission
  - Engine CC
  - Horsepower
  - Mileage
  - Price (USD)
  - Manufacturing Country
  - Car Age
  - Price Category
  - Efficiency Score

---

## 🛠️ Technologies Used
- Python
- CSV module (`csv.DictReader`)
- Visual Studio Code
- Git & GitHub

---

## ⚙️ How the Program Works
1. The program opens the CSV file.
2. It uses `DictReader` to read each row as a dictionary.
3. Each column name is treated as a key and its data as a value.
4. The program prints all vehicle details in a readable format.
5. The program works for small or large datasets without changing the code.

---

## ▶️ How to Run the Project
1. Clone the repository or download the files.
2. Make sure Python is installed.
3. Keep the CSV file and Python file in the same folder.
4. Run the program using:
   ```bash
   python read_csv.py
