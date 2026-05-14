"""
提示词加载器 - 从 .prompt 文件加载提示词，支持通过属性访问

使用方式：
    from src.core.prompt_loader import prompts

    print(prompts.answer_out)  # 访问 answer_out.prompt 中的内容
"""

from pathlib import Path


class PromptNamespace:
    """支持属性访问的命名空间对象"""

    def __init__(self, data: dict[str, str]):
        for key, value in data.items():
            setattr(self, key, value)

    def __repr__(self) -> str:
        attrs = ", ".join(f"{k}=..." for k in self.__dict__)
        return f"PromptNamespace({attrs})"


class PromptLoader:
    """提示词加载器，从目录中读取所有 .prompt 文件并提供属性访问"""

    @classmethod
    def load(cls, prompt_dir: str | Path) -> PromptNamespace:
        """
        加载指定目录下所有 .prompt 文件，返回一个可通过点号访问的对象。

        Args:
            prompt_dir: 提示词文件所在目录路径

        Returns:
            PromptNamespace 实例，每个 .prompt 文件对应一个属性
        """
        prompt_dir = Path(prompt_dir)
        if not prompt_dir.exists():
            raise FileNotFoundError(f"提示词目录不存在: {prompt_dir}")

        prompts: dict[str, str] = {}
        for file in sorted(prompt_dir.glob("*.prompt")):
            name = file.stem
            with open(file, "r", encoding="utf-8") as f:
                prompts[name] = f.read().strip()

        if not prompts:
            raise ValueError(f"提示词目录为空: {prompt_dir}")

        return PromptNamespace(prompts)


# 默认实例，其他模块直接导入使用
PROMPT_DIR = Path(__file__).resolve().parent.parent / "prompts"
prompts = PromptLoader.load(PROMPT_DIR)

if __name__ == "__main__":
    print(prompts.answer_out)
