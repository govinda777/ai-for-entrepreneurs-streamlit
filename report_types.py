from dataclasses import dataclass
from typing import List

@dataclass
class ReportField:
    name: str
    type: str
    required: bool
    description: str

@dataclass
class ReportType:
    name: str
    description: str
    cost: int
    fields: List[ReportField]

BUSINESS_MAP_FIELDS = [
    ReportField("sector", "text", True, "Setor de atuação"),
    ReportField("business_model", "text", True, "Modelo de negócio"),
    ReportField("competitors", "text", True, "Concorrentes principais"),
    ReportField("monthly_revenue", "number", True, "Faturamento mensal"),
    ReportField("employees", "number", True, "Número de colaboradores"),
]

XPERIENCE_FIELDS = [
    ReportField("products", "text", True, "Produtos/serviços atuais"),
    ReportField("differentiators", "text", True, "Diferenciais competitivos"),
    ReportField("customer_pain_points", "text", True, "Dores do cliente-alvo"),
    ReportField("strategic_goals", "text", True, "Objetivos estratégicos"),
    ReportField("available_resources", "text", True, "Recursos disponíveis"),
]

SEO_FIELDS = [
    ReportField("website_url", "text", True, "URL do site"),
    ReportField("target_keywords", "text", True, "Palavras-chave alvo"),
    ReportField("digital_competitors", "text", True, "Concorrentes digitais"),
    ReportField("marketing_channels", "text", True, "Canais de marketing utilizados"),
    ReportField("online_goals", "text", True, "Objetivos da presença online"),
]

REPORT_TYPES = [
    ReportType(
        "Mapa do Seu Negócio",
        "Análise completa do seu modelo de negócio e posicionamento no mercado",
        1,
        BUSINESS_MAP_FIELDS
    ),
    ReportType(
        "Relatório Xperience",
        "Estratégia de diferenciação e inovação baseada na metodologia Oceano Azul",
        1,
        XPERIENCE_FIELDS
    ),
    ReportType(
        "Relatório SEO",
        "Otimização da presença digital e estratégia de marketing online",
        1,
        SEO_FIELDS
    ),
] 