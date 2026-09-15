<center align="center" style="text-align: center;justify-content:center;">
<div align="center" style="text-align: center;justify-content:center;">
<h1 align="center" style="text-align: center;justify-content:center;">

Prowlarr MCP server

<img style="justify-content:center;text-align: center;width: 95px; height: auto;" width="793" height="411" alt="image" src="https://github.com/user-attachments/assets/abed1a04-d69b-4ab4-a490-d606064df72d" />
<img style="justify-content:center;text-align: center;width: 152px; height: auto;" alt="Prowlarr" src="public/logo.png" />

</h1>


![Version](https://img.shields.io/badge/version-1.0.0-blue.svg?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Prowlarr](https://img.shields.io/badge/Prowlarr-DD9E35?style=for-the-badge&logo=prowlarr&logoColor=white) ![Coverage](https://img.shields.io/badge/API_coverage-128%2F128-brightgreen?style=for-the-badge)

</div>
</center>

<hr>

Run Prowlarr from Claude.ai and Claude Code. All 128 operations of the v1 API are tools, generated from Prowlarr's own OpenAPI document. Not a curated subset: every endpoint Prowlarr's web interface can reach, this can reach.

<hr>

## Why not the other options

Measured against `Prowlarr.Api.V1/openapi.json`, which has 93 paths and 128 non-HEAD operations:

| Server | Prowlarr tools | Coverage |
| --- | --- | --- |
| `davidgibbons/mcp-arr` | 4 | 3 % |
| `GauranshMathur/ARR_MCP` | a handful | partial |
| `bardesss/arr-mcp` | unified verbs across 10 services | partial |
| This one | **128** | **100 %** |

Prowlarr is the worst served of the Servarr apps: every existing server treats it as an afterthought behind Sonarr and Radarr. Nothing else exposes `indexerproxy`, `appprofile`, `indexerstats`, `indexerstatus`, `applications` or the Newznab routes at all.

## How it stays complete

`src/prowlarr_mcp/tools.py` is generated, not written:

```bash
curl -o openapi.json https://raw.githubusercontent.com/Prowlarr/Prowlarr/develop/src/Prowlarr.Api.V1/openapi.json
python scripts/generate_tools.py openapi.json src/prowlarr_mcp/tools.py
```

A test compares every generated call against every operation in the spec, in both directions. An endpoint Prowlarr adds and this misses fails the build; so does a tool pointing at an endpoint the spec does not define.

## Tool names

Verb first, derived from the method and path, so the name says what it does:

| Pattern | Meaning | Example |
| --- | --- | --- |
| `list_*` | Read a collection | `list_indexer`, `list_search` |
| `get_*_by_id` | Read one record | `get_indexer_by_id` |
| `create_*` | POST | `create_indexer`, `create_search` |
| `update_*` | PUT | `update_appprofile_by_id` |
| `delete_*` | DELETE | `delete_indexer_by_id` |

128 tools is a lot to put in front of a model at once. If your client supports tool filtering, narrow it to the groups you use.

## What is covered

Every resource group: `indexer`, `indexerproxy`, `indexerstats`, `indexerstatus`, `applications`, `appprofile`, `downloadclient`, `search`, `history`, `notification`, `command`, `customfilter`, `tag`, `health`, `log`, `filesystem`, `localization`, `update`, `system` and the config endpoints, plus the Newznab compatibility routes.

## Setup

```bash
git clone https://github.com/rollecode/prowlarr-mcp.git
cd prowlarr-mcp
uv venv && uv pip install -e .
```

```bash
export PROWLARR_URL=http://127.0.0.1:9696
export PROWLARR_API_KEY=...   # Settings, General, Security
```

### Claude Code

```bash
claude mcp add prowlarr -- /path/to/prowlarr-mcp/.venv/bin/prowlarr-mcp
```

## Writing records

Prowlarr replaces a record on PUT rather than merging, so read it first, change the fields you want and send the whole object back as `body`. For a new indexer, `list_indexer_schema` returns every definition Prowlarr knows and the fields each one needs.

## Development

```bash
uv pip install -e . pytest ruff
.venv/bin/python -m pytest tests
.venv/bin/ruff check .
```

