#!/usr/bin/env python3


import os
from dotenv import load_dotenv


def check_hardcoded(source_path: str) -> bool:
    suspicious_patterns = [
        "MATRIX_MODE " + "="
        "DATABASE_URL " + "="
        "API_KEY " + "="
        "LOG_LEVEL " + "="
        "ZION_ENDPOINT " + "="
    ]
    with open(source_path, "r") as f:
        source = f.read()
        return not any(patterns in source for patterns in suspicious_patterns)


def check_env(values: list) -> bool:
    env_exist = os.path.exists(".env")
    values__exist = all(value is not None for value in values)
    return env_exist and values__exist


def check_overrides() -> bool:
    os.environ["MATRIX_MODE"] = "test"
    load_dotenv()
    return os.getenv("MATRIX_MODE") == "test"


if __name__ == "__main__":
    load_dotenv()

    matrix_mode = os.getenv("MATRIX_MODE")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    if matrix_mode == "development":
        print("[DEVELOPMENT]")
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")
    print(f"Database: {database_url}")
    print(f"API Access: {api_key}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {zion_endpoint}")
    print()
    print("Environment security check:")
    values = [matrix_mode, database_url, api_key, load_dotenv, zion_endpoint]
    if check_hardcoded("oracle.py"):
        print("[OK] No hardcoded secrets detected")
    else:
        print("[KO] hardcoded secrets detected")
    if check_env(values):
        print("[OK] .env file properly configured")
    else:
        print("[KO] .env file doesn't extst or isn't properly configured")
    if check_overrides():
        print("[OK] Production overrides available")
    else:
        print("[KO] Production overrides aren't available")
    print()
    print("The Oracle sees all configurations")
