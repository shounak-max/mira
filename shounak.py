from mira_sdk import MiraClient, Flow

# Initialize the client
client = MiraClient(config={"API_KEY": "your api key"})

version = "1.0.0"
input_data = {}

# If no version is provided, latest version is used by default
if version:
    flow_name = f"@shounakbanerjee/mess-menu-generator/{version}"
else:
    flow_name = "@shounakbanerjee/mess-menu-generator"

result = client.flow.execute(flow_name, input_data)
print(result)
