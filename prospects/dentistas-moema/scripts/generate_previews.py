import csv
import json
import re
from pathlib import Path
from urllib.parse import quote_plus
from jinja2 import Environment, FileSystemLoader

# Configuração de caminhos
base = Path(__file__).parent.parent
csv_path = base / "data" / "leads-moema.csv"
out_dir = base / "previews"
template_dir = base / "templates"
out_dir.mkdir(parents=True, exist_ok=True)

# Configuração Jinja2
env = Environment(loader=FileSystemLoader(template_dir))

def slugify(name: str) -> str:
    s = name.lower()
    repl = {
        "á": "a", "à": "a", "ã": "a", "â": "a", "ä": "a",
        "é": "e", "ê": "e", "è": "e", "ë": "e",
        "í": "i", "ì": "i", "î": "i", "ï": "i",
        "ó": "o", "ò": "o", "õ": "o", "ô": "o", "ö": "o",
        "ú": "u", "ù": "u", "û": "u", "ü": "u",
        "ç": "c",
    }
    for a, b in repl.items():
        s = s.replace(a, b)
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")

def phone_digits(phone: str) -> str:
    digits = re.sub(r"\D", "", phone or "")
    if digits and len(digits) in (10, 11):
        digits = "55" + digits
    return digits

def map_link(address: str) -> str:
    return f"https://www.google.com/maps/search/?api=1&query={quote_plus(address)}"

# Filtros personalizados Jinja2
env.filters["map_link"] = map_link

# Carregar dados
with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
    leads = list(csv.DictReader(f))

# Dicionário de configurações customizadas (conforme script original)
custom = {
    "Dentista Moema - TCR Odontologia": {
        "brand": "TCR Odontologia",
        "subbrand": "Estética, clareamento e transformação do sorriso em Moema",
        "theme": {"bg": "#fffaf2", "text": "#28190e", "muted": "#7a5a45", "primary": "#b7772e", "secondary": "#f7d9b1", "accent": "#fff1de", "dark": False},
        "kicker": "Sorriso • Estética • Moema",
        "headline": "Um sorriso mais confiante começa com uma experiência mais clara e acolhedora.",
        "intro": "Uma comunicação mais elegante ajuda pacientes a perceber valor logo no primeiro contato. Para uma clínica com apelo estético, o site precisa transmitir desejo, leveza e segurança.",
        "services": [("Clareamento", "Para quem quer brilho, leveza e imagem mais cuidada."), ("Facetas", "Posicionamento ideal para estética dental com alto valor percebido."), ("Avaliação personalizada", "Primeira conversa com CTA claro para acelerar o contato.")],
        "differentials": ["Visual mais aspiracional", "CTA forte para pacientes de estética", "Tom comercial orientado a desejo e confiança"],
        "faq": [("Esse posicionamento funciona para estética?", "Sim. O foco em imagem, leveza e clareza comercial conversa bem com pacientes de maior intenção."), ("O WhatsApp ajuda na conversão?", "Sim. Ele reduz atrito e acelera o início da conversa.")],
    },
    "Ferraz e Fonseca Odontologia": {
        "brand": "Ferraz & Fonseca",
        "subbrand": "Infraestrutura moderna e atendimento odontológico em Moema",
        "theme": {"bg": "#f4f8fc", "text": "#11253e", "muted": "#5f738c", "primary": "#183b6b", "secondary": "#d8e7ff", "accent": "#ffffff", "dark": False},
        "kicker": "Infraestrutura • Conforto • Moema",
        "headline": "Odontologia com estrutura moderna, conveniência e comunicação que transmite confiança.",
        "intro": "Quando a clínica já tem boa percepção de infraestrutura, o preview precisa reforçar organização, conforto e praticidade para o paciente decidir com mais rapidez.",
        "services": [("Clínica geral", "Bloco institucional com linguagem segura e bem resolvida."), ("Avaliação com conveniência", "Estacionamento e localização viram argumentos de decisão."), ("Atendimento moderno", "Design mais sóbrio para valorizar estrutura e profissionalismo.")],
        "differentials": ["Tom institucional premium", "Ênfase em conveniência local", "Layout limpo e profissional"],
        "faq": [("Vale destacar infraestrutura?", "Sim. Isso reduz incerteza e aumenta a percepção de valor."), ("Esse layout serve para clínica mais ampla?", "Sim. Ele é versátil para diferentes serviços odontológicos.")],
    },
    "Dra. Elisa Macedo - Dentista Moema | DTM e dor Orofacial, Bruxismo, Prótese, Facetas, Clareamento": {
        "brand": "Dra. Elisa Macedo",
        "subbrand": "DTM, dor orofacial, prótese, facetas e clareamento",
        "theme": {"bg": "#f4f8ff", "text": "#0a1d34", "muted": "#62748f", "primary": "#5a3bff", "secondary": "#d9edff", "accent": "#ffffff", "dark": False},
        "kicker": "DTM • Bruxismo • Estética • Moema",
        "headline": "Atendimento odontológico com foco em conforto, função e estética.",
        "intro": "Uma presença digital mais clara ajuda pacientes a perceber segurança no diagnóstico, entender o tratamento e avançar mais rápido para a avaliação.",
        "services": [("DTM e dor orofacial", "Comunicação pensada para confiança, escuta e precisão."), ("Bruxismo e prótese", "Posicionamento técnico com linguagem acessível e segura."), ("Facetas e clareamento", "Bloco visual de estética natural e sofisticada.")],
        "differentials": ["Posicionamento premium clínico", "Boa aderência a tratamentos de maior valor", "Leitura simples com CTA forte"],
        "faq": [("O WhatsApp ajuda no primeiro atendimento?", "Sim. É a forma mais rápida de iniciar a conversa."), ("Esse modelo funciona para DTM e estética juntos?", "Sim. A estrutura permite equilibrar autoridade clínica e apelo visual.")],
    },
    "Dr. Joelson Richa": {
        "brand": "Dr. Joelson Richa",
        "subbrand": "Atendimento odontológico em Moema com acesso contínuo",
        "theme": {"bg": "#f3fbf7", "text": "#123126", "muted": "#5d7d71", "primary": "#127a52", "secondary": "#d8f4e7", "accent": "#ffffff", "dark": False},
        "kicker": "Disponibilidade • Moema • Atendimento",
        "headline": "Uma presença digital objetiva para quem quer contato rápido e sensação de cuidado imediato.",
        "intro": "Como o lead aparece com operação 24 horas, o preview foi pensado para transmitir disponibilidade, proximidade e facilidade de acesso, sem inventar canais que não foram capturados publicamente.",
        "services": [("Atendimento odontológico", "Texto direto para facilitar entendimento do paciente."), ("Contato rápido", "Estrutura de conversão focada em reduzir atrito."), ("Presença local", "Moema como reforço de conveniência e confiança.")],
        "differentials": ["Tom mais acessível e direto", "Ênfase em disponibilidade", "CTA seguro sem inventar WhatsApp"],
        "faq": [("Por que não há botão de WhatsApp?", "Porque o telefone não foi capturado nesta rodada; o preview evita informar contato não confirmado."), ("Esse estilo funciona para clínica pessoal?", "Sim. Ele reforça proximidade e acesso rápido.")],
    },
    "Tiger Odontologia": {
        "brand": "Tiger Odontologia",
        "subbrand": "Branding forte e presença digital moderna para clínica odontológica",
        "theme": {"bg": "#fff7f2", "text": "#241813", "muted": "#755d53", "primary": "#f06f2f", "secondary": "#ffd7bf", "accent": "#ffffff", "dark": False},
        "kicker": "Branding • Clínica • Moema",
        "headline": "Uma clínica com nome forte pede um visual memorável, moderno e orientado à ação.",
        "intro": "O preview da Tiger foi construído para valorizar marca própria, dar energia ao visual e mostrar uma comunicação mais atual para captação local.",
        "services": [("Clínica odontológica", "Bloco amplo para serviços diversos com linguagem moderna."), ("Captação local", "Design pensado para destacar a marca e acelerar contato."), ("Apresentação forte", "Visual com mais contraste e personalidade.")],
        "differentials": ["Identidade mais marcante", "Boa aderência a branding próprio", "Layout comercial com energia visual"],
        "faq": [("Vale investir mais em marca própria?", "Sim. Quando o nome da clínica tem força, o design pode amplificar lembrança e diferenciação."), ("Esse modelo ajuda na captação local?", "Sim. Ele une visibilidade de marca com CTA claro.")],
    },
    "LOYS CLINIC": {
        "brand": "LOYS CLINIC",
        "subbrand": "Presença premium para clínica em região nobre de Moema/Ibirapuera",
        "theme": {"bg": "#111111", "text": "#f7f1e8", "muted": "#c7bfb3", "primary": "#d9b36a", "secondary": "#2a2a2a", "accent": "#171717", "dark": True},
        "kicker": "Premium • Ibirapuera • Moema",
        "headline": "Sofisticação, clareza e presença digital à altura de uma clínica premium.",
        "intro": "Para uma clínica posicionada em região nobre, a comunicação precisa transmitir exclusividade, organização e segurança desde a primeira dobra.",
        "services": [("Atendimento premium", "Tom visual mais sóbrio para valorizar exclusividade."), ("Posicionamento local forte", "Endereço e contexto como sinais de valor percebido."), ("Captação qualificada", "Estrutura feita para atrair pacientes com maior intenção.")],
        "differentials": ["Paleta luxo e contraste alto", "Ênfase em sofisticação", "Boa aderência a público premium"],
        "faq": [("Esse visual é mais indicado para ticket alto?", "Sim. A paleta escura com dourado reforça percepção premium."), ("O endereço ajuda no posicionamento?", "Sim. Região forte contribui para autoridade e valor percebido.")],
    },
}

clinics_data = []
clinic_template = env.get_template("clinic_template.html")

for row in leads:
    conf = custom[row["name"]]
    slug = slugify(conf["brand"])
    theme = conf["theme"]
    digits = phone_digits(row["phone"])
    has_whatsapp = bool(digits)
    cta_label = "Agendar pelo WhatsApp" if has_whatsapp else "Ver contato e localização"
    cta_href = f"https://wa.me/{digits}?text=Ol%C3%A1%2C%20gostaria%20de%20agendar%20uma%20avalia%C3%A7%C3%A3o." if has_whatsapp else "#contato"
    cta_attr = ' target="_blank" rel="noopener noreferrer"' if has_whatsapp else ""

    clinic_dir = out_dir / slug
    clinic_dir.mkdir(parents=True, exist_ok=True)

    payload = {
        "name": row["name"],
        "brand": conf["brand"],
        "subbrand": conf["subbrand"],
        "category": row["category"],
        "rating": row["rating"],
        "address": row["address"],
        "phone": row["phone"],
        "hours": row["hours"],
        "fit_with_plan": row["fit_with_plan"],
        "notes": row["notes"],
        "slug": slug,
        "theme": theme,
        "services": conf["services"],
        "differentials": conf["differentials"],
        "faq": conf["faq"],
        "cta_label": cta_label,
        "cta_href": cta_href,
        "cta_attr": cta_attr,
        "has_whatsapp": has_whatsapp,
        "kicker": conf["kicker"],
        "headline": conf["headline"],
        "intro": conf["intro"],
        "cta_secondary": "Abrir localização" if not has_whatsapp else "Ver especialidades",
        "cta_secondary_href": map_link(row["address"]) if not has_whatsapp else "#especialidades",
        "cta_secondary_attr": ' target="_blank" rel="noopener noreferrer"' if not has_whatsapp else ""
    }

    (clinic_dir / "data.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    html = clinic_template.render(**payload)
    (clinic_dir / "index.html").write_text(html, encoding="utf-8")

    clinics_data.append(payload)

# Gerar Índice
index_template = env.get_template("index_template.html")
index_html = index_template.render(clinics=clinics_data)
(out_dir / "index.html").write_text(index_html, encoding="utf-8")

print("OK")
for clinic in clinics_data:
    print(clinic["slug"])
