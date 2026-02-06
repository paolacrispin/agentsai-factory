const API_BASE =
  process.env.NEXT_PUBLIC_API_BASE || "http://localhost:8000";

export async function listAgents() {
  const res = await fetch(`${API_BASE}/agents`, { cache: "no-store" });
  if (!res.ok) throw new Error("Failed to fetch agents");
  return res.json();
}

export async function spawnAgent() {
  const res = await fetch(`${API_BASE}/agents/spawn`, { method: "POST" });
  if (!res.ok) throw new Error("Failed to spawn agent");
  return res.json();
}
