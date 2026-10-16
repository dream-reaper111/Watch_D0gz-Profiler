# Watch_D0gz-Profiler
old code me and my buddy programmed back in 2017
# Watch_D0gz-Profiler

> Legacy OSINT / reconnaissance profiling tool originally written in 2017.

![Status](https://img.shields.io/badge/status-legacy%20project-darkred)
![Python](https://img.shields.io/badge/python-3.x-blue)
![License](https://img.shields.io/badge/use-educational%20%7C%20authorized-orange)
![Year](https://img.shields.io/badge/original-2017-black)

---

## Overview

**Watch_D0gz-Profiler** is an old profiling / reconnaissance project that a friend and I originally worked on back in **2017**.

The original goal was to experiment with basic information gathering, username correlation, public-data collection, and Python automation.

This repository is being preserved as a piece of old code, but it may eventually be rebuilt into a cleaner and more modern OSINT framework.

<img width="498" height="498" alt="wrench-watch-dogs" src="https://github.com/user-attachments/assets/7e1d1c9b-d04c-4ce3-9b4e-e5f85f8a1997" />
<img width="244" height="244" alt="watch-dogs-mask" src="https://github.com/user-attachments/assets/b47c2b6c-428d-4f4b-974b-98ed8ba60b91" />



```text
 __        __    _       _       ____   ___
 \ \      / /_ _| |_ ___| |__   |  _ \ / _ \  __ _ ____
  \ \ /\ / / _` | __/ __| '_ \  | | | | | | |/ _` |_  /
   \ V  V / (_| | || (__| | | | | |_| | |_| | (_| |/ /
    \_/\_/ \__,_|\__\___|_| |_| |____/ \___/ \__, /___|
                                               |___/

              W A T C H _ D 0 G Z
                 P R O F I L E R
Original Project
The original version was built as a simple experimentation platform for:
- Python scripting
- Username discovery
- Search automation
- Public profile research
- Basic reconnaissance
- Terminal-based output
- Early OSINT concepts
The old code is intentionally preserved.
It represents the original version of the project and should remain available even if the codebase is completely rewritten.
Repository Philosophy
The future version should follow several design rules:
1. Preserve the original 2017 code.
2. Separate collection from analysis.
3. Use modular providers instead of one large script.
4. Store normalized data.
5. Keep correlation probabilistic.
6. Prefer passive/public intelligence sources.
7. Add rate limiting and responsible collection controls.
8. Allow users to run the system entirely locally.
9. Support both CLI and web interfaces.
10. Keep each feature independently replaceable.



Watch_D0gz-Profiler/
│
├── legacy/
│   └── profiler_2017.py
│
├── watchdog/
│   ├── __init__.py
│   ├── cli.py
│   │
│   ├── core/
│   │   ├── engine.py
│   │   ├── config.py
│   │   ├── logging.py
│   │   ├── scheduler.py
│   │   ├── rate_limit.py
│   │   └── exceptions.py
│   │
│   ├── models/
│   │   ├── target.py
│   │   ├── profile.py
│   │   ├── account.py
│   │   ├── domain.py
│   │   ├── evidence.py
│   │   └── relationship.py
│   │
│   ├── modules/
│   │   ├── username/
│   │   ├── github/
│   │   ├── domain/
│   │   ├── metadata/
│   │   ├── exposure/
│   │   ├── threat_intel/
│   │   └── search/
│   │
│   ├── correlation/
│   │   ├── scoring.py
│   │   ├── clustering.py
│   │   └── similarity.py
│   │
│   ├── graph/
│   │   ├── builder.py
│   │   └── export.py
│   │
│   ├── reporting/
│   │   ├── json_report.py
│   │   ├── csv_report.py
│   │   ├── markdown_report.py
│   │   ├── html_report.py
│   │   └── pdf_report.py
│   │
│   ├── database/
│   │   ├── models.py
│   │   └── storage.py
│   │
│   └── api/
│       └── server.py
│
├── web/
├── plugins/
├── tests/
├── docs/
├── examples/
├── reports/
│
├── README.md
├── ROADMAP.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── requirements.txt
├── pyproject.toml
└── LICENSE





Development Roadmap
Phase 0 — Preserve the Original
Before major development begins, freeze the original version.
Recommended steps:
git tag v0.1-legacy
git push origin v0.1-legacy

Move the original profiler into:
legacy/profiler_2017.py

Goals:
- Preserve historical code
- Maintain the original behavior
- Allow future comparison
- Prevent the rewrite from destroying the legacy version
Suggested status:
Original Code : Archived
Rewrite       : Planned
Original Year : 2017

Phase 1 — Core Rewrite
Replace the monolithic script with a modular engine.
Core responsibilities:
Target handling
Configuration
Logging
Module loading
Request management
Result normalization
Error handling
Rate limiting

Create a shared module interface.
Example:
class ReconModule:    name = "base"    async def scan(self, target):        raise NotImplementedError


Future modules inherit from this interface.
Example:
class GitHubModule(ReconModule):    name = "github"    async def scan(self, target):        ...


This keeps every feature independent.
Phase 2 — Modern CLI
Create a clean command-line interface.
Potential libraries:
Typer
Rich
Pydantic

Example commands:
watchdog username deadbyte
watchdog github deadbyte
watchdog domain example.com
watchdog metadata image.jpg
watchdog exposure deadbyte
watchdog report scan.json
watchdog graph scan.json
watchdog history deadbyte

Possible CLI menu:
╭──────────────────────────────────────────────╮
│            WATCH_D0GZ PROFILER               │
│              Recon Engine v2                 │
╰──────────────────────────────────────────────╯

[01] Username Scan
[02] GitHub Intelligence
[03] Domain Recon
[04] Metadata Analysis
[05] Exposure Audit
[06] Threat Intelligence
[07] Graph Analysis
[08] Generate Report
[09] Scan History
[10] Configuration

Phase 3 — Username Intelligence Engine
Build a dedicated username discovery engine.
Example:
watchdog username example_user

Possible categories:
Development
├── GitHub
├── GitLab
├── Codeberg
├── Docker Hub
└── Dev.to

Social
├── Reddit
├── Bluesky
├── Mastodon
└── Twitch

Gaming
├── Steam
├── Chess.com
└── other public profiles

Suggested result format:
USERNAME SCAN

Target: example_user

GitHub      FOUND
GitLab      FOUND
Reddit      FOUND
Twitch      NOT FOUND
Steam       FOUND

Accounts Found: 4
Sources Checked: 5

Each service should have its own adapter.
modules/
└── username/
    ├── github.py
    ├── gitlab.py
    ├── reddit.py
    ├── steam.py
    └── twitch.py

Phase 4 — Async Recon Engine
Move network requests to asynchronous execution.
Recommended:
asyncio
httpx

Concept:
results = await asyncio.gather(    github.scan(target),    reddit.scan(target),    gitlab.scan(target),)


Benefits:
- Faster scans
- Better handling of large provider lists
- Lower idle time
- Cleaner concurrency controls
Important controls:
Maximum concurrent requests
Per-provider rate limits
Retry delays
Timeouts
Backoff handling
Provider-specific throttling

Phase 5 — Normalized Intelligence Model
Every module should return standardized objects.
Example:
{
  "platform": "github",
  "username": "example_user",
  "found": true,
  "display_name": "Example User",
  "bio": "Security Research",
  "url": "https://example.invalid",
  "public_links": [],
  "confidence": 0.95
}

Suggested object model:
Target
Account
Profile
Domain
Artifact
Source
Evidence
Relationship
Scan
Report

Normalization is important because later phases will depend on it.
Phase 6 — Profile Correlation Engine
Compare public profiles and estimate whether they may represent the same public identity.
Possible signals:
Username similarity
Display-name similarity
Public website matches
Avatar perceptual similarity
Bio similarity
Repository names
Public social links
Shared public domains
Cross-linked accounts
Account creation timing

Example:
PROFILE CORRELATION

GitHub <-> GitLab
Confidence: 94%

GitHub <-> Reddit
Confidence: 73%

GitHub <-> Steam
Confidence: 37%

Example weighted score:
Username similarity     30%
Website match           25%
Avatar similarity       20%
Cross-linked profile    15%
Bio similarity          10%

The output should remain probabilistic.
Use:
Possible match
Probable match
Strong correlation
Low confidence

rather than presenting uncertain matches as fact.
Phase 7 — Graph Visualization Engine
Create a relationship graph from collected intelligence.
Possible libraries:
NetworkX
Graphviz
PyVis
Cytoscape.js

Example:
                    Website
                       |
                       |
GitHub ----------- Username ----------- Reddit
  |                    |
  |                    |
GitLab                Steam
  |
Domain

Command:
watchdog graph scan.json

Possible output:
reports/graph.html

Future graph features:
Clickable nodes
Relationship confidence
Source attribution
Timeline overlays
Account clusters
Domain links
Color-coded node types
Filtering
Search
Zoom
Export to PNG/SVG

Phase 8 — Domain Reconnaissance
Add passive intelligence for domains.
Command:
watchdog domain example.com

Potential modules:
DNS
RDAP
WHOIS
MX
TXT records
SPF
DMARC
DKIM
TLS certificate information
Certificate Transparency
HTTP headers
Technology fingerprinting
Passive subdomain discovery

Example:
DOMAIN PROFILE

Target: example.com

DNS
A       203.0.113.15
MX      mail.example.com

Security
SPF     PRESENT
DMARC   PRESENT
DKIM    PRESENT

TLS
Issuer  Example CA
Status  VALID

Phase 9 — GitHub Intelligence
Create a specialized GitHub reconnaissance module.
Command:
watchdog github username

Collect public information including:
Repositories
Programming languages
Repository topics
Stars
Forks
Organizations
Public Gists
Contribution activity
Public website
Public profile links
Repository descriptions

Potential report:
GITHUB INTELLIGENCE

Repositories: 47

Primary Languages:

Python       46%
C#           25%
JavaScript   18%
C++          11%

Common Topics:

Security
Automation
Networking
AI
OSINT
Trading

Phase 10 — Metadata Analyzer
Add metadata inspection for files supplied by the user.
Command:
watchdog metadata image.jpg

or:
watchdog metadata document.pdf

Potential metadata:
EXIF
Camera model
Software
Creation timestamps
Modification timestamps
Document author
PDF producer
GPS metadata
Embedded file information
Image dimensions

Example:
METADATA REPORT

File:
photo.jpg

Camera:
Example Camera

Software:
Example Editor

Timestamp:
2026-10-16 15:04:44

GPS Metadata:
Present

This module can also provide privacy recommendations.
Phase 11 — Exposure Audit
Create a defensive profile exposure score.
Command:
watchdog exposure example_user

Potential categories:
Username reuse
Number of public accounts
Public email exposure
Metadata exposure
Domain exposure
Profile correlation
Developer activity
Public link reuse

Example:
WATCH_D0GZ EXPOSURE SCORE

Username reuse       8/10
Email exposure       3/10
Metadata exposure    2/10
Domain exposure      4/10
Profile correlation  7/10

Overall Exposure:
48 / 100

Classification:
MODERATE

The purpose of the score should be defensive:
Personal OPSEC
Privacy review
Security awareness
Public footprint analysis

Phase 12 — Reporting Engine
All scans should support export.
Formats:
JSON
CSV
Markdown
HTML
PDF

Example:
watchdog username example_user \
    --format html \
    --output reports/example_user.html

Reports should include:
Executive Summary
Target
Scan Date
Sources Checked
Accounts Found
Evidence
Correlation Scores
Domain Intelligence
Exposure Score
Graph
Recommendations
Raw Results

Phase 13 — Database Layer
Store scan history.
Start with:
SQLite

Optional future support:
PostgreSQL

Potential tables:
targets
profiles
accounts
domains
artifacts
scans
relationships
evidence
sources
reports

Example:
watchdog history example_user

Output:
SCAN HISTORY

2026-10-16
Accounts: 12

2026-11-01
Accounts: 15

2027-01-04
Accounts: 17

Phase 14 — Historical Change Detection
Compare scans over time.
Command:
watchdog compare scan1.json scan2.json

Example:
PROFILE CHANGES

Previous:
2026-10-16

Current:
2026-11-21

Changes:

+ New public GitLab profile
+ New GitHub repository
~ GitHub bio changed
~ Public website changed
- Reddit profile unavailable

Potential uses:
Personal OPSEC monitoring
Brand monitoring
Defensive security
Asset inventory
Public profile tracking
Threat intelligence

Phase 15 — REST API
Expose the engine through an API.
Recommended stack:
FastAPI
Pydantic
Uvicorn

Potential endpoints:
POST /scan/username
POST /scan/github
POST /scan/domain
POST /scan/metadata
POST /scan/exposure

GET /scan/{id}
GET /report/{id}
GET /graph/{id}
GET /target/{id}

The API allows multiple clients to use the same backend.
Phase 16 — Web Dashboard
Create a browser-based dashboard.
Possible architecture:
Frontend
React
Next.js

Backend
FastAPI

Database
PostgreSQL

Cache
Redis

Graph
Cytoscape.js

Possible dashboard:
┌─────────────────────────────────────────────────────┐
│ WATCH_D0GZ                                         │
├──────────────┬──────────────────────────────────────┤
│              │                                      │
│ Dashboard    │          PROFILE GRAPH               │
│ Targets      │                                      │
│ Scans        │              ● GitHub                │
│ Graph        │             /                         │
│ Reports      │        ● TARGET ── ● Reddit          │
│ Modules      │             \                         │
│ History      │              ● GitLab                │
│ Settings     │                                      │
│              │                                      │
├──────────────┴──────────────────────────────────────┤
│ Accounts 12    Domains 3    Exposure 46/100        │
└─────────────────────────────────────────────────────┘

Phase 17 — Plugin Framework
Create a plugin system.
Structure:
plugins/
├── github/
│   └── plugin.py
│
├── reddit/
│   └── plugin.py
│
├── gitlab/
│   └── plugin.py
│
└── custom_source/
    └── plugin.py

Possible plugin interface:
class WatchdogPlugin:    name = "example"    async def scan(self, target):        ...    def normalize(self, result):        ...


Commands:
watchdog plugins list
watchdog plugins enable github
watchdog plugins disable reddit

Example:
PLUGIN             STATUS

github             enabled
reddit             enabled
gitlab             enabled
steam              enabled
metadata           enabled

Phase 18 — AI-Assisted Analysis
Add AI after the data pipeline is reliable.
AI should analyze information already collected by the system.
Possible commands:
watchdog analyze report.json

Possible jobs:
Summarize scan results
Explain account clusters
Highlight OPSEC risks
Summarize public developer activity
Explain graph relationships
Generate defensive recommendations
Compare historical scans
Summarize domain exposure
Categorize repositories

Example:
WATCH_D0GZ ANALYSIS

The strongest correlation exists between the
GitHub and GitLab profiles.

Supporting indicators include:

- highly similar usernames
- matching public website
- overlapping repository names
- similar avatar hashes

Estimated correlation:
92%

Primary public exposure appears to originate
from username reuse across developer platforms.

Phase 19 — Local AI / LLM Support
Allow AI analysis to run locally.
Potential support:
Ollama
llama.cpp
LM Studio
OpenAI-compatible local APIs

Example config:
ai:

  provider: ollama

  model: qwen

  endpoint: http://localhost:11434

Benefits:
Privacy
Offline analysis
No external API requirement
Custom models
Lower operational cost

Phase 20 — Threat Intelligence Mode
Expand beyond public profiles into defensive indicator research.
Commands:
watchdog intel domain example.com
watchdog intel ip 203.0.113.10
watchdog intel hash <hash>
watchdog intel url example.com

Potential integrations:
VirusTotal
AlienVault OTX
AbuseIPDB
URLhaus
MalwareBazaar
CISA KEV
NVD
MITRE ATT&CK
Shodan
Censys

Possible report:
THREAT INTELLIGENCE REPORT

Indicator:
203.0.113.10

Reputation:
Suspicious

Observed Sources:
OTX
AbuseIPDB
Threat Feed

Confidence:
Medium

Passive intelligence should remain the default behavior.
Phase 21 — Timeline Intelligence
Build timelines from historical public data.
Example:
2024
|
+-- GitHub account created
|
2025
|
+-- Public domain appeared
|
2026
|
+-- GitLab profile discovered
|
+-- Website changed
|
2027
|
+-- New repository cluster

Potential command:
watchdog timeline example_user

Timeline data could come from:
Account creation
Repository creation
Domain changes
Public profile changes
Scan history
Metadata timestamps

Phase 22 — Evidence Tracking
Every discovered item should contain evidence metadata.
Example:
{
  "source": "github",
  "observed_at": "2026-10-16T15:00:00Z",
  "confidence": 0.91,
  "type": "public_profile",
  "collector": "github_plugin"
}

This makes results auditable.
Potential evidence fields:
Source
Timestamp
Collector
Confidence
Raw result reference
Normalized value
Relationship

Phase 23 — Provider Health Monitoring
Public websites and APIs constantly change.
Add automated provider health tests.
Example:
PROVIDER STATUS

GitHub       ONLINE
GitLab       ONLINE
Reddit       DEGRADED
Steam        ONLINE
Twitch       RATE LIMITED

Command:
watchdog providers test

This makes maintenance much easier.
Phase 24 — Search Engine Integration
Add optional public search engine providers.
Possible providers:
Brave Search
DuckDuckGo
Bing
Google Custom Search API

Command:
watchdog search "example_username"

Search results could be normalized into:
URL
Title
Source
Timestamp
Matched term
Category

Phase 25 — Avatar Similarity
Add public avatar correlation using perceptual hashing.
Potential libraries:
Pillow
imagehash
OpenCV

Example:
AVATAR ANALYSIS

GitHub <-> GitLab
Similarity: 94%

GitHub <-> Reddit
Similarity: 71%

GitHub <-> Steam
Similarity: 21%

This should remain visual similarity analysis, not biometric identity determination.
Phase 26 — Automated Defensive Recommendations
After an exposure scan, provide mitigation guidance.
Example:
RECOMMENDED ACTIONS

[HIGH]
Username reused across 11 public platforms.

Recommendation:
Separate professional and personal usernames.

[MEDIUM]
Public image contains metadata.

Recommendation:
Strip EXIF metadata before public upload.

[LOW]
Public developer profile exposes email.

Recommendation:
Use a dedicated public contact address.

Phase 27 — Scan Profiles
Allow reusable scan templates.
Examples:
quick
standard
developer
domain
privacy
threat-intel
full

Commands:
watchdog scan example_user --profile quick

or:
watchdog scan example_user --profile full

Config:
profiles:

  quick:
    username: true
    github: true

  privacy:
    username: true
    metadata: true
    exposure: true
    correlation: true

  full:
    username: true
    github: true
    domain: true
    correlation: true
    graph: true
    exposure: true

Phase 28 — Configuration System
Create centralized configuration.
Example:
watchdog:

  concurrency: 10

  timeout: 15

  reports:
    format: html

  database:
    engine: sqlite

  ai:
    enabled: false

  providers:

    github:
      enabled: true

    reddit:
      enabled: true

    steam:
      enabled: true

Environment variables should support secrets.
Example:
WATCHDOG_GITHUB_TOKEN=
WATCHDOG_VT_API_KEY=
WATCHDOG_OTX_API_KEY=

Never hard-code API keys.
Phase 29 — Docker Support
Containerize the project.
Files:
Dockerfile
docker-compose.yml
.env.example

Example:
docker compose up

Potential stack:
watchdog-api
watchdog-web
postgres
redis
worker

Phase 30 — Worker Queue
For longer scans, move jobs into workers.
Potential stack:
Celery
RQ
Redis

Architecture:
User
 |
 v
API
 |
 v
Queue
 |
 v
Worker
 |
 v
Collectors
 |
 v
Database

This allows multiple scans to execute independently.
Phase 31 — Authentication
If a web dashboard is added, implement authentication.
Potential features:
Local accounts
Password hashing
Session management
API tokens
Role-based access
Audit logs
Optional MFA

Roles:
Administrator
Analyst
Viewer

Phase 32 — Audit Logging
Track important application events.
Examples:
Scan started
Scan completed
Provider queried
Report generated
Configuration changed
User login
Plugin enabled
Plugin disabled

Example:
2026-10-16T18:03:01
SCAN_START
target=example_user

2026-10-16T18:03:08
SCAN_COMPLETE
results=17

Phase 33 — Testing Framework
Add automated testing.
Suggested stack:
pytest
pytest-asyncio
responses
coverage

Tests:
Module tests
Parser tests
Provider tests
Normalization tests
Correlation tests
CLI tests
API tests
Database tests

Target:
80%+ coverage

Phase 34 — CI/CD
Add GitHub Actions.
Possible workflow:
Push
 |
 v
Lint
 |
 v
Unit Tests
 |
 v
Security Checks
 |
 v
Build
 |
 v
Release

Tools:
GitHub Actions
ruff
black
mypy
pytest
bandit
pip-audit

Phase 35 — Versioning
Use semantic versioning.
Example:
v0.1.0
Legacy archive

v0.2.0
Core rewrite

v0.3.0
Username engine

v0.4.0
Correlation engine

v0.5.0
Graph engine

v0.6.0
Domain intelligence

v0.7.0
Reporting

v0.8.0
Database

v0.9.0
API

v1.0.0
Stable platform

Phase 36 — Documentation Site
Eventually create a documentation site.
Potential tools:
MkDocs
Material for MkDocs
Sphinx

Documentation could include:
Installation
CLI Usage
Modules
API
Plugin Development
Configuration
Reporting
Architecture
Security
Contributing

Phase 37 — Full v1 Architecture
The mature project could look like:
                ┌──────────────────┐
                │       CLI        │
                └────────┬─────────┘
                         │
                ┌────────▼─────────┐
                │       API        │
                └────────┬─────────┘
                         │
                ┌────────▼─────────┐
                │   Recon Engine   │
                └────────┬─────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼

 Username Engine    Domain Engine    Metadata Engine
        │                │                │
        └────────────────┼────────────────┘
                         │
                         ▼

                 Normalization Layer
                         │
                         ▼

                  Correlation Engine
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼

          Database               Graph Engine
              │                     │
              └──────────┬──────────┘
                         │
                         ▼

                  Analysis Engine
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼

          AI Analysis           Reports
                                    │
                                    ▼

                         HTML / PDF / JSON

Long-Term Vision
Watch_D0gz could eventually become less of a single profiler and more of a modular defensive intelligence platform.
Potential final capabilities:
Username intelligence
Public account discovery
Developer intelligence
Domain reconnaissance
Metadata analysis
Profile correlation
Graph visualization
Exposure scoring
Historical monitoring
Change detection
Threat intelligence
Evidence tracking
Timeline generation
AI-assisted analysis
Local LLM support
Web dashboard
REST API
Plugin ecosystem
Reporting
Database history

Potential Command Set
A future stable version could support commands such as:
watchdog scan username deadbyte

watchdog scan github deadbyte

watchdog scan domain example.com

watchdog scan metadata image.jpg

watchdog exposure deadbyte

watchdog graph deadbyte

watchdog timeline deadbyte

watchdog history deadbyte

watchdog compare scan1 scan2

watchdog report deadbyte --format html

watchdog analyze deadbyte

watchdog intel domain example.com

watchdog providers test

watchdog plugins list

Future Feature Checklist
Core
- [ ] Preserve legacy version
- [ ] Rewrite architecture
- [ ] Async engine
- [ ] Unified configuration
- [ ] Structured logging
- [ ] Rate limiting
- [ ] Error handling
Recon
- [ ] Username discovery
- [ ] GitHub intelligence
- [ ] Domain reconnaissance
- [ ] Search engine integration
- [ ] Metadata analysis
- [ ] Passive threat intelligence
Intelligence
- [ ] Profile correlation
- [ ] Similarity scoring
- [ ] Avatar hashing
- [ ] Graph analysis
- [ ] Exposure scoring
- [ ] Timeline generation
- [ ] Evidence tracking
Storage
- [ ] SQLite
- [ ] PostgreSQL
- [ ] Scan history
- [ ] Result caching
- [ ] Historical comparison
Reports
- [ ] JSON
- [ ] CSV
- [ ] Markdown
- [ ] HTML
- [ ] PDF
- [ ] Interactive graphs
Platform
- [ ] CLI
- [ ] REST API
- [ ] Web dashboard
- [ ] Worker queue
- [ ] Docker
- [ ] Plugin ecosystem
AI
- [ ] Report summarization
- [ ] Exposure explanation
- [ ] Graph analysis
- [ ] Scan comparison
- [ ] Local LLM support
- [ ] AI-assisted defensive recommendations
Security
- [ ] API key management
- [ ] Authentication
- [ ] MFA support
- [ ] Role-based access
- [ ] Audit logging
- [ ] Dependency scanning
- [ ] Secrets detection
Development
- [ ] Unit tests
- [ ] Integration tests
- [ ] GitHub Actions
- [ ] Automated releases
- [ ] Semantic versioning
- [ ] Documentation site
- [ ] Contributor guide
Development Priority
A realistic order would be:
1. Preserve legacy code
2. Rewrite core
3. Modern CLI
4. Username engine
5. Async engine
6. Normalize results
7. GitHub module
8. Domain module
9. Correlation engine
10. Reporting
11. Graph engine
12. SQLite history
13. Exposure scoring
14. Change detection
15. Metadata analysis
16. Threat intelligence
17. REST API
18. Web dashboard
19. Plugin system
20. AI analysis
21. Local AI support
22. Production hardening

Milestone Plan
Milestone 1 — Watch_D0gz Legacy
v0.1

Goals:
- Preserve the original profiler
- Clean repository layout
- Document the project
- Add screenshots
- Add roadmap
Milestone 2 — Watch_D0gz Core
v0.2

Goals:
- Modular engine
- Modern Python structure
- Config system
- Logging
- CLI
Milestone 3 — Watch_D0gz Recon
v0.3

Goals:
- Username discovery
- Async scanning
- Provider adapters
- Result normalization
Milestone 4 — Watch_D0gz Intelligence
v0.4

Goals:
- Profile correlation
- Confidence scoring
- GitHub intelligence
- Domain intelligence
Milestone 5 — Watch_D0gz Visualization
v0.5

Goals:
- Relationship graph
- HTML reports
- Interactive visualization
- Exposure score
Milestone 6 — Watch_D0gz History
v0.6

Goals:
- SQLite database
- Scan history
- Change detection
- Timeline generation
Milestone 7 — Watch_D0gz API
v0.7

Goals:
- FastAPI backend
- API authentication
- Background workers
- Database abstraction
Milestone 8 — Watch_D0gz Web
v0.8

Goals:
- Dashboard
- Graph explorer
- Target management
- Report viewer
- Scan history
Milestone 9 — Watch_D0gz Intelligence Platform
v0.9

Goals:
- Threat-intelligence integrations
- Plugin framework
- Provider health system
- Advanced correlation
- AI analysis
Milestone 10 — Watch_D0gz 1.0
v1.0

Goals:
- Stable CLI
- Stable API
- Stable plugin system
- Web dashboard
- Graph engine
- Reporting
- Exposure analysis
- Historical intelligence
- Documentation
- Automated testing
- Production deployment
Installation
For the current legacy version:
git clone https://github.com/YOUR_USERNAME/Watch_D0gz-Profiler.git

cd Watch_D0gz-Profiler

python3 profiler.py

For the eventual modern version:
git clone https://github.com/YOUR_USERNAME/Watch_D0gz-Profiler.git

cd Watch_D0gz-Profiler

python3 -m venv .venv

source .venv/bin/activate

pip install -e .

Run:
watchdog --help

Example Future Usage
watchdog username example_user

watchdog github example_user

watchdog domain example.com

watchdog exposure example_user

watchdog graph example_user

watchdog report example_user --format html

watchdog history example_user

watchdog analyze example_user

Legal / Ethical Use
Watch_D0gz-Profiler is intended for:
- Cybersecurity education
- Security research
- OSINT training
- Personal OPSEC reviews
- Privacy auditing
- Authorized investigations
- CTF environments
- Defensive threat intelligence
- Systems and accounts you own
- Environments where you have permission to perform research
Do not use this project to:
- Harass individuals
- Stalk individuals
- Attempt unauthorized account access
- Collect private data unlawfully
- Circumvent authentication
- Impersonate another person
- Conduct unauthorized intrusive scanning
- Perform credential attacks
Only collect information that is public, intentionally provided to the tool, or explicitly authorized for analysis.
Current Status
Project Name     : Watch_D0gz-Profiler
Original Year    : 2017
Original Version : Legacy
Language         : Python
Current State    : Archive / Modernization Planning
Future Direction : Modular Defensive Intelligence Platform

Project Timeline
2017
|
+-- Original Watch_D0gz profiler created
|
+-- Basic Python reconnaissance
|
+-- Username research
|
+-- Public profile discovery


2026
|
+-- Repository restored
|
+-- Legacy code preserved
|
+-- Documentation rewritten
|
+-- Modern development roadmap created


Future
|
+-- Watch_D0gz Core
|
+-- Watch_D0gz Recon Engine
|
+-- Watch_D0gz Correlation Engine
|
+-- Watch_D0gz Graph Engine
|
+-- Watch_D0gz Exposure Engine
|
+-- Watch_D0gz API
|
+-- Watch_D0gz Web Dashboard
|
+-- Watch_D0gz Threat Intelligence
|
+-- Watch_D0gz AI Analysis
|
+-- Watch_D0gz v1.0

Authors
Originally developed in 2017 as a Python security and reconnaissance experiment.
Modernization maintained by:
DeadByte.dll
Final Goal
The original Watch_D0gz was a small profiling script.
The future Watch_D0gz could become:
                 WATCH_D0GZ

        PUBLIC INTELLIGENCE COLLECTION

                       +

             PROFILE CORRELATION

                       +

               GRAPH ANALYSIS

                       +

             EXPOSURE SCORING

                       +

            HISTORICAL ANALYSIS

                       +

             THREAT INTELLIGENCE

                       +

              AI ASSISTANCE

                       =

       DEFENSIVE INTELLIGENCE PLATFORM

The old code stays.
The architecture evolves.
The Watch_D0gz wakes back up.
```
