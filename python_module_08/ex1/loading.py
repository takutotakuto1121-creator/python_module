#!/usr/bin/env python3

try:
    import pandas as pd
except ImportError:
    pd = None

try:
    import requests
except ImportError:
    requests = None

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
except ImportError:
    matplotlib = None
    plt = None

try:
    import numpy as np
except ImportError:
    np = None

try:
    import sys
except ImportError:
    sys = None

try:
    import importlib
except ImportError:
    importlib = None


def check_dependency(name: str, module: object) -> bool:
    if module is None:
        print(f"[KO] {name} - not installed")
        return False
    else:
        version = getattr(module, "__version__", "unknown")
        print(f"[OK] {name} ({version}) - ready")
        return True


def generate_matrix_data(size: int = 1000) -> "np.ndarray":
    """
    np.random.default_rng(seed=42)
    ...numpyの乱数生成器。seedを指定することにより、毎回同じ乱数列が再現される。
    rng.normal(loc=0.0, scale=1.0, size=size)
    ...正規分布に従う乱数をsize個生成。loc->中心, scale->標準偏差, size->生成する個数
       戻り値->1000個の浮動小数点が入った1次元のnumpy配列
    """
    rng = np.random.default_rng(seed=42)
    return rng.normal(loc=0.0, scale=1.0, size=size)


def analyze_data(data: "np.ndarray") -> "pd.DataFrame":
    """
    pd.DataFrame(data)
    ...numpyの1次元配列をpandasのDataFrame(表形式のデータ)に変換。1000行一列
       の配列になり、列名は自動で0になる.
    """
    df = pd.DataFrame(data)
    print(df)
    return df


def create_visualization(
        df: "pd.DataFrame",
        output_path: str = "matrix_analysis.png") -> None:
    """
    df.plot()
    ...pandasに組み込まれている可視化メソッド。DataFrameの中身を折れ線グラフとして描画。
    plt.savefig(output_path)
    ...df.plot()で作られたグラフを指定したファイル名に画像として保存。
    """
    df.plot()
    plt.savefig(output_path)


def main():
    print("LOADING STATUS: Loading program...")
    print()
    print("Checking dependencies...")

    deps_ok = True
    deps_ok &= check_dependency("pandas", pd)
    deps_ok &= check_dependency("requests", requests)
    deps_ok &= check_dependency("matplotlib", matplotlib)
    deps_ok &= check_dependency("numpy", np)
    deps_ok &= check_dependency("sys", sys)
    deps_ok &= check_dependency("importlib", importlib)
    print()

    if not deps_ok:
        print("[Error] import required module")
        print("Usage: pip install <module>")
        sys.exit(1)

    print("Analyzing Matrix data...")
    data = generate_matrix_data(1000)
    # print(data)
    print("Procesing 1000 data points...")
    df = analyze_data(data)
    print("Generating Visualization...")
    create_visualization(df)
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()

# poetry add "pandas>=2.1,<3.0"
# poetry add "numpy>=1.26,<2.0"
# poetry add "matplotlib>=3.8,<3.9"
# poetry add requests
