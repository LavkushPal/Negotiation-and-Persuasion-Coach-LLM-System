from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B-Instruct")


"""
tokenizer need in this format

{
 "messages": [
  {
   "role": "system",
   "content": "You are an expert negotiation coach."
  },
  {
   "role": "user",
   "content": "Opponent says they need more firewood."
  },
  {
   "role": "assistant",
   "content": "Offer a trade such as sharing resources."
  }
 ]
}

"""

messages = [
    {"role": "system", "content": "You are a negotiation coach."},
    {"role": "user", "content": "Opponent wants more firewood."}
]

prompt = tokenizer.apply_chat_template(messages, tokenize=False)

print(prompt)