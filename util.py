import os
import joblib
import matplotlib.pyplot as plt

print('util loaded')

PROJECT_ROOT_DIR = "."
MODELS_PATH = os.path.join(PROJECT_ROOT_DIR, "models")
IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR, "images")

os.makedirs(MODELS_PATH, exist_ok=True)

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)

def save_model(model, name):
    name = name + ".pkl"
    p = os.path.join(MODELS_PATH, name)
    joblib.dump(model, p)

def load_model(model_name):
    model_name = model_name + ".pkl"
    p = os.path.join(MODELS_PATH, model_name)
    m = None
    if os.path.exists(p):
        m = joblib.load(p)
    return m