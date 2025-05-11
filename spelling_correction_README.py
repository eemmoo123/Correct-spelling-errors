
# Simple Spelling Correction Tool using pyspellchecker and ipywidgets

# Install necessary libraries
!pip install pyspellchecker ipywidgets

# Import required modules
from spellchecker import SpellChecker
import ipywidgets as widgets
from IPython.display import display

# Initialize the spell checker
spell = SpellChecker()

# Define the spelling correction function
def correct_spelling(text):
    """Corrects spelling errors in the input text."""
    words = text.split()
    corrected_words = []
    for word in words:
        corrected_word = spell.correction(word)
        if corrected_word is not None:
            corrected_words.append(corrected_word)
        else:
            corrected_words.append(word)  # Use original word if no correction found
    return " ".join(corrected_words)

# Create user interface elements
text_input = widgets.Textarea(
    value='',
    placeholder='Enter text here...',
    description='Text:',
    disabled=False
)

output_text = widgets.Textarea(
    value='',
    placeholder='Corrected text will appear here...',
    description='Corrected Text:',
    disabled=False
)

correct_button = widgets.Button(
    description='Correct Spelling',
    disabled=False,
    button_style='',
    tooltip='Click me to correct the spelling',
    icon='check'
)

# Define button click event handler
def on_correct_button_clicked(b):
    output_text.value = correct_spelling(text_input.value)

# Bind the click event to the handler
correct_button.on_click(on_correct_button_clicked)

# Display the UI
display(text_input, correct_button, output_text)
