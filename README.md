# LFI-Hunter
Searches for potentially vulnerable websites to local file inclusion, throughout the web and then exploits them for LFI
A script written in python which gathers websites potentially vulnerable to local file inclusion & makes a file named as targets.txt  for future reference or manual exploitation. This script later uses the targets.txt file & start fuzzing the endpoint to check whether the website is actually vulnerable or not.

``Long story short`` : Run this script to get a list of websites along with the vulnerable endpoints.

## Features

- Searches for potentially vulnerable websites
- Performs directory fuzzing at the vulnerable endpoints
- Comes with built in searching algorithm
- Requires an API key for more results

  
## Screenshots

Loading Screen Banner:
![App Screenshot](loading.jpeg)

Script while it is running:
![App Screenshot](run.jpeg)
## Pre Requisites

Python Installed

```bash
version > 3.0
```

## Installation
```bash
git clone https://github.com/anukulpandey/LFI-Hunter
cd LFI-Hunter
pip install requirements.txt
```
## Run locally
```bash
python3 lfi-hunter.py
```

## Authors

- [@anukulpandey](https://www.github.com/anukulpandey)

  
