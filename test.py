api_key = "wtc-sk-ad74a24c0976d994b382a85c48b31f6d79288983"

from wetro import Wetrocloud

client = Wetrocloud(api_key=api_key)
tools_client = client.tools

# Extract structured data from a website
extract_response = tools_client.extract(
    website="https://www.forbes.com/real-time-billionaires/",
    json_schema='[{"name": "<name>", "networth": "<networth>"}]'
)
print(extract_response)