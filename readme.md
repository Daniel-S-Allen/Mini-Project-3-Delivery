# LogLens
A python program to analyze log files

## Requirements
Ensure [Docker](https://docs.docker.com/get-started/get-docker/) is installed.

## Installation
1. Open your terminal and navigate to the folder you want to clone this repository to
2. Clone this repository with `git clone https://github.com/Daniel-S-Allen/Mini-Project-3-Delivery`
3. `cd` into the directory that was created (`Mini-Project-3-Delivery` by default)
4. Run `docker build -t loglens .`

## Usage
Run `docker run loglens <args>` in your terminal, replacing `<args>` with any arguments to pass to the program

usage: `loglens [-h] [-f {txt,csv}] [-o OUTPUT] [-d DATE_RANGE]
                  [-s {INFO,WARNING,ERROR,CRITICAL}] [-p PATTERN] [--stats]
                  [--alerts ALERTS]
                  log_file`

|Argument               |Possible Values            |Reason|
|-----------------------|---------------------------|-------------------------------|
|log_file               |                           |Path to the log file to analyze|
|-h, --help             |                           |show this help message and exit
|-f, --format           |txt,csv                    |Output format (default: txt)
|-o, --output           |                           |Output file path (default: stdout)
|-d, --date-range       |                           |Filter by date range (format: YYYY-MM-DD:YYYY-MM-DD)
|-s, --severity         |INFO,WARNING,ERROR,CRITICAL|Filter by severity level
|-p, --pattern          |                           |Filter by regex pattern
|--stats                |                           |Generate statistics
|--alerts ALERTS        |float                      |Generate alerts for error rates above threshold



## Expected Input/Output
| Input | Output |
|------|-------|
| `docker build -t loglens` | Build docker image from source with progress tracking |
| `docker run loglens --help` | Print usage information |
| `docker run loglens --severity CRITICAL python-example-log.txt` | Print logs of critical severity from `python-example-log.txt`|
| `docker build -t loglens` | Data2 |

## Troubleshooting

- Ensure Docker is installed and running  
  - Check docker installation `docker --version`  
  - Verify that docker is set up correctly by running `docker run hello-world`  
- Start Docker daemon if not running   
  - `sudo systemctl start docker` (linux only)  
- Verify Docker image
  - List docker images `docker images`  
- Check Docker Logs  
  - View container logs `docker logs <container_id>`  
- Verify Running Containers  
  - Check to see if container has is running or has exited `docker ps –a`  
- Rebuild Docker image  
  - Rebuild docker image `docker build -t loglens`

For further troubleshooting, see [Troubleshoot Docker Desktop](https://docs.docker.com/desktop/troubleshoot-and-support/troubleshoot/)