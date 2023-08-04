@echo off
if "%1" == "h" goto begin
mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit
:begin

:: D:
:: cd D:\_archived\screenshot

%~d0
cd %~dp0 

python main.py > log.txt

:: 无窗口运行
