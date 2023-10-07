#Sowtyy
#1.0.0
#07.10.2023


import os
import os.path
import requests
import time
from dotenv import load_dotenv

load_dotenv()


URL = os.getenv("URL")
FILES_DIR_PATH = os.getenv("FILES_DIR_PATH")


def main():
  print(f"{URL=}\n{FILES_DIR_PATH=}")

  dirFileNames = os.listdir(FILES_DIR_PATH)
  dirFileNamesLen = len(dirFileNames)

  for i, fileName in enumerate(dirFileNames):
    filePath = os.path.join(FILES_DIR_PATH, fileName)

    if not os.path.isfile(filePath):
      continue

    with open(filePath, "rb") as file:
      fileDict = {"file": file}

      print(f"Uploading file #{i + 1}/{dirFileNamesLen}: {fileName}...", end = " ")
      response = requests.post(URL, files = fileDict)
      print(("OK," if response.status_code == 200 else "Warning,"), f"{response.status_code}.")
      time.sleep(1)

  print("Done.")
  return

if __name__ == "__main__":
  main()
