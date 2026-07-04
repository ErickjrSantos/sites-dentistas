import csv
import json
import re
from pathlib import Path
from urllib.parse import quote_plus

base = Path(__file__).parent.parent
csv_path = base / "data" / "leads-moema.csv"
out_dir = base / "previews"
out_dir.mkdir(parents=True, exist_ok=True)


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


with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
    leads = list(csv.DictReader(f))

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
        "has_whatsapp": has_whatsapp,
    }
    (clinic_dir / "data.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    cards_html = "".join(
        f'<article class="card"><span class="badge">{title}</span><h3>{title}</h3><p>{desc}</p></article>'
        for title, desc in conf["services"]
    )
    diff_html = "".join(f"<li>{d}</li>" for d in conf["differentials"])
    faq_html = "".join(
        f'<article class="faq-item"><h3>{q}</h3><p>{a}</p></article>'
        for q, a in conf["faq"]
    )
    theme_css = f":root{{--bg:{theme['bg']};--text:{theme['text']};--muted:{theme['muted']};--primary:{theme['primary']};--secondary:{theme['secondary']};--surface:{theme['accent']};--line:{'#2f2f2f' if theme['dark'] else '#dce6ef'};--shadow:rgba(0,0,0,.18) 0 22px 44px -26px,rgba(0,0,0,.08) 0 12px 24px -18px;}}"
    theme_css += "\n    .cta,.ghost,.float{transition:transform 0.2s ease, filter 0.2s ease;}\n    .cta:hover,.ghost:hover,.float:hover{filter:brightness(1.1);transform:translateY(-2px)}\n    .cta:focus-visible,.ghost:focus-visible,.float:focus-visible{outline:2px solid var(--primary);outline-offset:4px}\n    .card,.panel,.contact-card{transition:transform 0.3s ease;}\n    .card:hover,.panel:hover,.contact-card:hover{transform:translateY(-4px)}"
    phone_line = f'<p><strong>Telefone / WhatsApp:</strong> {row["phone"]}</p>' if row["phone"] else '<p><strong>Contato público:</strong> não capturado nesta rodada</p>'
    hours_line = f'<p><strong>Horário exibido:</strong> {row["hours"]}</p>' if row["hours"] else ""
    cta_secondary = "Abrir localização" if not has_whatsapp else "Ver especialidades"
    cta_secondary_href = map_link(row["address"]) if not has_whatsapp else "#especialidades"
    cta_secondary_attr = ' target="_blank" rel="noopener noreferrer"' if not has_whatsapp else ""
    final_cta = ("Falar pelo WhatsApp", cta_href, cta_attr) if has_whatsapp else ("Ver contato", "#contato", "")

    html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{conf['brand']} | Preview Comercial em Moema</title>
  <meta name="description" content="{conf['subbrand']}" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    {theme_css}
    *{{box-sizing:border-box}} html{{scroll-behavior:smooth}} body{{margin:0;font-family:'Inter',system-ui,sans-serif;background:var(--bg);color:var(--text)}}
    .container{{max-width:1180px;margin:auto;padding:0 22px}} .nav{{display:flex;justify-content:space-between;align-items:center;padding:26px 0}}
    .brand{{font-size:24px;font-weight:800;letter-spacing:-.03em}} .brand span{{color:var(--primary)}}
    .cta,.ghost,.float{{display:inline-flex;align-items:center;justify-content:center;gap:10px;text-decoration:none;font-weight:700;border-radius:16px;transition:.2s ease}}
    .cta{{background:var(--primary);color:{'#111' if theme['dark'] else '#fff'};padding:14px 20px;box-shadow:var(--shadow)}} .cta:hover{{transform:translateY(-1px)}}
    .ghost{{padding:14px 20px;border:1px solid var(--line);color:var(--text);background:rgba(255,255,255,.06)}}
    .hero{{display:grid;grid-template-columns:1.08fr .92fr;gap:26px;align-items:center;padding:24px 0 56px}}
    .kicker{{display:inline-block;padding:8px 12px;border-radius:999px;background:{'rgba(217,179,106,.12)' if theme['dark'] else 'rgba(0,0,0,.05)'};color:var(--primary);font-weight:800;font-size:12px;letter-spacing:.1em;text-transform:uppercase}}
    h1{{font-size:clamp(40px,6vw,74px);line-height:.95;letter-spacing:-.05em;margin:16px 0 16px}} .hero p{{font-size:19px;line-height:1.7;color:var(--muted);max-width:660px}}
    .actions{{display:flex;gap:14px;flex-wrap:wrap;margin-top:26px}} .panel,.card,.faq-item,.contact-card,.summary{{background:var(--surface);border:1px solid var(--line);border-radius:26px;box-shadow:var(--shadow)}}
    .panel{{padding:24px}} .summary{{padding:18px}} .badge{{display:inline-flex;padding:8px 12px;border-radius:999px;background:{'#171717' if theme['dark'] else '#fff'};border:1px solid var(--line);font-size:12px;font-weight:800;color:var(--text)}}
    .stats{{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-top:18px}} .stat{{padding:16px;border-radius:18px;background:{'#171717' if theme['dark'] else '#fff'};border:1px solid var(--line)}}
    .stat strong{{display:block;font-size:24px}} .stat span{{color:var(--muted);font-size:14px}}
    section{{padding:34px 0}} .section-head{{display:flex;justify-content:space-between;gap:20px;align-items:end;margin-bottom:20px}} .section-head h2{{font-size:34px;letter-spacing:-.04em;margin:0}} .section-head p{{max-width:560px;margin:0;color:var(--muted);line-height:1.7}}
    .grid-3{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}} .grid-2{{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}} .card,.faq-item,.contact-card{{padding:22px}} .card h3,.faq-item h3{{margin:14px 0 10px;font-size:24px;letter-spacing:-.03em}} .card p,.faq-item p,.contact-card p{{color:var(--muted);line-height:1.7}}
    .brand-block{{display:grid;grid-template-columns:.9fr 1.1fr;gap:18px}} .portrait{{min-height:350px;border-radius:28px;border:1px solid var(--line);background:linear-gradient(160deg,var(--secondary),{theme['bg']} 52%,var(--surface));position:relative;overflow:hidden;box-shadow:var(--shadow)}}
    .portrait:before{{content:'';position:absolute;inset:11% 10%;border-radius:32px;background:radial-gradient(circle at 28% 20%,rgba(255,255,255,.9),transparent 28%),linear-gradient(180deg,rgba(255,255,255,.86),rgba(255,255,255,.28));border:1px solid rgba(255,255,255,.55)}}
    .portrait:after{{content:'{conf['brand']}';position:absolute;left:22px;bottom:22px;padding:10px 14px;border-radius:999px;background:{'#111' if theme['dark'] else 'rgba(255,255,255,.9)'};color:{'#f7f1e8' if theme['dark'] else theme['text']};font-weight:800}}
    ul.clean{{margin:14px 0 0;padding-left:20px;color:var(--muted);line-height:1.8}} .final{{padding:34px;border-radius:30px;background:linear-gradient(135deg,var(--primary),var(--secondary));color:{'#111' if theme['dark'] else '#fff'};box-shadow:var(--shadow)}}
    .float{{position:fixed;right:18px;bottom:18px;background:var(--primary);color:{'#111' if theme['dark'] else '#fff'};padding:14px 18px;box-shadow:var(--shadow)}}
    .link{{color:var(--primary);font-weight:700;text-decoration:none}} .subtle{{color:var(--muted)}}
    @media (max-width: 940px){{.hero,.brand-block,.grid-3,.grid-2,.stats{{grid-template-columns:1fr}} .nav{{flex-direction:column;align-items:flex-start;gap:12px}} h1{{font-size:52px}} .float{{left:16px;right:16px;bottom:16px}}}}
  </style>
</head>
<body>
  <div class="container">
    <nav class="nav">
      <div class="brand">{conf['brand'].split()[0]} <span>{' '.join(conf['brand'].split()[1:])}</span></div>
      <a class="cta" href="{cta_href}"{cta_attr}>{cta_label}</a>
    </nav>
    <section class="hero">
      <div>
        <span class="kicker">{conf['kicker']}</span>
        <h1>{conf['headline']}</h1>
        <p>{conf['intro']}</p>
        <div class="actions">
          <a class="cta" href="{cta_href}"{cta_attr}>{cta_label}</a>
          <a class="ghost" href="{cta_secondary_href}"{cta_secondary_attr}>{cta_secondary}</a>
        </div>
      </div>
      <div class="panel">
        <span class="badge">Moema • {row['category']}</span>
        <h2 style="font-size:32px;letter-spacing:-.04em;margin:18px 0 10px">{conf['subbrand']}</h2>
        <p class="subtle">Esse preview foi estruturado para transmitir mais valor percebido, clareza comercial e facilitar o primeiro passo do paciente.</p>
        <div class="stats">
          <div class="stat"><strong>{row['rating']}</strong><span>nota pública exibida na rodada</span></div>
          <div class="stat"><strong>{row['fit_with_plan'].capitalize()}</strong><span>aderência ao plano comercial</span></div>
          <div class="stat"><strong>Moema</strong><span>forte contexto local para captação</span></div>
          <div class="stat"><strong>{'WhatsApp' if has_whatsapp else 'Contato seguro'}</strong><span>{'CTA direto com telefone público' if has_whatsapp else 'sem inventar canal não capturado'}</span></div>
        </div>
      </div>
    </section>
    <section id="especialidades">
      <div class="section-head">
        <h2>Estrutura pensada para valor, clareza e decisão.</h2>
        <p>O objetivo é mostrar uma versão mais organizada e comercial da presença digital do consultório, respeitando o posicionamento percebido deste lead.</p>
      </div>
      <div class="grid-3">{cards_html}</div>
    </section>
    <section class="brand-block">
      <div class="portrait"></div>
      <div class="panel">
        <span class="badge">Diferenciação visual própria</span>
        <h2 style="font-size:38px;letter-spacing:-.05em;margin:14px 0 10px">Uma identidade visual distinta para este consultório.</h2>
        <p class="subtle">Cada preview foi desenhado com uma direção visual própria para evitar repetição e reforçar melhor o caráter de cada marca ou profissional.</p>
        <div class="summary">
          <strong style="font-size:18px">Direção desta versão</strong>
          <ul class="clean">{diff_html}</ul>
        </div>
      </div>
    </section>
    <section>
      <div class="section-head">
        <h2>Perguntas e objeções mais comuns.</h2>
        <p>Um FAQ curto ajuda o paciente a avançar mais rápido para contato, especialmente quando o objetivo é captação local.</p>
      </div>
      <div class="grid-2">{faq_html}</div>
    </section>
    <section id="contato">
      <div class="section-head">
        <h2>Contato e localização</h2>
        <p>Todos os dados abaixo vieram da coleta pública desta rodada.</p>
      </div>
      <div class="grid-3">
        <article class="contact-card">
          <span class="badge">Contato</span>
          <h3 style="margin:14px 0 10px">{conf['brand']}</h3>
          {phone_line}
          {hours_line}
        </article>
        <article class="contact-card">
          <span class="badge">Localização</span>
          <h3 style="margin:14px 0 10px">Endereço público</h3>
          <p>{row['address']}</p>
          <a class="link" href="{map_link(row['address'])}" target="_blank" rel="noopener noreferrer">Abrir no mapa</a>
        </article>
        <article class="contact-card">
          <span class="badge">Leitura comercial</span>
          <h3 style="margin:14px 0 10px">Resumo do lead</h3>
          <p>{row['notes']}</p>
        </article>
      </div>
    </section>
    <section class="final">
      <h2 style="font-size:40px;letter-spacing:-.05em;margin:0 0 10px">{conf['brand']} com uma presença digital mais forte, clara e pronta para converter.</h2>
      <p style="max-width:760px;line-height:1.7">Este preview mostra como a marca pode parecer mais atual, mais organizada e mais orientada a contato comercial sem depender de stack complexa.</p>
      <div class="actions">
        <a class="cta" href="{final_cta[1]}"{final_cta[2]}>{final_cta[0]}</a>
        <a class="ghost" href="../index.html">Voltar ao índice</a>
      </div>
    </section>
  </div>
  <a class="float" href="{cta_href}"{cta_attr}>{'WhatsApp' if has_whatsapp else 'Contato'}</a>
</body>
</html>'''
    (clinic_dir / "index.html").write_text(html, encoding="utf-8")

cards = []
for row in leads:
    conf = custom[row["name"]]
    slug = slugify(conf["brand"])
    cards.append(
        f'<article class="card"><span class="badge">{row["category"]}</span><h2>{conf["brand"]}</h2><p>{conf["subbrand"]}</p><p class="muted"><strong>Nota pública:</strong> {row["rating"]}<br><strong>Fit:</strong> {row["fit_with_plan"]}<br><strong>Bairro:</strong> Moema</p><a class="cta" href="./{slug}/index.html" aria-label="Abrir preview de {conf["brand"]}">Abrir preview</a></article>'
    )

index_html = f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Previews Moema | Fábrica Autônoma de Sites</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root{{--bg:#0f172a;--card:#fff;--text:#e5edf9;--muted:#9fb3d1;--ink:#10223d;--primary:#7c9cff;--shadow:rgba(0,0,0,.24) 0 22px 44px -26px}}
    *{{box-sizing:border-box}} body{{margin:0;font-family:'Inter',system-ui,sans-serif;background:linear-gradient(180deg,#0b1220,#15233f);color:var(--text)}}
    .container{{max-width:1240px;margin:auto;padding:32px 22px 56px}} h1{{font-size:56px;letter-spacing:-.05em;margin:0 0 12px}} p.lead{{max-width:820px;color:var(--muted);line-height:1.8;font-size:18px}}
    .grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:28px}} .card{{background:var(--card);border-radius:28px;padding:22px;border:1px solid #dbe6ff;box-shadow:var(--shadow);color:var(--ink)}}
    .card h2{{margin:14px 0 10px;font-size:28px;letter-spacing:-.03em}} .card p{{line-height:1.7}} .muted{{color:#51627e}} .badge{{display:inline-flex;padding:8px 12px;border-radius:999px;background:#eef4ff;border:1px solid #d4e1fb;font-size:12px;font-weight:800;color:#335085}}
    .cta{{display:inline-flex;margin-top:14px;padding:13px 18px;border-radius:14px;background:var(--primary);color:#fff;text-decoration:none;font-weight:800;transition:transform 0.2s ease, filter 0.2s ease}}
    .cta:hover{{filter:brightness(1.1);transform:translateY(-2px)}}
    .cta:focus-visible{{outline:2px solid var(--primary);outline-offset:4px}}
    .card{{transition:transform 0.3s ease}} .card:hover{{transform:translateY(-4px)}}
    @media (max-width: 980px){{.grid{{grid-template-columns:1fr}} h1{{font-size:42px}}}}
  </style>
</head>
<body>
  <div class="container">
    <span class="badge">Dentistas em Moema • 6 previews</span>
    <h1>Previews comerciais individuais com identidade visual própria.</h1>
    <p class="lead">Cada consultório prospectado recebeu uma direção visual distinta para facilitar comparação, apresentação e priorização comercial. Os arquivos foram gerados localmente a partir dos dados públicos capturados na rodada.</p>
    <div class="grid">{"".join(cards)}</div>
  </div>
</body>
</html>'''
(out_dir / "index.html").write_text(index_html, encoding="utf-8")

print("OK")
for row in leads:
    print(slugify(custom[row["name"]]["brand"]))
