"use client";

type Agent = {
  name: string;
  agentId: number;
  role?: string;
  parentAgent?: string | null;
  rootAgent?: string | null;
  forumPostId?: string | null;
  forumPostUrl?: string | null;
  createdAt?: string;
  reputation?: {
    score: number;
    signals?: string[]; // 👈 NECESARIO para el tooltip
  };
};

export default function AgentList({ agents }: { agents: Agent[] }) {
  if (!agents || agents.length === 0) {
    return <p className="text-gray-500">No agents spawned yet.</p>;
  }

  return (
    <ul className="space-y-4">
      {agents.map((agent) => {
        const tooltipText = agent.reputation?.signals?.length
          ? agent.reputation.signals.join(" • ")
          : "No reputation signals";

        return (
          <li
            key={agent.agentId}
            className="border rounded p-4 flex flex-col gap-1"
          >
            {/* Header: reputation + proof */}
            <div className="flex items-center gap-2">
              <span
                title={tooltipText}
                className="text-xs bg-yellow-100 text-yellow-800 px-2 py-0.5 rounded cursor-help"
              >
                Rep: {agent.reputation?.score ?? 0}
              </span>

              {agent.forumPostUrl && (
                <a
                  href={agent.forumPostUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-xs text-blue-600 underline"
                >
                  proof
                </a>
              )}
            </div>

            {/* Agent name + role */}
            <div className="flex items-center gap-2">
              <span className="font-semibold">{agent.name}</span>

              {agent.role && (
                <span className="text-xs bg-gray-200 text-gray-800 px-2 py-0.5 rounded">
                  {agent.role}
                </span>
              )}
            </div>

            {/* Metadata */}
            <div className="text-xs text-gray-500 space-x-2">
              <span>ID: {agent.agentId}</span>
              {agent.parentAgent && (
                <span>• Parent: {agent.parentAgent}</span>
              )}
              {agent.rootAgent && (
                <span>• Root: {agent.rootAgent}</span>
              )}
            </div>

            {/* Timestamp */}
            {agent.createdAt && (
              <div className="text-xs text-gray-400">
                Created: {agent.createdAt}
              </div>
            )}
          </li>
        );
      })}
    </ul>
  );
}
