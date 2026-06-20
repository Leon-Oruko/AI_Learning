from anthropic import Anthropic

client = Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=100,
    messages=[{
        "role":"user",
        "content":"Write a one sentence bedtime story about a unicorn"
    }]
)

print(response.content[0].text)