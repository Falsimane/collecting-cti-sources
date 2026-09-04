from dataclasses import dataclass, field


@dataclass
class Article:
    url: str
    domain: str
    title: str
    publication_date: str
    content: str


@dataclass
class SourceConfig:
    key: str
    domain: str
    article_path: str | None = None
    engine: str = "httpx"
    needs_filtering: bool = False
    cookie_element: dict = field(default_factory=dict)
    filter_elements: dict = field(default_factory=dict)
    pagination: dict = field(default_factory=dict)
    selectors: dict = field(default_factory=dict)

    @classmethod
    def from_dict(cls, key: str, data: dict) -> "SourceConfig":
        return cls(
            key=key,
            domain=data.get("domain", ""),
            article_path=data.get("article_path"),
            engine=data.get("engine", "httpx"),
            needs_filtering=data.get("needs-filtering", False),
            cookie_element=data.get("cookie_element", {}),
            filter_elements=data.get("filter_elements", {}),
            pagination=data.get("pagination") or {},
            selectors=data.get("selectors") or {},
        )