"""This module provides example tools for web scraping and search functionality.

It includes a basic Tavily search function (as an example)

These tools are intended as free examples to get started. For production use,
consider implementing more robust and specialized tools tailored to your needs.
"""

from typing import Any, Callable, List, Optional, cast

from langchain_tavily import TavilySearch
from langgraph.runtime import get_runtime

from react_agent.context import Context


async def search(query: str) -> Optional[dict[str, Any]]:
    """Search for general web results.

    This function performs a search using the Tavily search engine, which is designed
    to provide comprehensive, accurate, and trusted results. It's particularly useful
    for answering questions about current events.
    """
    runtime = get_runtime(Context)
    wrapped = TavilySearch(max_results=runtime.context.max_search_results)
    return cast(dict[str, Any], await wrapped.ainvoke({"query": query}))


def get_weather(location: str) -> str:
    """指定された都市の天気を返します。
    ただし、このツールは「東京」と「大阪」にしか対応していません。
    それ以外の都市（福岡など）の天気については、こちらで試してみてダメだったら'search' ツール（Web検索）を使って調べてください。
    """
    # queryの中に「東京」が含まれていたら
    if "東京" in location:
        return "東京は快晴で、とても暑いです！嫌い！"
    elif "大阪" in location:
        return "大阪は雨で、寒いです！"
    else:
        return "ちょっとよくわかりません！"


TOOLS: List[Callable[..., Any]] = [search, get_weather]
