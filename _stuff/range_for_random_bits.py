import pyperclip

def generate_ranges_for_random_bits(input_number):
    if not (1 <= input_number <= 255):
        return "Input must be an integer between 1 and 255."

    range_size = 256 // input_number
    output_lines = []
    
    for i in range(input_number):
        start = i * range_size
        end = (i + 1) * range_size - 1 if i < input_number - 1 else 255
        output_lines.append(f"    {start}..{end}: {i};")

    return "\n".join(output_lines)

input_value = 3
result = generate_ranges_for_random_bits(input_value)
pyperclip.copy(result)
print(result)
