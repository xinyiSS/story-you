class CombinedTextEditorNode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input_text": ("STRING", {
                    "multiline": True,
                    "default": "Enter your text here."
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "process_text"
    CATEGORY = "Text Processing"

    def process_text(self, input_text):
        # Step 1: Check if the first character is "|", if so, remove it
        if input_text.startswith("|"):
            input_text = input_text[1:]
        
        # Step 2: Replace each "|" with "|\n"
        output_text = input_text.replace("|", "|\n")
        
        return (output_text,)


# A dictionary that contains all nodes you want to export with their names
NODE_CLASS_MAPPINGS = {
    "CombinedTextEditorNode": CombinedTextEditorNode
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "CombinedTextEditorNode": "textbianji"
}
