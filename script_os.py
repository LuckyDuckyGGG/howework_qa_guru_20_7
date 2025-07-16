import os
import shutil

CURRENT_FILE = os.path.abspath(__file__)

CURRENT_DIR = os.path.dirname(CURRENT_FILE)
print(CURRENT_DIR)

TMP_DIR = os.path.join(CURRENT_DIR, "homeworkDirectory")
print(TMP_DIR)

# if not os.path.exists("tmp2"):
#     os.mkdir("tmp2")
#     print("Создал")
# else:
#     print("Не создал")

# shutil.rmtree(os.path.join(CURRENT_DIR, "tmp2"))