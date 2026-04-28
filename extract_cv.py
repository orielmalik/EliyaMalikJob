import docx
import sys
import json
import io

def extract_text(file_path):
    try:
        doc = docx.Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            if para.text.strip():
                full_text.append(para.text.strip())
        return full_text
    except Exception as e:
        return [f"Error: {str(e)}"]

def get_structured_data(text_lines):
    # Basic heuristic to extract contact info and sections
    data = {
        "name": "",
        "contact": {},
        "sections": {}
    }
    
    current_section = "Header"
    data["sections"][current_section] = []
    
    for line in text_lines:
        if any(keyword in line.upper() for keyword in ["EXPERIENCE", "SKILLS", "EDUCATION", "SUMMARY", "LANGUAGES", "ניסיון", "כישורים", "השכלה", "תמצית"]):
            current_section = line.strip()
            data["sections"][current_section] = []
        else:
            data["sections"][current_section].append(line)
            
    return data

if __name__ == "__main__":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    if len(sys.argv) < 2:
        print("Usage: python extract_cv.py <file_path> [--json]")
        sys.exit(1)
        
    file_path = sys.argv[1]
    lines = extract_text(file_path)
    
    if "--json" in sys.argv:
        print(json.dumps(get_structured_data(lines), ensure_ascii=False, indent=2))
    else:
        print('\n'.join(lines))
