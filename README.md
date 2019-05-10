# stream_simulator

### Pre-installation
You have to have `docker` and `python3` installed on your PC.

### Installation

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

### Initialize
```
make init
```

### Run server
1. Open terminal
2. Navigate to `stream_simulator` folder
3. Run commands:
```
source env/bin/activate
make server
```

### Run client
1. Open terminal
2. Navigate to `stream_simulator` folder
3. Run commands: `source env/bin/activate`, `make client`
4. From console output click on the link: `http://localhost:8000/client/<client_id>` to see messages in web browser.