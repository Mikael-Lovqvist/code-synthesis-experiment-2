#This experiment is using the template system that has now been transferred to mvp4

from efforting.mvp4.improved_mnemonic_tree_processor.presets.template_processor import load_template, contextual_renderer
from efforting.mvp4.text_nodes import text_node
from efforting.mvp4.improved_mnemonic_tree_processor.presets import main_processor
from html import escape as html_escape


word_list_template = load_template(text_node.from_text('''
	<ul>
		§ for word, description in word_list.items():
			<li>
				§ render template: word_description
			</li>
	</ul>
'''))

word_description_template = load_template(text_node.from_text('''
	<details>
		<summary>«html_escape(word)»</summary>
		<p style="font-style: italic;">«html_escape(description)»</p>
	</details>
'''))


print(contextual_renderer(main_processor.context.sub_context(
	word_list = dict(
		toner = 'Plastic color pigment used in laser printers',
		ink = 'Liquid color pigment stuff',
		escape = 'Here is a HTML tag that is escaped: <details>',
	),
	html_escape = html_escape,
), templates = dict(
	word_list = word_list_template,
	word_description = word_description_template,
)).render(word_list_template).text)

#   ___       _             _
#  / _ \ _  _| |_ _ __ _  _| |_
# | (_) | || |  _| '_ \ || |  _|
#  \___/ \_,_|\__| .__/\_,_|\__|
#                |_|

	# <ul>
	# 	<li>
	# 		<details>
	# 			<summary>toner</summary>
	# 			<p style="font-style: italic;">Plastic color pigment used in laser printers</p>
	# 		</details>
	# 	</li>
	# 	<li>
	# 		<details>
	# 			<summary>ink</summary>
	# 			<p style="font-style: italic;">Liquid color pigment stuff</p>
	# 		</details>
	# 	</li>
	# 	<li>
	# 		<details>
	# 			<summary>escape</summary>
	# 			<p style="font-style: italic;">Here is a HTML tag that is escaped: &lt;details&gt;</p>
	# 		</details>
	# 	</li>
	# </ul>
