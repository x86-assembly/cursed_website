import json
import os


def convert_json_to_html(json_data):
    if isinstance(json_data, dict):
        tag_type = json_data.get("type")
        attributes = json_data.get("attributes", {})
        content = json_data.get("content", [])
        
        if tag_type:
            html = f"<{tag_type}"
            
            if attributes:
                attribute_str = " ".join([f'{key}="{value}"' for key, value in attributes.items()])
                html += f" {attribute_str}"
            
            html += ">"
            
            if isinstance(content, list):
                for item in content:
                    html += convert_json_to_html(item)
            
            html += f"</{tag_type}>"
            return html
        
    elif isinstance(json_data, list):
        html = ""
        for item in json_data:
            html += convert_json_to_html(item)
        return html
    
    elif isinstance(json_data, str):
        return json_data.strip()
    
    return ""



with open("./src/index.json", 'r') as file:
    json_data = json.load(file)

html = convert_json_to_html(json_data)


file_path = "./build/index.html"  # File path relative to the current directory

# Create the directory if it doesn't exist
os.makedirs(os.path.dirname(file_path), exist_ok=True)

# Open the file in write mode and create it if it doesn't exist
with open(file_path, "w") as file:
    file.write(html)

