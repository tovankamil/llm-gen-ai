import tiktoken

enc = tiktoken.encoding_for_model('gpt-4o')
text = "Hey There! My name is Tofan"
tokens = enc.encode(text)

print("tokens",tokens)

dec =  enc.decode([25216, 3274, 0, 3673, 1308, 382, 353, 96902])

print("Decode",dec)