"use client";

import { useState } from "react";

export default function SpawnButton({
  onSpawn,
}: {
  onSpawn: () => void;
}) {
  const [role, setRole] = useState("logger");
  const [loading, setLoading] = useState(false);

  async function spawnAgent() {
    try {
      setLoading(true);
      await fetch(
        `http://localhost:8000/agents/spawn?role=${role}`,
        { method: "POST" }
      );
      onSpawn();
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="flex items-center gap-2">
      <select
        value={role}
        onChange={(e) => setRole(e.target.value)}
        className="border rounded px-2 py-1 text-sm"
      >
        <option value="logger">Logger</option>
        <option value="monitor">Monitor</option>
        <option value="executor">Executor</option>
        <option value="generic">Generic</option>
      </select>

      <button
        onClick={spawnAgent}
        disabled={loading}
        className="px-3 py-1 rounded bg-black text-white text-sm disabled:opacity-50 hover:bg-gray-900"
      >
        {loading ? "Spawning..." : "Spawn agent"}
      </button>
    </div>
  );
}
