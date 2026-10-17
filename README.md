# Hi, I'm Anish

I build backend services, and I work out where AI-generated code goes wrong.

That second part is my actual job. At **Handshake** I write software engineering
tasks that are used to test AI coding agents, then grade the code they produce.
Before that I designed CFD/OpenFOAM tasks at **Alignerr** and worked on LLM
post-training at **Ethara AI**. Writing a task properly means building the
environment it runs in and the verifier that decides whether an agent really
solved it - not just describing the problem.

## Open source

**[BasedHardware/omi](https://github.com/BasedHardware/omi)** - the Python CLI
for the Omi wearable. Both reviewed and approved:

- [#13202](https://github.com/BasedHardware/omi/pull/13202) - `memory create-batch`
  from a UTF-8 JSON file, with BOM handling and a preflight that rejects
  over-long entries before any HTTP request. 16 tests.
- [#13192](https://github.com/BasedHardware/omi/pull/13192) - a `--file` option
  for `memory create`, mapping every file-read failure to a usage error instead
  of a traceback. 18 tests.

Four more open, each a bug found by reading the code and shipped with the
regression test that fails without the fix:

- [#22007](https://github.com/BasedHardware/omi/pull/22007) - an IPv4-mapped
  address slips past the webhook delivery check, so `webhook verify` reports
  `pass` for a URL Omi silently drops.
- [#22008](https://github.com/BasedHardware/omi/pull/22008) - a 429 reports the
  rate-limit policy as its own budget (`dev:ask (dev:ask)`), which hit 13 of the
  16 real policies.
- [#22009](https://github.com/BasedHardware/omi/pull/22009) - an unreadable
  config file crashes every command, including `omi version`, and leaves the
  guard that protects it disarmed.
- [#22010](https://github.com/BasedHardware/omi/pull/22010) - length limits the
  CLI declares and documents were never actually enforced.

**[harbor-framework/terminal-bench](https://github.com/harbor-framework/terminal-bench/pull/1908)** -
a task I authored for measuring coding agents: a Python 2.7 batch ledger system
ported to Python 3 byte-exactly, shipped as a Docker environment plus a verifier
that runs 16 hidden input corpora against golden outputs. 276 files.

## Shipped and live

**[exactsizetool.com](https://exactsizetool.com)** - resizes exam photos and
signatures to an exact KB target, for Indian government application forms that
reject anything outside a narrow byte range.

**[gateguide.co.in](https://gateguide.co.in)** - GATE 2027 preparation books
across CSE, ECE, EE, ME, Civil and Data Science.

**[anishahamad.com](https://anishahamad.com)** - my portfolio. Hand-written, no
template.

## Projects

**[incident-engineer](https://github.com/anishraja04/incident-engineer)** - two
agents that find and fix real bugs. A fix is only accepted once the full test
suite passes. 11 of 11 incidents resolved, against 0 of 11 for a single-prompt
baseline.

**[team-task-manager](https://github.com/anishraja04/team-task-manager)** -
KaamSathi. Django REST, React and PostgreSQL with JWT auth and role-based
access. Live on Railway.

**[ai_resume_generator](https://github.com/anishraja04/ai_resume_generator)** -
Spring Boot REST API with a React front end and a pluggable LLM backend.

**[mermail-expense-tracker](https://github.com/anishraja04/mermail-expense-tracker)** -
an MCP skill that turns receipt emails into an expense ledger. Treats every
email as untrusted input.

**[cloud-native-devops](https://github.com/anishraja04/cloud-native-devops)** -
Terraform for an AWS VPC and EC2, a Dockerised app behind Nginx, and GitHub
Actions deploying on every push.

**[api-etl-pipeline](https://github.com/anishraja04/api-etl-pipeline)** - pulls
records from external REST APIs, cleans up the JSON and loads it into
PostgreSQL. FastAPI.

## What I work with

**Languages** Python, Java, SQL, JavaScript
**Backend** FastAPI, Spring Boot, Django REST, REST API design
**Data** PostgreSQL, MySQL, MongoDB
**Infra** Docker, GitHub Actions, Terraform, AWS (EC2, VPC), Linux
**AI** LLM evaluation, agent architecture, task and verifier design, LangGraph,
FAISS, MCP

## Find me

- Portfolio: [anishahamad.com](https://anishahamad.com)
- LinkedIn: [md-anish-ahamad](https://linkedin.com/in/md-anish-ahamad)
- Email: mdanisahamad2003@gmail.com
