# Strava Tools

Tools to query, monitor, and manipulate data from Strava

## Python Environment

The python 3.10 development environment is handled with python virtual environments.
Create, activate the virtual environment, and install the required packages with the following commands:

```bash
python3.10 -m venv venv
source venv/bin/activate
pip install requests python-dotenv
```

To run scripts within `bin/` you must also install `strava_tools` as a package:

```bash
pip install -e .
```

Then you can run scripts from the root directory of the repository:

```bash
python bin/test_api_request.py
```
