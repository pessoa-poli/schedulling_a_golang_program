from rocketry import Rocketry
from datetime import datetime
import os
from redbird.repos import CSVFileRepo
app = Rocketry()
""" app = Rocketry(
    logger_repo=CSVFileRepo(
        filename="logs.csv"
    )
) """


# @app.task('minutely between 00 and 10')
@app.task('every 2 sec')
def do_things():
    with open('./logs.csv', 'a') as f:
        f.write(f'{datetime.now()}, phlegm\n')


@app.task("(after task 'do_things') & (every 3 sec)")
def do_after():
    with open('./logs.csv', 'a') as f:
        f.write(f'{datetime.now()}, FINISHED\n')


if __name__ == "__main__":
    do_things()
    app.run()
