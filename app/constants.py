from app.commons.csv_writer import CSVWriter
import pathlib, os


BASE_PATH = pathlib.Path(__file__).parent.absolute()
HOST = "35.239.80.182"
PORT = "3001"
BASE_URL = "http://{}:{}".format(HOST, PORT)
allowed_methods = ("xpath", "name" , "link_text", "partial_link_text", "id", "tag_name", "class_name", "css_selector")
MEDIA_PATH = f"{BASE_PATH}/media"
STATIC_PATH = f"{BASE_PATH}/static"
EXPORT_PATH = f"{BASE_PATH}/export"
DRIVER_PATH = f"{STATIC_PATH}/chromedriver.exe"
csv_writer = CSVWriter(f'{EXPORT_PATH}/TestCase.csv', ["Path","Error Type",  "Remarks" , "Result"])
MAX_WAIT = 5


if not os.path.exists(MEDIA_PATH):
    os.mkdir(MEDIA_PATH)

if not os.path.exists(STATIC_PATH):
    os.mkdir(MEDIA_PATH)
