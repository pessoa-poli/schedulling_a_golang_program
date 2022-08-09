# schedulling_a_golang_program
This repository was made to test how I could use the Rocketry python library to schedule the execution of a go program compiled to a binary.  

Please check the file scheduler_example3.py for a working example on how to schedule and check the running of a go program using the Rocketry python library.  

[Rocketry Web Page](https://rocketry.readthedocs.io/en/stable/)  

The Golang version can be checked in the go.mod file, inside myGoProgram  

The requirements.txt file is available as well so you can easily build your virtual environment and test this project.  

The Makefile in this project contains a simple rule to erase the log.csv file, rebuild the go binary and clear the terminal, so that less time was spent when fixing mistakes and re-running the program.  
