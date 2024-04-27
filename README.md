# Audit code using AI

## Install

```bash
$ git clone git@github.com:0xbepresent/auditoorai.git
$ python3 -m venv .venv && source .venv/bin/activate
$ pip3 install -r requirements.txt
$ python3 setup.py install
```

## Configure

Create an `.env` file and set the [`OPENAI_API_KEY`](https://openai.com/blog/openai-api) and [`ACTIVELOOP_TOKEN`](https://activeloop.ai).

```bash
$ cp .env-example .env
```

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
> qa in `RedemptionFacet::disputeRedemption` what is the purpose and why someone wants to dispute?

**Answer**: The `disputeRedemption` function in the `RedemptionFacet` contract is designed to allow users to challenge a proposed short redemption that they believe is incorrect or invalid. 

The reason why someone might want to dispute a proposed short is because the system allows DUSD holders to redeem their tokens for an equivalent amount of ETH. Users propose a list of Short Records (SRs) to redeem against, but this list is not automatically sorted from lowest to highest. Therefore, there is a risk that a user could propose an incorrect or unfair list of SRs for redemption.

To protect the system and its users, the `disputeRedemption` function provides a dispute period during which any proposal can be challenged and potentially reverted. If a proposal is found to be incorrect, a penalty is levied against the proposer. This mechanism incentivizes users to propose fair and correct redemptions, and allows the community to police and correct any erroneous proposals. 
```
