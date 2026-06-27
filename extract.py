import json
import os

transcript_path = 'C:/Users/abhii/.gemini/antigravity-ide/brain/27e20736-f997-446d-8174-26c8cdf29b5a/.system_generated/logs/transcript_full.jsonl'

with open(transcript_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for line in reversed(lines):
    try:
        entry = json.loads(line)
        if 'tool_calls' in entry:
            for call in entry['tool_calls']:
                if call['function']['name'] in ['default_api:replace_file_content', 'default_api:multi_replace_file_content', 'default_api:write_to_file', 'default_api:run_command']:
                    args = json.loads(call['function']['arguments'])
                    print(f"Tool: {call['function']['name']}, Args: {list(args.keys())}")
    except:
        pass
