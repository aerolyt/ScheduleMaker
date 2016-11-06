I.)	Included files:
	
	1. README 		-	this file
	2. main_writer.py 	- 	script that will generate main.lp
	3. mainExample.lp 	- 	example of a successfully generated main.lp (can be renamed to main.lp if so desired)
	4. input.txt 		-	sample classes used to generate exampleMain.lp
	
II.)	Usage:

		1.)	Create or edit input.txt:
			input.txt must contain classes in the format XXXX####, where XXXX is the class code (CS, SE, GOVT, FILM, etc.) and #### is the class number (must be four digits).
			Class names are not case sensitive and must be separated by a single newline.
			
		2.)	Run main_writer.py:
			Using Python version 2, execute "python main_writer.py" in the terminal/command prompt. Please note input.txt must be in the same directory as main_writer.
			
		3.)	Run main.lp:
			Ensure main.lp is in the same directory as Schedule.lp, and execute it through sasp.exe.
			
		4.)	Results:
			The answer set will contain the schedule that best fits the set of classes. If no schedule is possible, or one of the classes is invalid (not offered), it will return false.
			
III.)	Caveats:

		1.) Currently, classes with variable dates and times (e.g. exam sections and labs) are not supported for generation through main_writer.
		2.) This program operates by comparing each section of a class with the schedule generated and adjusting said schedule until a solution is found or all possibilities have been found.
			As a result, please note that more classes = more sections = more possibilities = much longer runtime.
