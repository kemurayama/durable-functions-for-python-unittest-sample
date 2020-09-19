# Azure Durable Functions for Python UnitTest Sample

## What is this ?

Based on [Durable Functions unit testing](https://docs.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-unit-testing#unit-testing-activity-functions) for C#, created Durable Functions UnitTest Sample for Python.

Since this sample uses [IsolatedAsyncioTestCase](https://docs.python.org/3/library/unittest.html#unittest.IsolatedAsyncioTestCase) in order to test async function, Python version should be 3.8 above.

```bash
$ python --version
Python 3.8.5
```

```bash
azure-functions==1.3.1
azure-functions-durable==1.0.0b8
```

There are 3 test files which are bsaed on template samples.

- test_DurableFunctionsHttpStart.py
- test_DurableFunctionsOrchestrator.py
- test_Hello.py

## Usage

1. [Create your first durable function in Python](https://docs.microsoft.com/en-us/azure/azure-functions/durable/quickstart-python-vscode)
2. Create `tests` directory under project root then copy `test_xxx.py` files under `tests` directory.
3. Run `python -m unittest tests.test_xxx.py` at project root.

You will see these files after finishing tutorial.

```
.devcontainer
.funcignore
.vscode
DurableFunctionsHttpStart/
DurableFunctionsOrchestrator/
Hello/
host.json
proxies.json
requirements.txt
```

## License

Copyright (c) 2020 kemurayama
[MIT LICENSE](./LICENSE)

- Template Functions are from [Azure/azure-functions-templates](https://github.com/Azure/azure-functions-templates)
- Other Templates files are from [microsoft/vscode-azurefunctions](https://github.com/microsoft/vscode-azurefunctions)
- Dev Container files are from [microsoft/vscode-dev-containers](https://github.com/microsoft/vscode-dev-containers)
