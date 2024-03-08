# Audit code using AI

## Install

```bash
$ python3 -m venv .venv && source .venv/bin/activate
$ source .env/bin/activate
$ pip3 install -r requirements
$ python3 setup.py install
```

## Configure

Create an `.env` file and set the `OPENAI_API_KEY` and `ACTIVELOOP_TOKEN`.

## Usage

```bash
$ aai --help
(.venv) ➜  aai --help
Usage: aai [OPTIONS] COMMAND [ARGS]...

  Audit code using AI

Options:
  --help  Show this message and exit.

Commands:
  index   Index code to an ActivePool
  prompt  Prompt the code
```

```bash
$ aai prompt -ua bepresent -ds project_to_audit
Deep Lake Dataset in hub://bepresent/rolla already exists, loading from the storage
Starting conversation...
> qa Explain in me what the code does?
```