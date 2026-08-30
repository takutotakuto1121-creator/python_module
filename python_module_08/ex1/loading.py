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
    rng = np.random.default_rng(seed=42)
    return rng.normal(loc=0.0, scale=1.0, size=size)


def analyze_data(data: "np.ndarray") -> "pd.DataFrame":
    df = pd.DataFrame(data)
    print(df)
    return df


def create_visualization(df: "pd.DataFrame", output_path: str = "matrix_analysis.png") -> None:
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
