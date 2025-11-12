# VD Custom Nodes for ComfyUI

## Installation

Navigate to the /ComfyUI/custom_nodes/ folder
```
git clone https://github.com/vadym-drok/ComfyUI-VDNodes
```

## MultiPromptsCombiner Node for ComfyUI

`MultiPromptsCombiner` is a custom ComfyUI node designed to parse multiple prompts from a single multiline input string. 
Prompts are defined using numbered tags (e.g., `<0>: prompt text`) and can be optionally filtered and formatted before being passed to downstream nodes such as `CLIP Text Encode`.

The node supports:
- Commented-out prompt blocks using `#<n>:` or `#  <n>:` syntax.
- Optional prefix (`before_prompt`) and suffix (`after_prompt`) that are added to each valid prompt.
- Frame filtering via `start_frame` and `end_frame` (inclusive range).
- Automatic pairing of positive and negative prompts.
- A single negative prompt that is applied to all positive prompts.
- Automatic sorting of prompts by their numerical order.

---

## Usage

The node takes a `prompts_list` input in the following format:

```text
<0>: A knight in armor
#<1>: A girl with a sword   <-- This line is ignored
<2>: A roaring lion

## Examples

![image](https://github.com/user-attachments/assets/a8559790-d1e0-4aa8-8358-4ffb7c905375)