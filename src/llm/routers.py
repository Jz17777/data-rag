"""LLM 供应商路由器，通过 Anthropic 兼容接口统一访问各模型供应商。

Usage:
    from src.llm.routers import model_router

    llm = model_router.deepseek
    llm = model_router.mimo
"""

from langchain_anthropic import ChatAnthropic

from src.core.settings import (
    dashscope_settings,
    deepseek_settings,
    minimax_settings,
    mimo_settings,
)


class ProviderRouter:
    """统一管理各 LLM 供应商的 ChatAnthropic 实例，按属性名直接访问。"""

    @property
    def deepseek(self) -> ChatAnthropic:
        """DeepSeek 模型实例。"""
        return ChatAnthropic(
            model=deepseek_settings.model,
            api_key=deepseek_settings.api_key,
            base_url=deepseek_settings.base_url_anthropic,
        )

    @property
    def minimax(self) -> ChatAnthropic:
        """MiniMax 模型实例。"""
        return ChatAnthropic(
            model=minimax_settings.model,
            api_key=minimax_settings.api_key,
            base_url=minimax_settings.base_url_anthropic,
        )

    @property
    def dashscope(self) -> ChatAnthropic:
        """通义千问模型实例。"""
        return ChatAnthropic(
            model=dashscope_settings.model,
            api_key=dashscope_settings.api_key,
            base_url=dashscope_settings.base_url,
        )

    @property
    def mimo(self) -> ChatAnthropic:
        """Mimo 模型实例。"""
        return ChatAnthropic(
            model=mimo_settings.model,
            api_key=mimo_settings.api_key,
            base_url=mimo_settings.base_url_anthropic,
        )


model_router = ProviderRouter()

if __name__ == "__main__":
    # 测试各模型实例是否正确创建
    print(model_router.deepseek)
    print(model_router.minimax)
    print(model_router.dashscope)
    print(model_router.mimo)