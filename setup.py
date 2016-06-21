import cx_Freeze
import sys

base = None

executables= [cx_Freeze.Executable("main.py", base= None)]

cx_Freeze.setup(
		name= "Client",
		options= {"build_exe": {"packages":[]}},
		version= "0.01",
		description= "my des",
		executables= executables
)
