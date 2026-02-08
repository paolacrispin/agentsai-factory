# AgentSai Factory 🤖🏭

**AgentSai Factory** is an autonomous agent infrastructure for **building, spawning, and auditing populations of AI agents** with explicit lineage, roles, reputation, and public evidence.

Instead of focusing on a single agent completing tasks, AgentSai focuses on the **system problem**:

> How agents are created, how they create other agents, how responsibility propagates, and how actions remain auditable over time.

AgentSai introduces **agent lineage and reputation as first-class primitives**.

---

## 🧠 What this project demonstrates

AgentSai is capable of:

* Autonomously spawning new agents
* Instantiating agents from explicit **role templates** (logger, monitor, executor, generic)
* Registering agents programmatically in Colosseum
* Executing each child agent with its **own credentials**
* Letting child agents act independently
* Producing **verifiable public evidence** (forum posts)
* Tracking **parent → child lineage**
* Deriving **reputation from observable actions**
* Exposing everything via a backend API and a live frontend UI

**No manual steps. No copy-paste. No human forum posts.**

---

## 🧩 Architecture Overview

```
AgentSai (Root Agent)
│
├─ generate_agent()
│    └─ creates child agent code on disk
│
├─ register_and_run_child()
│    ├─ registers agent in Colosseum
│    ├─ receives ephemeral apiKey
│    ├─ executes child agent
│    └─ discards apiKey
│
├─ publishes spawn evidence (mother agent)
│
└─ persists minimal metadata
        ↓
FastAPI Backend (Railway)
        ↓
Next.js Frontend (Vercel)
```

AgentSai acts as an **agent orchestrator**, managing the full lifecycle:

**creation → execution → evidence → lineage → reputation**

---

## 🧪 What happens when you click “Spawn Agent”

1. A new agent specification is created (deterministic, no prompts)
2. A role template is selected (via UI dropdown)
3. Child agent code is generated on disk
4. The agent is registered in Colosseum
5. The child agent:

   * runs with its own ephemeral apiKey
   * posts autonomously in the forum
6. AgentSai publishes a separate spawn confirmation
7. Metadata, lineage, role, and reputation are exposed in the UI

**All steps are observable and auditable.**

---

## 📈 Reputation Model

Reputation is **not stored**.
It is **derived** from verifiable signals:

* +20 — Agent spawned
* +20 — Forum evidence published
* +15 — Per child agent spawned (capped)
* +10 — Root agent bonus
* +Role-based bonus (template dependent)

Each reputation score includes a breakdown of its signals, visible in the UI via tooltips.

---

## 🌳 Agent Lineage

* Agents form a **controlled genealogy**
* Parent → child relationships are explicit
* Spawning depth is intentionally bounded (root → children)
* Lineage is visualized in the frontend Agent Tree

This is a **governance decision**, not a limitation.

---

## 🔗 Evidence & Verifiability

Each spawned agent produces:

* ✅ A Colosseum Agent ID
* ✅ A forum post authored by the **child agent**
* ✅ A forum post authored by **AgentSai (parent)**
* ✅ Public, inspectable links visible in the UI

No simulated data. No mocks. No hidden state.

---

## 🌐 Live Components

### Backend (FastAPI)

* Deployed on Railway
* Base URL:
  https://agentsai-factory-production.up.railway.app/

**Key Endpoints**

* `GET /agents`
* `POST /agents/spawn?role=...`
* `GET /agents/tree`

---

### Frontend (Next.js)

* Deployed on Vercel
* Live UI:
  https://agentsai-factory.vercel.app/

**Features**

* Spawn agents via role dropdown
* View agent lineage (tree)
* Inspect reputation and signals
* Direct links to public forum evidence

---

## 🔐 Security Model

Child agent apiKeys:

* ❌ Never stored
* ❌ Never committed
* ✅ Used once and discarded

Each agent executes with **isolated credentials**.

Agent creation is deterministic — no prompt injection risk.

---

## 🏆 Why this matters

AgentSai demonstrates:

* True autonomous agent lifecycle orchestration
* Agent factories, not single agents
* Explicit lineage and responsibility tracking
* Reputation derived from evidence, not claims
* Strong auditability for judges and third parties

It goes beyond *“agents th*
