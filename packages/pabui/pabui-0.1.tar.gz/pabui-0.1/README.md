# PAB UI

A Web-based GUI for PAB development. Check out [PAB here!](https://github.com/manuelpepe/PyAutoBlockchain)


## Features

* Load project from host filesystem
* Read and edit configs
* Read, edit and create tasks
* List strategies and parameters
* List, add and remove contracts
* Create/Restore private key


## Running the UI

```bash
	$ pip install pabui
	$ pabui
```

The UI loads the PAB project in the current working directory, so you have to run `pabui`
from the directory with your `config.json`, `tasks.json` and such. 

## Development

After cloning the repo and installing all dependencies, make sure to install the pre-commit hooks for the
automatic formatter (see black):

```bash
	$ source venv/bin/activate
	$ pip install -r requirements-dev.txt
	$ pre-commit install
```

For UI development check [the frontend README](frontend/README.md)

### Running tests

```
	$ . venv/bin/activate
	$ pip install -r requirements-dev.txt
	$ pytest --cov=pabui
```


