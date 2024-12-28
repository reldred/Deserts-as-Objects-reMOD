from PIL import Image

def merge_images(image_paths, mode="vertical"):
	"""	Merges images vertically/horizontally, returns img obj.
	image_paths (list of str): List of paths to PNG images."""
	images = [Image.open(path) for path in image_paths]

	if mode == "vertical":
		total_width = max(img.width for img in images)
		total_height = sum(img.height for img in images)

		result_image = Image.new("RGB", (total_width, total_height), (255, 255, 255))

		y_offset = 0
		for img in images:
			result_image.paste(img, (0, y_offset))
			y_offset += img.height

		return result_image

	elif mode == "horizontal":
		total_width = sum(img.width for img in images)
		total_height = max(img.height for img in images)

		result_image = Image.new("RGB", (total_width, total_height), (255, 255, 255))

		x_offset = 0
		for img in images:
			result_image.paste(img, (x_offset, 0))
			x_offset += img.width

		return result_image

	else:
		print("Mode: 'horizontal' or 'vertical'.")
		return None