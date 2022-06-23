from pathlib import Path
import pandas as pd

df = pd.read_csv('the_data.csv')


def main():
    file_path = Path.cwd() / "the_data.csv"
    print(file_path)

    if file_path.exists():
        df.fillna("John", inplace=True)
        df['Birthdate'] = pd.to_datetime(df['Birthdate'])
        df.drop_duplicates(inplace=True)

    for i in df.index:
        if df.loc[i, 'Name'] == 'Bazinga':
            df.loc[i, 'Name'] = 'Christy'


if __name__ == "__main__":
    main()
    print(df.to_string())
