'''
My problem and solutions

31/5/2021:  What is the bionetgen? -> Ans. other laguage
01/6/2021:  What is the environment variable BNGPATH by path? 

03/6/2021: set BNGPATH environment variable
instalation BioNetGen by pip install bionetgen and set BNGPATH for environment variable as following:
BNGPATH
C:\Users\Lenovo\AppData\Local\Programs\Python\Python39\Lib\site-packages\bionetgen\bng-win##
! not complete because BNG2.pl has to open with Perl from jupeter error:
    "BngInterfaceError: 
    Can't locate BNGUtils.pm in @INC (you may need to install the BNGUtils module) (@INC contains: C:\Users\Lenovo\AppData\Local\Programs\Python\Python39\Lib\site-packages\bionetgen\bng-win\BNG2.pl\Perl2 C:/Users/Lenovo/anaconda3/Library/vendor/lib C:/Users/Lenovo/anaconda3/Library/lib) at C:\Users\Lenovo\AppData\Local\Programs\Python\Python39\Lib\site-packages\bionetgen\bng-win\BNG2.pl line 50.
    BEGIN failed--compilation aborted at C:\Users\Lenovo\AppData\Local\Programs\Python\Python39\Lib\site-packages\bionetgen\bng-win\BNG2.pl line 50."

VS code and command promt error is 
    "Traceback (most recent call last):
  File "c:\users\lenovo\appdata\local\programs\python\python39\lib\runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "c:\users\lenovo\appdata\local\programs\python\python39\lib\runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "C:\Users\Lenovo\AppData\Local\Programs\Python\Python39\Scripts\bionetgen.exe\__main__.py", line 7, in <module>
  File "c:\users\lenovo\appdata\local\programs\python\python39\lib\site-packages\bionetgen\main.py", line 246, in main
    app.run()
  File "c:\users\lenovo\appdata\local\programs\python\python39\lib\site-packages\cement\core\foundation.py", line 916, in run
    return_val = self.controller._dispatch()
  File "c:\users\lenovo\appdata\local\programs\python\python39\lib\site-packages\cement\ext\ext_argparse.py", line 808, in _dispatch
    return func()
  File "c:\users\lenovo\appdata\local\programs\python\python39\lib\site-packages\bionetgen\main.py", line 74, in run
    runCLI(self.app.config, args)
  File "c:\users\lenovo\appdata\local\programs\python\python39\lib\site-packages\bionetgen\core\main.py", line 35, in runCLI
    cli.run()
  File "c:\users\lenovo\appdata\local\programs\python\python39\lib\site-packages\bionetgen\core\main.py", line 127, in run
    rc = subprocess.run(["perl", self.bng_exec, self.inp_path], stdout=stdout_loc, stderr=stderr_loc)
  File "c:\users\lenovo\appdata\local\programs\python\python39\lib\subprocess.py", line 505, in run
    with Popen(*popenargs, **kwargs) as process:
  File "c:\users\lenovo\appdata\local\programs\python\python39\lib\subprocess.py", line 951, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "c:\users\lenovo\appdata\local\programs\python\python39\lib\subprocess.py", line 1420, in _execute_child
    hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
FileNotFoundError: [WinError 2] The system cannot find the file specified"


04/6/2021: To acheived installation BioNetGen
            For windown has to perl before install RuleBender (include BioNetgen folder amd set BNGPATH for environment variable) ->
            https://github.com/RuleWorld/rulebender/blob/master/docs/RuleBender-installation-guide.pdf

'''