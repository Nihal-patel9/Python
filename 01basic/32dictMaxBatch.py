
batches = {
    'SA': 200,
    'SB': 300,
    'SC': 207,
    'SD': 305,
    'SE': 280,
}

max = 0
batch_code = ''
for k, v in batches.items():
    if (v > max):
        max = v
        batch_code = k


print("Max size batch code is ", batch_code)
