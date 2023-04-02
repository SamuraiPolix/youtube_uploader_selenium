import json
import io

def create_metadata(title, desc, tags, output_path):
    with io.open('metadata.json', 'w', encoding='utf8') as f:
        str_ = json.dumps({'title': title, 'description': desc, 'tags': tags}, ensure_ascii=False, indent=4)
        f.write(str_)
