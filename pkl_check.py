import pandas as pd


def inspect_pkl(filepath):
    try:
        df = pd.read_pickle(filepath)
    except Exception as e:
        print(f"Error loading .pkl file: {e}")
        return

    # Basic Info
    print("=" * 50)
    print(f"File: {filepath}")
    print("=" * 50)
    print(f"Data Type: {type(df)}")
    print(f"Shape: {df.shape} (Rows x Columns)")
    print(f"Columns: {list(df.columns)}")
    print("\n")

    # Data Types
    print("=" * 50)
    print("Data Types:")
    print("=" * 50)
    print(df.dtypes)
    print("\n")

    # Missing Values
    print("=" * 50)
    print("Missing Values (Gaps):")
    print("=" * 50)
    missing = df.isna().sum()
    print(missing[missing > 0] if missing.sum() > 0 else "No gaps found!")
    print("\n")

    # Summary Stats
    print("=" * 50)
    print("Summary Statistics:")
    print("=" * 50)
    print(df.describe(include='all'))
    print("\n")

    # Sample Data
    print("=" * 50)
    print("Sample Data:")
    print("=" * 50)
    print(df.head(3))
    print("\n...\n")
    print(df.tail(3))
    print("\n")

    # Check Requirements for Imputation
    print("=" * 50)
    print("Validation Checks:")
    print("=" * 50)
    if not isinstance(df.index, pd.DatetimeIndex):
        print("❌ Index is NOT datetime. Required for time-series imputation.")
    else:
        print("✅ Index is datetime.")

    gap_cols = [col for col in df.columns if df[col].isna().any()]
    if len(gap_cols) == 0:
        print("❌ No columns with gaps found. Nothing to impute!")
    else:
        print(f"✅ Found {len(gap_cols)} gap columns: {gap_cols}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, required=True, help="Path to .pkl file")
    args = parser.parse_args()
    inspect_pkl(args.file)
