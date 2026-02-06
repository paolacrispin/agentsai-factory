type Agent = {
  name: string;
  agentId: number;
  forumPostId?: number;
  createdAt?: string;
};

export default function AgentList({ agents }: { agents: Agent[] }) {
  if (!agents.length) {
    return <p className="text-gray-500">No agents spawned yet</p>;
  }

  return (
    <ul className="space-y-3">
      {agents.map((agent) => (
        <li
          key={`${agent.agentId}-${agent.forumPostId ?? "nopost"}`}
          className="border rounded-lg p-4 bg-white shadow-sm space-y-2"
        >
          {/* Header */}
          <div className="flex items-center justify-between">
            <div className="font-mono text-sm font-semibold">
              {agent.name}
            </div>
            <span className="text-xs bg-green-100 text-green-700 px-2 py-0.5 rounded">
              spawned
            </span>
          </div>

          {/* Metadata */}
          <div className="text-xs text-gray-500 space-y-1">
            <div>agentId: {agent.agentId}</div>
            {agent.createdAt && (
              <div>
                created: {new Date(agent.createdAt).toLocaleString()}
              </div>
            )}
          </div>

          {/* Evidence */}
          {agent.forumPostId ? (
            <div className="text-xs text-green-700 bg-green-50 px-2 py-1 rounded">
              ✅ Forum post created (postId: {agent.forumPostId})
            </div>
          ) : (
            <div className="text-xs text-gray-400">
              No forum evidence
            </div>
          )}
        </li>
      ))}
    </ul>
  );
}

