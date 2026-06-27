import json
import ast

def apply_all_replacements():
    with open('extracted_full_utf8.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open('services-2.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Read each line as a python list of dicts (since we used `print(list)` in extraction)
    # The extraction output might look like: [{'name': 'multi_replace_file_content', 'args': {...}}]
    all_chunks = []
    for line in lines:
        try:
            # We can use ast.literal_eval because we printed it directly from Python
            calls = ast.literal_eval(line.strip())
            for call in calls:
                if call['name'] == 'multi_replace_file_content':
                    # Sometimes arguments are sent as a JSON string, sometimes as dict
                    args = call['args']
                    chunks = args.get('ReplacementChunks', [])
                    if isinstance(chunks, str):
                        chunks = json.loads(chunks)
                    for chunk in chunks:
                        all_chunks.append(chunk)
        except Exception as e:
            print(f"Error parsing line: {e}")
    
    # Now we have a list of all ReplacementChunks!
    # They contain TargetContent and ReplacementContent
    success_count = 0
    fail_count = 0
    
    for chunk in all_chunks:
        target = chunk['TargetContent']
        replacement = chunk['ReplacementContent']
        if target in content:
            content = content.replace(target, replacement)
            success_count += 1
        else:
            fail_count += 1
            print(f"Failed to find target:\n{target[:100]}...\n")

    with open('services-2.html', 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Successfully applied {success_count} replacements. Failed {fail_count} replacements.")

apply_all_replacements()
