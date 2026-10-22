<h1 align="center">Md Anish Ahamad</h1>

<p align="center">
  AI evaluation &nbsp;·&nbsp; task and verifier authoring &nbsp;·&nbsp; backend engineering
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/anishraja04/anishraja04/main/assets/typewriter-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/anishraja04/anishraja04/main/assets/typewriter-light.svg" />
    <img src="assets/typewriter-light.svg" width="567" alt="I make agents prove it." />
  </picture>
</p>

<p align="center">
  I turn domain problems into executable benchmark tasks: the environment, the<br/>
  reference solution and the scorer, across data engineering, STEM and CFD.
</p>

<p align="center">
  <a href="https://github.com/BasedHardware/omi/pulls?q=is%3Apr+author%3Aanishraja04"><img src="https://img.shields.io/badge/omi_CLI-6_pull_requests-0B6477?style=for-the-badge&logo=github&logoColor=white" height="26" alt="omi pull requests" /></a>&nbsp;
  <a href="https://github.com/search?q=is%3Apr+author%3Aanishraja04&type=pullrequests"><img src="https://img.shields.io/badge/Open_source-PRs-24292F?style=for-the-badge&logo=git&logoColor=white" height="26" alt="Open-source pull requests" /></a>&nbsp;
  <a href="https://anishahamad.com"><img src="https://img.shields.io/badge/Portfolio-anishahamad.com-18A05F?style=for-the-badge&logo=firefox&logoColor=white" height="26" alt="Portfolio" /></a>
</p>

<p align="center"><em>Every claim on this page links to something you can open and check.</em></p>

---

## Benchmark & evaluation work

My day job is adversarial: take a domain problem, turn it into an executable task, then build the
scorer that decides whether an agent genuinely solved it or merely looked like it did.

| Where | Benchmark | What |
| --- | --- | --- |
| **Handshake AI** · Project Dynamo | Terminal-Bench 2 | Benchmark task development, authoring tasks that evaluate AI agents working in terminal environments. |
| **Handshake AI** · Project Insight | Terminal-Bench 4 | Benchmark task development, hands-on across task authoring and grading agent output. |
| **Handshake AI** · Project LUMIERE | STEM (Engineering) | Engineering-domain task authoring, where a correct answer has to come from the underlying physics rather than from pattern-matching the prompt. |
| **Imperium** (via Mercor) | Real World Engineering | Data Engineering task author for long-horizon engineering tasks. |
| **Alignerr** | | CFD task design on **OpenFOAM**, turning simulation problems into checkable engineering tasks. |
| **Ethara AI** | | LLM post-training. |

**Domains I have authored in:** data engineering · STEM and engineering · computational fluid dynamics

### What a task package actually contains

The problem statement is the easy part. A task is only usable as an eval when all five pieces hold
together:

| Piece | Why it decides whether the task is worth anything |
| --- | --- |
| **Runnable environment** | Containerised and deterministic. If it drifts between runs, every score it produces is noise. |
| **Instructions** | Unambiguous about the goal and silent about the method, or you are testing reading comprehension instead of engineering. |
| **Automated scorer** | Checks the outcome, not the shape of the output. String-matching a solution grades style, not correctness. |
| **Reference solution** | Proves the task is solvable at all, and sets the ceiling the scorer must award full marks to. |
| **Validation evidence** | Shows the whole thing behaves: reference scores full, a no-op scores zero, and the gap between them is real. |

### How I calibrate

A task that every agent passes measures nothing, and one that nothing can pass is usually a broken
verifier rather than a hard problem. So the first job after building is to attack my own task:

- **Both ends pinned.** The reference solution must score full marks and a do-nothing attempt must
  score zero. If the no-op scores above zero, the scorer is reading something it should not.
- **Near-misses must fail.** A plausible, confidently-wrong answer is the case that matters. If it
  passes, the scorer is checking appearance rather than outcome.
- **Hidden cases stay hidden.** Grading assets and expected outputs live outside the environment the
  agent can see. An agent that can read the answer key is not being evaluated.
- **Failure analysis separates causes.** When an agent fails, the question is whether it reasoned
  badly, whether the verifier is wrong, or whether the infrastructure broke. Grading agent output at
  Handshake is mostly this: reading trajectories and telling those three apart.

The part that matters is not the problem statement. It is the environment that runs reproducibly, the
reference solution, and a scorer strict enough that a plausible-looking wrong answer still fails.

---

## Open source: found by reading the code

My contributions to [**BasedHardware/omi**](https://github.com/BasedHardware/omi), the Python CLI for
the Omi wearable, are all the same shape: a defect nobody had reported, found by reading the code,
fixed in one narrow diff, and shipped with the regression test that fails without it. The live list
below is generated from the GitHub API, so it is current rather than something I remembered to update.

Four of them, to show what that means in practice:

- An IPv4-mapped address slipped past the webhook delivery check, so `omi app webhook verify` printed
  **pass** for a URL the backend silently drops. The rule was written for one spelling of an address
  and `::ffff:100.64.0.1` is another.
- A 429 reported the rate-limit policy as its own budget, `dev:ask (dev:ask)`, because the lookup
  defaulted to its own key. The table held 3 of the 16 policies the backend actually defines, so this
  fired on most real rate limits.
- An unreadable config file crashed **every** command, `omi version` included, and left the guard
  that protects it disarmed. The function documented the opposite behaviour; the file open just sat
  outside the `try`.
- `b64decode(validate=True)` rejects newlines, so a line-wrapped screenshot payload, which is what
  every MIME encoder produces, was refused as corrupt data.

> A maintainer on #13192: *"clean, narrow change with genuinely good test coverage."*

**Terminal-Bench task: legacy ledger migration.**
[A task I authored](https://github.com/harbor-framework/terminal-bench/pull/1908): a Python 2.7 batch
ledger system ported to Python 3 **byte-exactly**. BAI, CSV and fixed-width ingest, a reconciliation
engine, a Docker environment, and a scorer running 16 hidden input corpora against golden outputs.
276 files.

---

## Live activity

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/anishraja04/anishraja04/main/assets/activity-card-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/anishraja04/anishraja04/main/assets/activity-card-light.svg" />
    <img src="assets/activity-card-light.svg" width="620" alt="Open-source contribution summary" />
  </picture>
</p>

<!-- activity:start -->

**11 pull requests** to repositories I do not own · 8 merged · 2 open

**[BasedHardware/omi](https://github.com/BasedHardware/omi)**

- [#22618 fix: accept line-wrapped base64 when saving a screenshot](https://github.com/BasedHardware/omi/pull/22618) `MERGED`
- [#22617 fix: keep browser login working when the dev-keys API answers oddly](https://github.com/BasedHardware/omi/pull/22617) `MERGED`
- [#22610 fix: report a refused config overwrite as an error, not an unexpected one](https://github.com/BasedHardware/omi/pull/22610) `MERGED`
- [#22609 fix: stop a non-JSON key response crashing omi auth login](https://github.com/BasedHardware/omi/pull/22609) `MERGED`
- [#22010 harden: enforce the conversation length bounds the CLI already declares](https://github.com/BasedHardware/omi/pull/22010) `MERGED`
- [#22009 fix: record an unreadable config instead of raising out of load()](https://github.com/BasedHardware/omi/pull/22009) `MERGED`
- [#22008 fix: stop reporting an unknown rate-limit policy as its own budget](https://github.com/BasedHardware/omi/pull/22008) `MERGED`
- [#22007 fix: classify IPv4-mapped addresses in the webhook target check](https://github.com/BasedHardware/omi/pull/22007) `MERGED`
- [#13202 python-cli: add memory create-batch from UTF-8 JSON file](https://github.com/BasedHardware/omi/pull/13202) `OPEN`
- [#13192 python-cli : file option to omi memory create](https://github.com/BasedHardware/omi/pull/13192) `OPEN`

**[harbor-framework/terminal-bench](https://github.com/harbor-framework/terminal-bench)**

- [#1908 Add legacy-ledger-migration task: Python 2.7 batch to Python 3 byte-exact port](https://github.com/harbor-framework/terminal-bench/pull/1908) `CLOSED`

<sub>Updated automatically from the GitHub API. Self-authored pull requests are excluded.</sub>

<!-- activity:end -->

---

## Shipped and live

| Product | What it does |
| --- | --- |
| **[exactsizetool.com](https://exactsizetool.com)** | Resizes exam photos and signatures to an exact KB target, for Indian government forms that reject anything outside a narrow byte range. |
| **[gateguide.co.in](https://gateguide.co.in)** | GATE 2027 preparation books across CSE, ECE, EE, ME, Civil and Data Science. |
| **[anishahamad.com](https://anishahamad.com)** | My portfolio. Hand-written, no template. |

---

## Projects

**[incident-engineer](https://github.com/anishraja04/incident-engineer)** - two agents that find and fix
real bugs. A fix is only accepted once the full test suite passes. **11 of 11** incidents resolved,
against **0 of 11** for a single-prompt baseline. The gate is the point: the agent does not get to
declare its own success.

**[team-task-manager](https://github.com/anishraja04/team-task-manager)** - KaamSathi. Django REST,
React and PostgreSQL with JWT auth and role-based access. Live on Railway.

**[ai_resume_generator](https://github.com/anishraja04/ai_resume_generator)** - Spring Boot REST API,
React front end, pluggable LLM backend.

**[mermail-expense-tracker](https://github.com/anishraja04/mermail-expense-tracker)** - an MCP skill
turning receipt emails into an expense ledger. Treats every email as untrusted input.

**[cloud-native-devops](https://github.com/anishraja04/cloud-native-devops)** - Terraform for an AWS VPC
and EC2, a Dockerised app behind Nginx, GitHub Actions deploying on every push.

**[api-etl-pipeline](https://github.com/anishraja04/api-etl-pipeline)** - pulls records from external
REST APIs, cleans the JSON, loads it into PostgreSQL. FastAPI.

<details>
<summary><strong>Smaller repositories</strong></summary>

<br/>

Prototypes and practice projects, listed honestly as such, a few hundred lines each, not systems:
[document-rag-system](https://github.com/anishraja04/document-rag-system) (FastAPI, sentence-transformers,
FAISS), [multi-agent-assistant](https://github.com/anishraja04/multi-agent-assistant) (LangGraph),
[concurrent-task-processor](https://github.com/anishraja04/concurrent-task-processor) (Java concurrency,
with tests), [backend-order-system](https://github.com/anishraja04/backend-order-system) (Spring Boot,
Docker, GitHub Actions deploy), [lean4-formal-proofs](https://github.com/anishraja04/lean4-formal-proofs)
(Lean 4 foundations).

</details>

---

## Stack

| | |
| --- | --- |
| **Languages** | Python · Java · SQL · JavaScript |
| **Backend** | FastAPI · Spring Boot · Django REST · REST API design |
| **Data** | PostgreSQL · MySQL · MongoDB |
| **Infra** | Docker · GitHub Actions · Terraform · AWS (EC2, VPC) · Linux |
| **Evaluation** | Task and verifier design · reproducible environments · scorer calibration · failure analysis |
| **Simulation** | OpenFOAM · CFD task design |

### Currently learning

Kubernetes · CUDA and GPU kernel profiling · Lean 4 for certificate-based verification · distributed
data processing at scale

---

## Find me

[anishahamad.com](https://anishahamad.com) · [LinkedIn](https://linkedin.com/in/md-anish-ahamad) · mdanisahamad2003@gmail.com

B.Tech Computer Science, Noida Institute of Engineering and Technology, 2026
