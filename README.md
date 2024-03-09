# Audit code using AI

## Install

```bash
$ python3 -m venv .venv && source .venv/bin/activate
$ source .env/bin/activate
$ pip3 install -r requirements
$ python3 setup.py install
```

## Configure

Create an `.env` file and set the [`OPENAI_API_KEY`](https://openai.com/blog/openai-api) and [`ACTIVELOOP_TOKEN`](https://activeloop.ai).

## Usage

### Help command

```bash
$ aai --help
Usage: aai [OPTIONS] COMMAND [ARGS]...

  Audit code using AI

Options:
  --help  Show this message and exit.

Commands:
  index   Index code to an ActivePool
  prompt  Prompt the code
```

### Upload the code to audit to `activePool`

```bash
$ aai index -ua bepresent -ds pta -sp /tmp/project-to-audit/src/
```

### Initiate a conversation

```bash
$ aai prompt -ua bepresent -ds pta
Deep Lake Dataset in hub://bepresent/pta already exists, loading from the storage
Starting conversation...
> qa Explain in me what the code does?
```
