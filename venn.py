import matplotlib.pyplot as plt
from matplotlib_venn import venn2
deepseek = {"thinking", "max_tokens", "system", "..."}
openai = {"developer", "max_tokens", "reasoning","..."}

only_deepseek = deepseek - openai
both = deepseek & openai
only_openai = openai - deepseek
def format_region(items):
    text = "\n".join(sorted(items))
    return f"{text}\n..." if text else "..."
plt.figure(figsize=(6, 4))
v = venn2(
    subsets=(
        len(only_deepseek),
        len(both),
        len(only_openai)
    ),
    set_labels=("DeepSeek", "OpenAI")
)

v.get_label_by_id("10").set_text(format_region(only_deepseek))
v.get_label_by_id("11").set_text(format_region(both))
v.get_label_by_id("01").set_text(format_region(only_openai))
plt.savefig("venn.svg", bbox_inches="tight")
plt.show()