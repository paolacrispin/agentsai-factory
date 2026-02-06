"use client";

import { useState } from "react";
import { spawnAgent } from "@/lib/api";

export default function SpawnButton({
  onSpawn,
}: {
  onSpawn: () => Promise<void>;
}) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function handleClick() {
    setError(null);
    setLoading(true);
    try {
      await spawnAgent();
      await onSpawn();
    } catch (e) {
      setError("Failed to spawn agent");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="space-y-2">
      <button
        onClick={handleClick}
        disabled={loading}
        className={`px-4 py-2 rounded font-medium ${
          loading
            ? "bg-gray-300 cursor-not-allowed"
            : "bg-black text-white hover:bg-gray-800"
        }`}
      >
        {loading ? "Spawning agent…" : "Spawn agent"}
      </button>

      {error && <p className="text-sm text-red-600">{error}</p>}
    </div>
  );
}
