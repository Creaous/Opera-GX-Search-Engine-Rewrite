# Opera GX Search Engine Rewrite
Allows the usage of custom search engines in Opera GX by running a redirect server.

## Installation (windows only)
1. Install [OpenSSL](https://slproweb.com/download/Win64OpenSSL-3_0_2.exe)
2. Install [Python](https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe)
3. Download the project's source code.
4. Move it to the C: drive.
5. Done

## Run on startup
1. Open Task Scheduler.
2. Create a basic task.
3. Call it anything.
4. Select "When I log on" for Trigger.
5. Select "Start a program" for Action.
6. For the action settings put the following
   - Program/script: py
   - Add arguments: rewrite.py
   - Start in: "C:\Opera-GX-Search-Engine-Rewrite-main"
7. Right click Properties on the new task.
8. Change the following settings:
   - Run whether user is logged on or not
   - Do not store password.
   - Hidden
