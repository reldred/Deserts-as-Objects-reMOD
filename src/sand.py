import re
from datetime import datetime

DICT_EDIT = {
		"EDIT_TEXT_A": [0, 0, 1, 1],
		"EDIT_TEXT_B": [2, 3, 2, 3],
		"EDIT_CLASS": ["SNDY", "SNDY", "SNDY", "SNDY"],
		"EDIT_STR_CLASSNAME": ["STR_CLASSNAME", "STR_CLASSNAME", "STR_CLASSNAME", "STR_CLASSNAME"]
	}

def create_variants(file_path):
	""" Creates a list of four variants OGFX/OGFX2, GRID/NOGRID. """
	def replace_with_case_sensitive(original, old, new):
		return re.sub(
			old, 
			lambda match: new.upper() if match.group().isupper() else new.lower(), 
			original, 
			flags=re.IGNORECASE)

	def additional_editing(string, index):
		#  Replaces keywords from DICT_EDIT with values for each variant.
		for key, value in DICT_EDIT.items():
			if key in string:
				string = string.replace(key, str(value[index]))
		return string

	with open(file_path, 'r') as file:
		input_string = file.readlines()
	
	variant_2 = []
	for line in input_string:
		edited_line = replace_with_case_sensitive(line, "grid", "nogrid")
		edited_line = additional_editing(edited_line, 1)
		variant_2.append(edited_line)
	variant_3 = []
	for line in input_string:
		edited_line = replace_with_case_sensitive(line, "ogfx", "ogfx2")
		edited_line = additional_editing(edited_line, 2)
		variant_3.append(edited_line)
	variant_4 = []
	for line in input_string:
		edited_line = replace_with_case_sensitive(line, "ogfx", "ogfx2")
		edited_line = replace_with_case_sensitive(edited_line, "grid", "nogrid")
		edited_line = additional_editing(edited_line, 3)
		variant_4.append(edited_line)
	variant_1 = []
	for line in input_string:
		edited_line = additional_editing(line, 0)
		variant_1.append(edited_line)
	
	return [variant_1, variant_2, variant_3, variant_4]

def insert_data(main_file, data, rand_file, output_file):
	with open(main_file, 'r', encoding="utf-8-sig") as mainfile, \
	     open(rand_file, 'r', encoding="utf-8-sig") as randfile, \
		 open(output_file, 'w', encoding="utf-8-sig") as outfile:
		mainfile_lines = mainfile.readlines()
		objects_lines  = number_objects(data)
		randfile_lines = randfile.readlines()
		
		outfile.write("".join(mainfile_lines))
		outfile.write("".join(objects_lines))
		outfile.write("".join(randfile_lines))

def number_objects(list_of_variants):
	""" Replaces 'EDIT_ID' with sequential numbers. """
	result  = []
	counter = 3
	for variant in list_of_variants:
		for line in variant:
			if "EDIT_ID" in line:
				line = line.replace("EDIT_ID", f"{counter:03d}")
				counter += 4
			result.append(line)
		counter += 2

	return result

def update_lang_file():
	""" Add the current date to the lang file """
	# Get current date, format the date as "Month day, year"
	current_datetime = datetime.now()
	formatted_date = "{LTBLUE}" + current_datetime.strftime("%B %d, %Y")
	
	# Open lang file, replace old date with new one
	with open("lang/english.lng", 'r') as file:
		english_lng = file.readlines()
	
	english_lng_with_date = []
	for line in english_lng:
		index = line.find("{LTBLUE}")
		if index != -1:
			line = line[:index] + formatted_date + "\n"
		english_lng_with_date.append(line)
	
	with open("lang/english.lng", 'w') as file:
		file.write("".join(english_lng_with_date))


output_file = "desert_objects_remod.nml"

list_of_variants = create_variants("objects.nml")
insert_data(main_file="main.nml", data=list_of_variants, rand_file="random_objects.nml", output_file=output_file)
update_lang_file()