from wtforms import FileField, SelectMultipleField, widgets

class MultiCheckboxField(SelectMultipleField):
	widget = widgets.ListWidget(prefix_label=False)
	option_widget = widgets.CheckboxInput()

class MultiFileField():
	def __init__(self, labels):
		self.files = {}
		for label in labels:
			self.files[label] = FileField(label)