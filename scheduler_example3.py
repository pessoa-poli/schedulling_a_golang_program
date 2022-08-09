from unicodedata import name
from rocketry import Rocketry
from datetime import datetime
import subprocess
import os
from redbird.repos import CSVFileRepo
app = Rocketry()

# calling go
@app.task('every 3 sec', name='goProgram_succeed', execution='process')
def callGoToSucceed():
    subprocess.run(['./myGoProgram/bin/main'], shell=True, check=True)
@app.task('every 5 sec', name='goProgram_fail', execution='process')
def callGoToFail():
    subprocess.run(['./myGoProgram/bin/main fail'], shell=True, check=True)

@app.task("after task 'goProgram_fail' failed")
def recongnizeGoFailed():
    subprocess.run(['echo detected go program failed: `date` >> log.csv'], shell=True, check=True)

@app.task("after task 'goProgram_succeed' succeeded")
def recongnizeGoSucceeded():
    subprocess.run(['echo detected go program succeded: `date` >> log.csv'], shell=True, check=True)

if __name__ == "__main__":
    app.run()
