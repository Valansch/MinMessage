# MinMessage

A tool to simulate a network for sending broadcast with the minimal possible number of messages.


## Installation

Simply clone the repository.

```bash
git clone https://github.com/Valansch/MinMessage.git
```

### Requirements
- python3
- pytest (optional)
    To run the unit tests

## Run

Use python3 to call simulate_network.py directly:

```bash
python3 simulate_network.py 100000 3
```

### Usage

```
    usage: simulate_network.py [-h] <Network size> <Avg edges per node>

    Simulates broadcasting a message with minimum number of messages required

    positional arguments:
    <Network size>        The size of the network to simulate.
    <Avg edges per node>  The average number of edges per node

    optional arguments:
    -h, --help            show this help message and exit
```

## Tests

### Install
```bash
    pip3 install --user pytest
```

### Running the tests
```bash
    python3 -m pytest -v
```
