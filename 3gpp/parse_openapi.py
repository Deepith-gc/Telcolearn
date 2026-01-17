import yaml
import json,logging


logging.basicConfig(filename="obs.log",level=logging.INFO)

def api_parse(filepath):
    with open(r"C:\Users\deepi\Desktop\3gpp\src\TS24560_Aimlec_AIMLEClientServiceOperations.yaml",'r') as f:
        spec = yaml.safe_load(f)
    
    api_title =spec.get("info",{}).get("title")
    path = spec.get("paths",{})
    endpoints = []

    for path, method in path.items():
        for method,details in method.items():
            endpoints.append({
                "path": path,
                "method": method.upper(),
                "summary":details.get("summary"),
                "auth":spec.get("components",{}).get("security",{}),
            })

    return {
        "title": api_title,
        "endpoint_count": len(endpoints),
        "endpoints":endpoints
    }        

if __name__=="__main__":
    result = api_parse("TS24560_Aimlec_AIMLEClientServiceOperations.yaml")
    print(json.dumps(result,indent=2))
    with open("metadata.json", "w") as out_file:
        json.dump(result, out_file, indent=2)
        print("JSON output written to output.json")