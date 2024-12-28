from PIL import Image, ImageDraw, ImageFont

def create_number_sequence_image(number_range, text_color, font_path, font_size, step, direction="horizontal", output_file=None):
	"""	Creates an image displaying a sequence of numbers.

	Arguments:
		number_range (tuple): Starting and ending numbers of the sequence.
		text_color (tuple): Color of the text (RGB format).
		font_path (str): Path to the .ttf font file.
		font_size (int): Font size for the text.
		step (int): Step between nubmers in px.
		direction (str): 'horizontal' or 'vertical'
		output_file (str): Path to save the output image."""
	try:
		font = ImageFont.truetype(font_path, font_size)
	except IOError:
		print("Font file not found.")
		return

	sequence = range(number_range[0], number_range[1] + 1)

	# Calculate dimensions of image, get bounding box for the text
	last_number = str(sequence[-1])
	bbox = font.getbbox(last_number)
	last_number_width = bbox[2] - bbox[0]
	last_number_height = bbox[3] - bbox[1]

	if direction == "horizontal":
		image_width = (len(sequence) - 1) * step + last_number_width + 1
		image_height = last_number_height + font_size//2
	elif direction == "vertical":
		image_height = (len(sequence) - 1) * step + last_number_height + 1
		image_width = last_number_width + 2
	else:
		print("Direction: 'horizontal' or 'vertical'.")
		import sys
		sys.exit()

	# Create image and ImageDraw obj
	if text_color != (255, 255, 255):
		image = Image.new("RGB", (image_width, image_height), "white")
	else:
		image = Image.new("RGB", (image_width, image_height), "blue")
	draw = ImageDraw.Draw(image)

	# Paste numbers
	if direction == "horizontal":
		x_offset = 0
		for num in sequence:
			text = str(num)
			draw.text((x_offset, 0), text, font=font, fill=text_color)
			x_offset += step
	elif direction == "vertical":
		y_offset = 0
		for num in sequence:
			text = str(num)
			draw.text((1, y_offset), text, font=font, fill=text_color)
			y_offset += step

	image.save(output_file)

create_number_sequence_image(
	number_range=(0, 18),
	text_color=(0, 0, 255),
	font_path="arial.ttf",
	font_size=14,
	step=80,
	direction="horizontal",
	output_file="number_sequence.png"
)
