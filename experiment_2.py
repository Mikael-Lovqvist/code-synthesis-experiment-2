#This experiment is using the template system that has now been transferred to mvp4

from efforting.mvp4.improved_mnemonic_tree_processor.presets.template_processor import load_template, contextual_renderer
from efforting.mvp4.text_nodes import text_node
from efforting.mvp4.improved_mnemonic_tree_processor.presets import main_processor


template = load_template(text_node.from_text('''
	This is a test template
	§ for word in word_list:
		§ for char in word:
			§ if char in 'oe':
				§ execute
					emit_block(f'Vowel is {char}')
			§ elif char == 'l':
				\§ execute
					emit_block(f'lLLllLLl!')
			§ else:
				Consonant is «repr(char)»
		§ blank
'''))


print(contextual_renderer(main_processor.context.sub_context(
	word_list = ['all', 'the', 'words'],
)).render(template).text)

#   ___       _             _
#  / _ \ _  _| |_ _ __ _  _| |_
# | (_) | || |  _| '_ \ || |  _|
#  \___/ \_,_|\__| .__/\_,_|\__|
#                |_|

	# This is a test template
	# Consonant is 'a'
	# § execute
	#         emit_block(f'lLLllLLl!')
	# § execute
	#         emit_block(f'lLLllLLl!')

	# Consonant is 't'
	# Consonant is 'h'
	# Vowel is e

	# Consonant is 'w'
	# Vowel is o
	# Consonant is 'r'
	# Consonant is 'd'
	# Consonant is 's'
