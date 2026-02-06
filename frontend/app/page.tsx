"use client";

import { useEffect, useState } from "react";
import AgentList from "@/components/AgentList";
import SpawnButton from "@/components/SpawnButton";
import { listAgents } from "@/lib/api";

export default function Page() {
  const [agents, setAgents] = useState<any[]>([]);
  const [loading, setLoading] = useState(true); // 👈 inicia en true
  const [error, setError] = useState<string | null>(null);

  async function loadAgents() {
    try {
      setError(null);
      setLoading(true);
      const data = await listAgents();
      setAgents(data);
    } catch {
      setError("Failed to load agents");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadAgents();
  }, []);

  return (
    <main className="p-6 max-w-3xl mx-auto space-y-6">
      <h1 className="text-2xl font-bold">AgentSai Factory</h1>

      {/* Spawn control */}
      <SpawnButton onSpawn={loadAgents} />

      {/* States */}
      {loading && (
        <p className="text-gray-500">Loading agents...</p>
      )}

      {error && (
        <p className="text-red-500">{error}</p>
      )}

      {!loading && !error && (
        <AgentList agents={agents} />
      )}
    </main>
  );
}
