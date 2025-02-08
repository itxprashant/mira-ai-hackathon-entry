from mira_sdk import MiraClient, Flow
client = MiraClient(config={"API_KEY": "sb-6113a5cb58f6b3c5660b07363f88b025"})

flow = Flow(source="./config.yaml")
input_dict = { "key" : "value" }

response = client.flow.test(flow, input_dict)
