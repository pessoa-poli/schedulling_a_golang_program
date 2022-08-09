from unicodedata import name
from rocketry import Rocketry
from datetime import datetime
import os
from redbird.repos import CSVFileRepo
app = Rocketry()
log_output = './log.csv'
# @app.task('minutely between 00 and 10')


app.task('every 2 sec', command=('./failer.sh'),
         name='failer', execution='process')


@app.task("(after task 'failer' failed) & (every 3 sec)")
def do_after():
    with open(log_output, 'a') as f:
        f.write(f'{datetime.now()}, failer FAILED\n')

app.task('every 5 sec', command=('./myGoProgram/bin/main'),
         name='goProgram', execution='process')

@app.task("(after task 'goProgram' succeeded) & (every 3 sec)")
def do_after2():
    with open(log_output, 'a') as f:
        f.write(f'{datetime.now()}, goProgram SUCCEEDED\n')



if __name__ == "__main__":
    app.run()
