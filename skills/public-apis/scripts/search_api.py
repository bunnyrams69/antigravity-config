#!/usr/bin/env python3
"""
Public APIs Search Tool
CLI tool for finding free and public APIs from the curated public-apis catalog.
"""

import os
import sys
import json
import argparse

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, "..", "data")
APIS_FILE = os.path.join(DATA_DIR, "apis.json")
MCP_FILE = os.path.join(DATA_DIR, "mcp_servers.json")

def load_apis():
    if not os.path.exists(APIS_FILE):
        print(f"Error: Database not found at {APIS_FILE}", file=sys.stderr)
        sys.exit(1)
    with open(APIS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def load_mcp():
    if not os.path.exists(MCP_FILE):
        return []
    with open(MCP_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(description="Search and filter public APIs")
    parser.add_argument("-q", "--query", help="Search query (matches name, description, or category)")
    parser.add_argument("-c", "--category", help="Filter by category name (case-insensitive partial match)")
    parser.add_argument("--no-auth", action="store_true", help="Only show APIs that require no authentication")
    parser.add_argument("--https", action="store_true", help="Only show APIs with HTTPS support")
    parser.add_argument("--cors", choices=["yes", "no", "unknown"], help="Filter by CORS support")
    parser.add_argument("-n", "--limit", type=int, default=10, help="Max results to display (default: 10)")
    parser.add_argument("--json", action="store_true", help="Output results as JSON")
    parser.add_argument("--list-categories", action="store_true", help="List all available categories with API counts")
    parser.add_argument("--list-mcp", action="store_true", help="List available community MCP servers")

    args = parser.parse_args()

    if args.list_mcp:
        servers = load_mcp()
        if args.json:
            print(json.dumps(servers, indent=2, ensure_ascii=False))
        else:
            print(f"\nFound {len(servers)} Community MCP Servers:\n")
            for s in servers:
                print(f"- {s['name']}: {s['description']}")
                print(f"  URL: {s['url']}")
                print(f"  Auth: {s['auth']} | Transport: {s['transport']} | Install: {s['install']}\n")
        return

    apis = load_apis()

    if args.list_categories:
        cat_counts = {}
        for a in apis:
            cat = a.get("category", "Uncategorized")
            cat_counts[cat] = cat_counts.get(cat, 0) + 1
        
        sorted_cats = sorted(cat_counts.items(), key=lambda x: x[0].lower())
        if args.json:
            print(json.dumps(dict(sorted_cats), indent=2, ensure_ascii=False))
        else:
            print(f"\nPublic API Categories ({len(sorted_cats)} total):\n")
            for cat, count in sorted_cats:
                print(f"  {cat:<35} ({count} APIs)")
        return

    # Filter
    results = apis

    if args.category:
        cat_term = args.category.lower()
        results = [a for a in results if cat_term in a.get("category", "").lower()]

    if args.no_auth:
        results = [a for a in results if a.get("auth", "").lower() in ["no", "none", ""]]

    if args.https:
        results = [a for a in results if a.get("https", "").lower() == "yes"]

    if args.cors:
        results = [a for a in results if a.get("cors", "").lower() == args.cors.lower()]

    if args.query:
        q = args.query.lower()
        results = [
            a for a in results
            if q in a.get("name", "").lower()
            or q in a.get("description", "").lower()
            or q in a.get("category", "").lower()
        ]

    total_matched = len(results)
    limited_results = results[:args.limit]

    if args.json:
        output_payload = {
            "total_matches": total_matched,
            "displayed": len(limited_results),
            "results": limited_results
        }
        print(json.dumps(output_payload, indent=2, ensure_ascii=False))
    else:
        print(f"\nFound {total_matched} matching APIs (showing top {len(limited_results)}):\n")
        if not limited_results:
            print("No APIs matched the criteria. Try a broader search or use --list-categories.")
            return

        for idx, a in enumerate(limited_results, start=1):
            auth_str = "No auth" if a.get("auth", "").lower() in ["no", "none", ""] else a.get("auth", "Auth required")
            https_str = "HTTPS" if a.get("https", "").lower() == "yes" else "HTTP"
            cors_str = f"CORS: {a.get('cors', 'Unknown')}"
            print(f"[{idx}] {a['name']} ({a['category']})")
            print(f"    Description: {a['description']}")
            print(f"    URL:         {a['url']}")
            print(f"    Details:     {auth_str} | {https_str} | {cors_str}\n")

if __name__ == "__main__":
    main()
