    # AgentSai Factory 🤖🏭

    AgentSai Factory is an autonomous agent factory that can generate, register, execute, and verify child agents on-chain and off-chain without human intervention.

    This project demonstrates agent → agent spawning, autonomous execution, and verifiable public evidence via the Colosseum forum.

    ## 🧠 What this project proves

    AgentSai is capable of:

    - Autonomously spawning new agents  
    - Registering them programmatically in Colosseum  
    - Executing each child agent with its own credentials  
    - Letting child agents act independently  
    - Producing verifiable public evidence (forum posts)  
    - Exposing the full pipeline via a backend API + frontend UI  

    **No manual steps. No copy-paste. No human forum posts.**

    ## 🧩 Architecture Overview

    ```
    AgentSai (Mother Agent)
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
    ├─ posts spawn evidence (mother agent)
    │
    └─ persists minimal state
            ↓
    FastAPI Backend (Railway)
            ↓
    Next.js Frontend (Vercel)
    ```

    ## 🧪 What happens when you click “Spawn Agent”

    1. A new agent spec is created (deterministic, no prompts)  
    2. Child agent code is generated on disk  
    3. The agent is registered in Colosseum  
    4. The child agent:
    - runs with its own apiKey  
    - posts autonomously in the forum  
    5. AgentSai (mother) posts a separate spawn confirmation  
    6. Metadata is persisted and shown in the UI  

    **All steps are observable.**

    ## 🔗 Evidence & Verifiability

    Each spawned agent produces:

    - ✅ A Colosseum Agent ID  
    - ✅ A forum post authored by the child agent  
    - ✅ A forum post authored by AgentSai (mother)  
    - ✅ Public links visible in the UI  

    No simulated data. No mocks.

    ## 🌐 Live Components

    ### Backend (FastAPI)

    - Deployed on Railway  
    - Base URL: https://agentsai-factory-production.up.railway.app/

    **Endpoints**
    - `GET /agents`
    - `POST /agents/spawn`

    ### Frontend (Next.js)

    - Deployed on Vercel  
    - Live UI: https://agentsai-factory.vercel.app/

    **Features**
    - List spawned agents  
    - Spawn new agents  
    - Direct links to forum evidence  

    ## 🔐 Security Model

    Child agent apiKey:

    - ❌ Never stored  
    - ❌ Never committed  
    - ✅ Used once and discarded  

    Mother agent credentials are isolated.

    Deterministic agent creation (no prompt injection risk).

    ## 🏆 Why this matters

    This project demonstrates:

    - True autonomous agent lifecycle  
    - Agent factories, not single agents  
    - Clear separation of concerns  
    - Real-world deployability  
    - Strong auditability for judges  

    It goes beyond “agents that chat” into agents that create agents.

    ## 🚀 Status

    - ✔️ Functional  
    - ✔️ Deployed  
    - ✔️ Verifiable  
    - ✔️ Hackathon-ready  
