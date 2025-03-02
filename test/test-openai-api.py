from openai import OpenAI

client = OpenAI(
  api_key="sk-proj-****-jKH71ESSpDC3Hr2-7hI62f0kk-jne5DamnV8ojfrRC7jp_193QApDsn2wm2IellPCPIx-kA"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message)

