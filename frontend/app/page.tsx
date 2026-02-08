"use client";

import { useEffect, useState } from "react";
import AgentList from "@/components/AgentList";
import SpawnButton from "@/components/SpawnButton";
import AgentTree from "@/components/AgentTree";
import { fetchAgentTree, listAgentsWithReputation } from "@/lib/api";

export default function Page() {
  const [agents, setAgents] = useState<any[]>([]);
  const [tree, setTree] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  async function loadAll() {
    try {
      setError(null);
      setLoading(true);

      const [agentsData, treeData] = await Promise.all([
        listAgentsWithReputation(),
        fetchAgentTree(),
      ]);

      setAgents(agentsData);
      setTree(treeData);
    } catch {
      setError("Failed to load agents");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadAll();
  }, []);

  return (
    <main className="p-6 max-w-3xl mx-auto space-y-6">
      <h1 className="text-2xl font-bold">AgentSai Factory</h1>

      {/* Reputation legend */}
      <div className="border rounded-lg p-4 bg-gray-50">
        <h2 className="font-semibold mb-2">Reputation signals</h2>

        <table className="text-sm w-full border-collapse">
          <tbody className="text-gray-700">
            <tr>
              <td className="py-1 pr-4">Spawned agent</td>
              <td className="py-1 text-right font-mono">+20</td>
            </tr>
            <tr>
              <td className="py-1 pr-4">Forum evidence</td>
              <td className="py-1 text-right font-mono">+20</td>
            </tr>
            <tr>
              <td className="py-1 pr-4">Child agent spawned</td>
              <td className="py-1 text-right font-mono">+15 / child</td>
            </tr>
            <tr>
              <td className="py-1 pr-4">Root agent</td>
              <td className="py-1 text-right font-mono">+10</td>
            </tr>
            <tr>
              <td className="py-1 pr-4">Role bonus</td>
              <td className="py-1 text-right font-mono">+var</td>
            </tr>
          </tbody>
        </table>

        <p className="text-xs text-gray-500 mt-2">
          Reputation is derived from verifiable actions, not stored.
        </p>
      </div>

      {/* Spawn control */}
      <SpawnButton onSpawn={loadAll} />

      {loading && <p className="text-gray-500">Loading agents...</p>}

      {error && <p className="text-red-500">{error}</p>}

      {!loading && !error && (
        <>
          <AgentTree tree={tree} />
          <AgentList agents={agents} />
        </>
      )}
    </main>
  );
}
