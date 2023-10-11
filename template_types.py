from template_tokens import template_tokenizer
from template_ast import switch, switch_branch, for_loop, execute, conditional, unconditional, indented, placeholder, sequence, template_tree

def template_sequence(seq):
	if len(seq) == 0:
		return None
	elif len(seq) == 1:
		return seq[0]
	else:
		return sequence(*seq)
