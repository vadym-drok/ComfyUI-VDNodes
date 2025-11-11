import re
import logging


class MultiPromptsCombiner:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompts_list": ("STRING",{"multiline": True,"default": ""})
            },
            "optional": {
                "before_prompt": ("STRING",{"multiline": True,"default": ""}),
                "after_prompt": ("STRING",{"multiline": True,"default": ""}),
                "negative": ("STRING",{"multiline": True,"default": ""}),
                "start_frame": ("INT", {"default": 0, "min": 0, "max": 999999, "step": 1}),
                "end_frame": ("INT", {"default": 0, "min": 0, "max": 999999, "step": 1}),
            }
        }

    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("positive", "negative")
    OUTPUT_IS_LIST = (True, True)

    FUNCTION = "doit"
    CATEGORY = "VD_Pack"

    @staticmethod
    def doit(prompts_list, before_prompt='', after_prompt='', negative='', start_frame=0, end_frame=0):
        positive_prompts = []
        negative_prompts = []
        if start_frame > end_frame:
            raise ValueError("start_frame must be less or equal to end_frame")
        try:
            matches = re.findall(
                r"^[ \t]*(#?)[ \t]*<(\d+)>:\s*(.*?)(?=^[ \t]*#?[ \t]*<\d+>:|\Z)",
                prompts_list,
                re.DOTALL | re.MULTILINE
            )
            prompt_dict = {}
            for match in matches:
                # Ignore comment-prompts
                if match[0] != '#':
                    prompt_dict[int(match[1])] = match[2]
            for num, body in sorted(prompt_dict.items()):
                if start_frame <= num <= end_frame:
                    prompt = f"{before_prompt}, {body}, {after_prompt}".strip(", ")
                    positive_prompts.append(prompt)
                    negative_prompts.append(negative)
        except Exception as e:
            logging.error(f"[VD_Pack] MultiPromptsCombiner, an error: {e}.")

        return (positive_prompts, negative_prompts)
