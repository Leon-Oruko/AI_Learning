from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-5.5",
    input="Write a three sentence bedtime story about a unicorn, that demonstrates a lesson on honesty.The story must include a dragon and a castle"
)

print(response.output_text)