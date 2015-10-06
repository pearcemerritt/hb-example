content_file = open("/Users/pearce.merritt/personal/hackbright/w8c1/woods.txt")
content = content_file.readlines()
print content
i = 0
indent_count = 1

while(True):
	current_content = content[i]
	chosen_option = raw_input(current_content + ": ")
	chosen_option_index = int(chosen_option)  - 1
	while(content[i] 

