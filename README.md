# Opera GX Search Engine Rewrite
Allows the usage of custom search engines in Opera GX by running a redirect server.

## Purpose
I created this project because I wanted to use Brave Search on Opera GX, but when I went to make it default the option was blanked out. In my opinion, regardless of what Opera says about preventing "malicious" acts by doing this, I think its unacceptable.

## How it works
This project works by creating a https server in python with the domain "redir.opera.com" and making it redirect to Brave Search (customizable). 

## Installation (windows only)
1. Install [OpenSSL](https://slproweb.com/download/Win64OpenSSL-3_0_2.exe)
2. Install [Python](https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe)
3. Download the project's source code.
4. Move it to the C: drive.
5. Change your search engine in Opera (GX) to Amazon.

## Run on startup
1. Open Task Scheduler.
2. Create a basic task.
3. Call it anything.
4. Select "When I log on" for Trigger.
5. Select "Start a program" for Action.
6. For the action settings put the following:
   - Program/script: py
   - Add arguments: rewrite.py
   - Start in: "C:\Opera-GX-Search-Engine-Rewrite-main"
7. Right click Properties on the new task.
8. Change the following settings:
   - Run whether user is logged on or not
   - Do not store password.
   - Hidden
