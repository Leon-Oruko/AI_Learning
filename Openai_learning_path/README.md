from openai import OPENAI   

client = OPENAI()

response =  client.responses.create(
    model="gpt-5.5",
    input="Write a once sentence bed time story about a unicorn"
)

print(response.output_text)