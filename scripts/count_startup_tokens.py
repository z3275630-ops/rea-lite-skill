"""Count a normalized model-facing REA context budget from saved MCP catalogs.

Uses tiktoken's o200k_base; this is not a client's actual prompt or billing count.
Catalog inputs are complete {"tools": [...]} tools/list captures. No raw results,
private paths or tool definitions are included in the output report.
"""
import argparse
import json
from pathlib import Path
from importlib.metadata import version

import tiktoken


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--direct", required=True, type=Path)
    parser.add_argument("--lazy", required=True, type=Path)
    parser.add_argument("--upstream-skill", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    encoding = tiktoken.get_encoding("o200k_base")

    def count(text):
        return len(encoding.encode(text))

    def catalog(file):
        tools = json.loads(file.read_text(encoding="utf-8"))["tools"]
        names = [tool["name"] for tool in tools]
        if len(set(names)) != len(names):
            raise ValueError("Duplicate tool names in catalog")
        functions = [{"type": "function", "function": {
            "name": tool["name"], "description": tool.get("description", ""),
            "parameters": tool["inputSchema"],
        }} for tool in tools]
        text = json.dumps(functions, ensure_ascii=False, separators=(",", ":"))
        return {"toolEntries": len(tools), "utf8Bytes": len(text.encode("utf-8")),
                "tokens": count(text)}

    direct, lazy = catalog(args.direct), catalog(args.lazy)
    upstream_tokens = count(args.upstream_skill.read_text(encoding="utf-8"))
    lite_tokens = count((root / "skills/reverse-engineer-anything/SKILL.md").read_text(encoding="utf-8"))
    trigger_tokens = count((root / "snippets/AGENTS.md").read_text(encoding="utf-8"))
    original_budget = direct["tokens"] + upstream_tokens
    lite_budget = lazy["tokens"] + lite_tokens + trigger_tokens
    result = {
        "measurementDate": "2026-10-24", "reaVersion": "6.7.0", "proxyVersion": "1.3.3",
        "tokenizer": "o200k_base", "tiktokenVersion": version("tiktoken"),
        "method": "Compact UTF-8 JSON function definitions: name, description, inputSchema as parameters; exclude outputSchema and wire metadata.",
        "direct": direct, "lazy": lazy,
        "upstreamSkillTokens": upstream_tokens, "liteSkillTokens": lite_tokens,
        "triggerSnippetTokens": trigger_tokens,
        "estimatedReaContext": {"directWithSkill": original_budget,
                                "lazyWithSkillAndTrigger": lite_budget,
                                "reductionPercent": round(100 * (1 - lite_budget / original_budget), 2)},
        "limits": "REA-related comparison budget only. Excludes client system prompts, unrelated tools, messages, framing and later references/schemas/results. Not a fresh-chat UI or billing measurement.",
    }
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8", newline="\n")
    print(text, end="")


if __name__ == "__main__":
    main()
