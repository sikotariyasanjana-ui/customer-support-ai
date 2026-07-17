import os
import pandas as pd

# Current directory (backend/datasets)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_products():
    file_path = os.path.join(BASE_DIR, "products.csv")
    return pd.read_csv(file_path)


def load_faq():
    file_path = os.path.join(BASE_DIR, "faq.csv")
    return pd.read_csv(file_path)


def load_users():
    file_path = os.path.join(BASE_DIR, "users.csv")
    return pd.read_csv(file_path)


def load_orders():
    file_path = os.path.join(BASE_DIR, "orders.csv")
    return pd.read_csv(file_path)


def load_complaints():
    file_path = os.path.join(BASE_DIR, "complaints.csv")
    return pd.read_csv(file_path)