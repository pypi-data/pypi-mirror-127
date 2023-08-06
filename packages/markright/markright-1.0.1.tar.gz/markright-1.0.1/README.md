# markright v&shy;<!---version-->1.0.1<!---/version-->
*Templateless markdown template engine*

## Install

```shell
pip install markright
```

## Python usage

Create a `README.md` file containing:
```markdown
# MyPackage v&shy;<!---ver--><!---/ver-->
```

Create python script `markright_test.py` with code like:
```python
from markright import mark

data = {
    "ver": "0.0.1"
}

mark("README.md", data)
```

Run your script `python ./markright_test.py` and you will get `README.md` looks pretty awsome after rendering, for example on gitlab :
```markdown
# MyPackage v&shy;<!---ver--><!---/ver-->
```
Restarting the script does not require clearing the template, just run the script again with new data!

## CLI Usage

```shell
markright -h # for help
markright -f README.md -d data.json # take data from json file
markright -f README.md -d data.ini # take data from [markright] section of ini file
markright -f README.md -d {"version": "1.0.0"} # data from json string
```