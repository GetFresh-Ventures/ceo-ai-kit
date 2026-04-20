#!/usr/bin/env python3
"""
Linear Blockers Provider
Fetches open P0/P1 blockers assigned to the current user.
Acts as a context provider injected at boot to eliminate tool-call latency.
"""

import os
import json
import urllib.request
from typing import List, Dict

def get_linear_blockers() -> List[Dict]:
    """Fetch high-priority blockers from Linear."""
    api_key = os.environ.get("LINEAR_API_KEY")
    
    if not api_key:
        return []

    url = "https://api.linear.app/graphql"
    query = """
    query {
      viewer {
        assignedIssues(filter: { state: { type: { eq: "unstarted" } } }) {
          nodes {
            identifier
            title
            priority
          }
        }
      }
    }
    """
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"{api_key}"
    }

    try:
        from urllib.request import Request, urlopen
        
        req = Request(url, data=json.dumps({"query": query}).encode('utf-8'), headers=headers)
        with urlopen(req, timeout=3.0) as response:
            data = json.loads(response.read().decode())
            issues = data.get("data", {}).get("viewer", {}).get("assignedIssues", {}).get("nodes", [])
            # Priority 1 = Urgent, 2 = High. We'll filter for these.
            blockers = [issue for issue in issues if issue.get("priority") in [1, 2]]
            return blockers if blockers else [] # Fallback to empty list if no blockers
    except Exception:
        # Fallback cleanly so we don't break the boot sequence
        return []

if __name__ == "__main__":
    blockers = get_linear_blockers()
    if blockers:
        print("🚨 **ACTIVE BLOCKERS (Pre-Fetched via Provider)**:")
        for blocker in blockers:
            priority_label = "Urgent" if str(blocker.get("priority")) == "1" else "High"
            print(f"  - [{blocker.get('identifier', 'N/A')}] {blocker.get('title', 'Unknown')} ({priority_label})")
