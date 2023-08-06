# talk-in-code
Transform __natural language__ strings on __Python runnable code__

## Usage:
### install with pip:
```shell
pip install talk-in-code
```
### Import on your code:
```python
from talk_in_code import translate
```
### Run it
```python
translate.run('print Hello world!', language='pt-BR')
```

## Collaborate
#### Create issues, PR's and share the project, it's open-source!!

___
# How to...
## Print something
Use the key-word print on your string
```python
"print('Hello World')" == translate.run('print Hello World!')
```
## Declare a variable
Use the key-word variável on your string
```python
"idade = int('20')" == translate.run('variável idade recebe inteiro 20')
```

# Help us to improve the pt-BR features and create an english translator!
