# Audit code using AI

## Install

```bash
$ git clone git@github.com:0xbepresent/auditoorai.git
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
$ aai index --help
Usage: aai index [OPTIONS]

  Index the data source to an ActivePool Storage

Options:
  -v, --verbose                   Enables verbose mode
  -ua, --username-activepool TEXT
                                  Username ActivePool  [required]
  -ds, --dataset TEXT             Dataset name in ActivePool
  -sp, --source-path TEXT         Code source to upload
  --help                          Show this message and exit.
```

```bash
$ aai index -ua bepresent -ds pta -sp /tmp/project-to-audit/src/
```

### Initiate a conversation

```bash
$ aai prompt --help
Usage: aai prompt [OPTIONS]

  Open prompt

Options:
  -v, --verbose                   Enables verbose mode
  -ua, --username-activepool TEXT
                                  Username ActivePool  [required]
  -ds, --dataset TEXT             Dataset name in ActivePool
  --help                          Show this message and exit.
```

```bash
$ aai prompt -ua bepresent -ds pta
Deep Lake Dataset in hub://bepresent/pta already exists, loading from the storage
Starting conversation...
> qa Explain in me what the code does?
```
