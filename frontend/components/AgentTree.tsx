type AgentNode = {
    name: string;
    agentId: number;
    forumPostUrl?: string;
    children?: AgentNode[];
  };
  
  function Node({ agent, depth = 0 }: { agent: AgentNode; depth?: number }) {
    return (
      <div style={{ marginLeft: depth * 20 }} className="space-y-1">
        <div className="flex items-center gap-2">
          <span className="font-mono text-sm">
            └─ {agent.name}
          </span>
          <span className="text-xs text-gray-500">
            #{agent.agentId}
          </span>
          {agent.forumPostUrl && (
            <a
              href={agent.forumPostUrl}
              target="_blank"
              className="text-xs text-blue-600 underline"
            >
              forum
            </a>
          )}
        </div>
  
        {agent.children?.map((child) => (
          <Node key={child.agentId} agent={child} depth={depth + 1} />
        ))}
      </div>
    );
  }
  
  export default function AgentTree({ tree }: { tree: AgentNode[] }) {
    if (!tree.length) {
      return <p className="text-gray-500">No agent lineage yet</p>;
    }
  
    return (
      <div className="border rounded-lg p-4 bg-white">
        <h2 className="font-semibold mb-3">Agent Lineage</h2>
        {tree.map((root) => (
          <Node key={root.agentId} agent={root} />
        ))}
      </div>
    );
  }
  