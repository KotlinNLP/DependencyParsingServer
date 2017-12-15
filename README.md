# DependencyTreeServer

DependencyTreeServer is a web server that forwards requests to the 
[NLPServer](https://github.com/KotlinNLP/NLPServer "NLPServer on GitHub") 
and return the response for the 
[DependencyParsingDemo](https://github.com/KotlinNLP/DependencyParsingDemo "DependencyParsingDemo on GitHub").


## Requirements

* Python Pip
```bash
sudo apt-get install python-pip python-dev build-essential
```

* Python dependencies
```bash
sudo pip install -r requirements.txt
```


## Configuration

Create your own configuration file:
```bash
cd config/
cp configuration.xml.example configuration.xml
```

And edit it properly:
```bash
nano configuration.xml
```


## How to start

Launch from terminal:

```bash
python . [-t HOST] [-p PORT]
```
* Default HOST: 127.0.0.1
* Default PORT: 30000


## License

This software is released under the terms of the 
[Mozilla Public License, v. 2.0](https://mozilla.org/MPL/2.0/ "Mozilla Public License, v. 2.0")


## Contributions

We greatly appreciate any bug reports and contributions, which can be made by filing an issue or making a pull 
request through the [github page](https://github.com/KotlinNLP/DependencyTreeServer "DependencyTreeServer on GitHub").
