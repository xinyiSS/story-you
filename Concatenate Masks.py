import torch
import random
import folder_paths

class CombineMasksNode:
    def __init__(self):
        self.output_dir = folder_paths.get_temp_directory()
        self.prefix_append = "_combine_" + ''.join(random.choice("abcdefghijklmnopqrstuvwxyz1234567890") for _ in range(5))
        self.compress_level = 4

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "mask1": ("MASK",),
                "mask2": ("MASK",),
            },
        }

    RETURN_TYPES = ("MASK",)
    FUNCTION = "combine_masks"
    CATEGORY = "CustomNodes/LayerMask"
    OUTPUT_NODE = True

    def combine_masks(self, mask1, mask2):
        # Ensure both masks have the same height
        if mask1.shape[-2] != mask2.shape[-2]:
            raise ValueError("Masks must have the same height to be combined.")

        # Ensure both masks are 3D tensors (C, H, W)
        if mask1.dim() == 2:
            mask1 = torch.unsqueeze(mask1, 0)
        if mask2.dim() == 2:
            mask2 = torch.unsqueeze(mask2, 0)

        # Concatenate the masks along the width (last dimension)
        combined_mask = torch.cat((mask1, mask2), dim=-1)

        # Save the combined mask as an image
        self.save_image(combined_mask)
        return (combined_mask,)

    def save_image(self, image_tensor):
        # Save image logic
        file_name = f"{self.prefix_append}_combined_mask.png"
        file_path = f"{self.output_dir}/{file_name}"
        print(f"Saving combined mask to {file_path}")
        # Add your preferred image saving logic here

# Node mappings
NODE_CLASS_MAPPINGS = {
    "CombineMasksNode": CombineMasksNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CombineMasksNode": "Combine Masks Node"
}
