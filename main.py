from mira_sdk import MiraClient, Flow

# Initialize the client
client = MiraClient(config={"API_KEY": "sb-6113a5cb58f6b3c5660b07363f88b025"})

version = "1.0.0"
input_data = {
"user-prompt": "A romantic sci-fi"
}

# If no version is provided, latest version is used by default
if version:
    flow_name = f"@itxprashant/movie-book-recommender/{version}"
else:
    flow_name = "@itxprashant/movie-book-recommender"

result = client.flow.execute(flow_name, input_data)
print(result)