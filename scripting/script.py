import json
import sys

file = sys.argv[1]

with open(file) as f:
    data = json.load(f)

for resource in data.get("resource_changes") or []:
    actions = resource["change"]["actions"]

    # Ignore no-op
    if actions == ["no-op"]:
        continue

    # Block destructive changes
    if "delete" in actions or actions == ["delete", "create"]:
        print(f"BLOCKED: {resource['address']} has destructive action {actions}")
        sys.exit(1)

    # Validate update
    if "update" in actions:
        before = resource["change"]["before"] or {}
        after = resource["change"]["after"] or {}

        for key in before:
            if before.get(key) != after.get(key):
                if key != "tags":
                    print(f"BLOCKED: {resource['address']} modified {key}")
                    sys.exit(1)

        tags = after.get("tags", {})

        if len(tags) != 1 or "GitCommitHash" not in tags:
            print(f"BLOCKED: Invalid tag modification in {resource['address']}")
            sys.exit(1)

print("SAFE: Plan can be applied")

