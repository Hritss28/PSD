import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'BME_TEST_DEPLOY_TARGET_ONLY.csv')

df = pd.read_csv(csv_path)

class_counts = df.iloc[:, 0].value_counts()

print("=" * 50)
print("JUMLAH SETIAP KELAS")
print("=" * 50)
print(class_counts)
print("=" * 50)
print(f"\nTotal data: {len(df)}")
print("\nPersentase:")
for kelas, jumlah in class_counts.items():
    persentase = (jumlah / len(df)) * 100
    print(f"{kelas}: {jumlah} ({persentase:.2f}%)")
