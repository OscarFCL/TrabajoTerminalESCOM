@ECHO OFF
doskey ls= dir /b
doskey irtt= E: ^& cd E:\Mi\Mavis\Github\TrabajoTerminalESCOM\SASTRE

doskey vir= cd E:\Mi\Mavis\Github\TrabajoTerminalESCOM\SASTRE\sastreenv ^&^& cd E:\Mi\Mavis\Github\TrabajoTerminalESCOM\SASTRE ^&^& E:\Mi\Mavis\Github\TrabajoTerminalESCOM\SASTRE\sastreenv\Scripts\activate
doskey correr= python manage.py runserver
doskey cambios= python manage.py makemigrations ^&^& python manage.py migrate

E:
cd E:\Mi\Mavis\Github\TrabajoTerminalESCOM\SASTRE
E:\Mi\Mavis\Github\TrabajoTerminalESCOM\SASTRE\sastreenv\Scripts\activate