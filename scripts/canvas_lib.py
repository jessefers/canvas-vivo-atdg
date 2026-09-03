#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""canvas_lib — utilidades compartilhadas dos scripts do Canvas Vivo ATDG (somente biblioteca padrão).

Funções: carga/gravação de JSON, organograma canônico (códigos, siglas, id_app), seleção de entradas por setor,
hash de fontes, versão semântica, front matter das diretrizes, lições, validador de esquema mínimo.
"""
import datetime
import glob
import hashlib
import io
import json
import os
import re
import unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))


def path(*parts):
    return os.path.join(ROOT, *parts)


DATA_JSON = path('data.json')
ORG_JSON = path('diretrizes', '03-organograma-canonico.json')
POPS_DIR = path('pops')
DIAG_DIR = path('diagnosticos')
AG_REG = path('agentes', 'registry.json')
DIR_DIR = path('diretrizes')
SCHEMAS_DIR = path('schemas')
AGENTS_DIR = path('.claude', 'agents')

# ── JSON ────────────────────────────────────────────────────────────────────

def load_json(p, default=None):
    if not os.path.exists(p):
        if default is not None:
            return default
        raise FileNotFoundError(p)
    with io.open(p, encoding='utf-8') as f:
        return json.load(f)


def save_json(p, obj):
    os.makedirs(os.path.dirname(p) or '.', exist_ok=True)
    with io.open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(obj, ensure_ascii=False, indent=2) + '\n')


def dumps(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2)


def load_data():
    return load_json(DATA_JSON)


def save_data(data):
    ordered = {}
    for k in ('entries', 'versao', 'sincronizado_em', 'diretrizes', 'licoes', 'pops', 'diagnosticos', 'agentes'):
        if k in data:
            ordered[k] = data[k]
    for k, v in data.items():
        if k not in ordered:
            ordered[k] = v
    save_json(DATA_JSON, ordered)


# ── Tempo, texto, hash ──────────────────────────────────────────────────────

def now_iso():
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def today():
    return now_iso()[:10]


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFKD', s or '') if not unicodedata.combining(c))


def norm(s):
    return re.sub(r'\s+', ' ', strip_accents(str(s or '')).lower()).strip()


def slugify(s, maxlen=60):
    s = strip_accents(str(s or '')).lower()
    s = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return s[:maxlen].strip('-')


def sha256(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def hash_fontes(entries_or_ids):
    """SHA-256 de 'id|ts' ordenados (aceita entradas completas ou ids)."""
    keys = []
    for e in entries_or_ids or []:
        if isinstance(e, dict):
            keys.append('%s|%s' % (e.get('id', ''), e.get('ts', '')))
        else:
            keys.append('%s|' % e)
    return sha256('\n'.join(sorted(keys)))


def entries_hash(entries):
    return sha256(json.dumps(entries, ensure_ascii=False, sort_keys=True))


# ── Versão semântica ────────────────────────────────────────────────────────

ORDEM_TIPO = {'patch': 0, 'minor': 1, 'major': 2}


def version_tuple(v):
    parts = [int(x) if x.isdigit() else 0 for x in str(v or '0').lstrip('vV').split('.')]
    while len(parts) < 3:
        parts.append(0)
    return tuple(parts[:3])


def cmp_version(a, b):
    ta, tb = version_tuple(a), version_tuple(b)
    return (ta > tb) - (ta < tb)


def bump_version(v, tipo):
    major, minor, patch = version_tuple(v)
    if tipo == 'major':
        return '%d.0.0' % (major + 1)
    if tipo == 'minor':
        return '%d.%d.0' % (major, minor + 1)
    return '%d.%d.%d' % (major, minor, patch + 1)


def max_tipo(a, b):
    return a if ORDEM_TIPO.get(a, 0) >= ORDEM_TIPO.get(b, 0) else b


# ── Organograma canônico ────────────────────────────────────────────────────

class Org:
    def __init__(self, data=None):
        self.data = data or load_json(ORG_JSON)
        self.setores = self.data['setores']
        self.by_codigo = {s['codigo']: s for s in self.setores}
        self.by_sigla = {s['sigla'].upper(): s for s in self.setores}
        self.by_app = {}
        for s in self.setores:
            for lbl in [s.get('id_app')] + list(s.get('aliases') or []):
                if lbl:
                    self.by_app.setdefault(norm(lbl), []).append(s)

    def find(self, q):
        """Localiza setor por código, sigla, rótulo do app (id_app/alias) ou nome."""
        if not q:
            return None
        q = str(q).strip()
        if q in self.by_codigo:
            return self.by_codigo[q]
        if q.upper() in self.by_sigla:
            return self.by_sigla[q.upper()]
        nodes = self.by_app.get(norm(q))
        if nodes:
            return sorted(nodes, key=lambda s: s['nivel'])[0]
        for s in self.setores:  # prefixo de código (S03) ou nome parcial
            if s['codigo'].startswith(q.upper() + '-') or s['codigo'].split('-')[0] == q.upper():
                return s
        nq = norm(q)
        for s in self.setores:
            if nq and nq in norm(s['nome']):
                return s
        return None

    def chain(self, codigo):
        out = []
        node = self.by_codigo.get(codigo)
        while node:
            out.insert(0, node)
            node = self.by_codigo.get(node.get('pai')) if node.get('pai') else None
        return out

    def children(self, codigo):
        return [s for s in self.setores if s.get('pai') == codigo]

    def descendants(self, codigo):
        out = []
        for c in self.children(codigo):
            out.append(c)
            out.extend(self.descendants(c['codigo']))
        return out

    def app_labels(self, node, include_children=True):
        nodes = [node] + (self.descendants(node['codigo']) if include_children else [])
        labels = set()
        for n in nodes:
            for lbl in [n.get('id_app')] + list(n.get('aliases') or []):
                if lbl:
                    labels.add(lbl)
        return labels

    def entries_for(self, entries, node, include_children=True):
        """Entradas do setor (e subdivisões). Frentes com filtro_regex filtram por palavras-chave."""
        labels = self.app_labels(node, include_children)
        res = [e for e in entries if e.get('setor') in labels]
        rx = node.get('filtro_regex')
        if rx:
            res = [e for e in res if re.search(rx, text_of_entry(e), re.I)]
        return sorted(res, key=lambda e: e.get('ts', ''))

    def level1(self):
        return [s for s in self.setores if s['nivel'] == 1]

    def pop_dir(self, node):
        return os.path.join(POPS_DIR, node['sigla'])


def text_of_entry(e):
    p = e.get('p') or {}
    parts = [e.get('desc', ''), p.get('titulo', ''), p.get('resumo', ''), ' '.join(p.get('procedimento') or []),
             ' '.join(p.get('atencoes') or []), p.get('normativa', ''), (e.get('arquivo') or {}).get('nome', ''),
             json.dumps(e.get('estrutura') or {}, ensure_ascii=False)]
    return ' '.join(str(x) for x in parts if x)


def summarize_entry(e, chars=400):
    p = e.get('p') or {}
    est = e.get('estrutura') or {}
    return {
        'id': e.get('id'), 'ts': e.get('ts'), 'tipo': e.get('tipo'), 'setor': e.get('setor'),
        'titulo': p.get('titulo', ''), 'resumo': (p.get('resumo') or e.get('desc') or '')[:chars],
        'procedimento': p.get('procedimento') or [], 'atencoes': p.get('atencoes') or [],
        'responsavel': e.get('responsavel') or p.get('responsavel') or '',
        'estrutura': {k: v for k, v in est.items() if v}, 'normativa': p.get('normativa', ''),
        'class': p.get('class', ''), 'arquivo': (e.get('arquivo') or {}).get('nome', ''),
    }


# ── Códigos e arquivos de POP ───────────────────────────────────────────────

def sigla_of_code(codigo):
    return codigo.rsplit('-', 1)[0]


def pop_id(codigo):
    return 'pop-' + codigo.lower()


def pop_paths(pop_or_codigo, org=None):
    codigo = pop_or_codigo['codigo'] if isinstance(pop_or_codigo, dict) else pop_or_codigo
    sigla = sigla_of_code(codigo)
    d = os.path.join(POPS_DIR, sigla)
    return (os.path.join(d, codigo + '.pop.json'), os.path.join(d, codigo + '.md'), os.path.join(d, codigo + '.bpmn.json'))


def iter_pops():
    pops = []
    for f in sorted(glob.glob(os.path.join(POPS_DIR, '*', '*.pop.json'))):
        pops.append(load_json(f))
    return pops


def load_pop(codigo):
    p = pop_paths(codigo)[0]
    if not os.path.exists(p):
        raise FileNotFoundError('POP não encontrado: %s' % p)
    return load_json(p)


def next_process_number(sigla, existing_codes):
    nums = [int(c.rsplit('-', 1)[1]) for c in existing_codes if c.rsplit('-', 1)[0] == sigla and c.rsplit('-', 1)[1].isdigit()]
    return (max(nums) + 1) if nums else 1


# ── Diretrizes: front matter, versão, lições ────────────────────────────────

def read_front_matter(text):
    m = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            if ':' in line:
                k, v = line.split(':', 1)
                fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm


def diretrizes_files():
    return sorted(glob.glob(os.path.join(DIR_DIR, '0*.md')))


def diretrizes_versao():
    best = '0.0'
    for f in diretrizes_files():
        fm = read_front_matter(io.open(f, encoding='utf-8').read())
        if cmp_version(fm.get('versao', '0'), best) > 0:
            best = fm.get('versao')
    return best


def parse_licoes(md_text):
    """Extrai lições das tabelas de 07-licoes-aprendidas.md (vigentes, pendentes, rejeitadas)."""
    licoes = []
    for line in md_text.splitlines():
        if not line.startswith('| L-'):
            continue
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) < 6:
            continue
        licoes.append({'id': cells[0], 'data': cells[1], 'origem': cells[2], 'licao': cells[3], 'regra': cells[4], 'status': cells[5]})
    return licoes


def licoes_aprovadas():
    f = os.path.join(DIR_DIR, '07-licoes-aprendidas.md')
    if not os.path.exists(f):
        return []
    return [l for l in parse_licoes(io.open(f, encoding='utf-8').read()) if l['status'] == 'aprovada']


def next_licao_id():
    f = os.path.join(DIR_DIR, '07-licoes-aprendidas.md')
    ids = [int(l['id'][2:]) for l in parse_licoes(io.open(f, encoding='utf-8').read()) if l['id'][2:].isdigit()] if os.path.exists(f) else []
    return 'L-%03d' % ((max(ids) + 1) if ids else 1)


# ── Validador de esquema mínimo (subconjunto do JSON Schema) ───────────────

def load_schema(name):
    return load_json(os.path.join(SCHEMAS_DIR, name))


_TYPES = {'object': dict, 'array': list, 'string': str, 'integer': int, 'number': (int, float), 'boolean': bool}


def validate_schema(obj, schema, where='$'):
    errs = []
    t = schema.get('type')
    if t:
        pyt = _TYPES.get(t)
        ok = isinstance(obj, pyt) and not (t in ('integer', 'number') and isinstance(obj, bool))
        if t == 'integer' and isinstance(obj, float) and obj.is_integer():
            ok = True
        if not ok:
            return ['%s: esperado %s, obtido %s' % (where, t, type(obj).__name__)]
    if 'enum' in schema and obj not in schema['enum']:
        errs.append('%s: valor %r fora de %s' % (where, obj, schema['enum']))
    if isinstance(obj, str):
        if 'minLength' in schema and len(obj) < schema['minLength']:
            errs.append('%s: tamanho mínimo %d' % (where, schema['minLength']))
        if 'pattern' in schema and not re.search(schema['pattern'], obj):
            errs.append('%s: %r não corresponde a %s' % (where, obj, schema['pattern']))
    if isinstance(obj, (int, float)) and not isinstance(obj, bool):
        if 'minimum' in schema and obj < schema['minimum']:
            errs.append('%s: mínimo %s' % (where, schema['minimum']))
        if 'maximum' in schema and obj > schema['maximum']:
            errs.append('%s: máximo %s' % (where, schema['maximum']))
    if isinstance(obj, dict):
        for r in schema.get('required', []):
            if r not in obj:
                errs.append('%s: campo obrigatório ausente: %s' % (where, r))
        for k, sub in (schema.get('properties') or {}).items():
            if k in obj:
                errs.extend(validate_schema(obj[k], sub, where + '.' + k))
    if isinstance(obj, list):
        if 'minItems' in schema and len(obj) < schema['minItems']:
            errs.append('%s: mínimo de %d itens' % (where, schema['minItems']))
        if 'items' in schema:
            for i, it in enumerate(obj):
                errs.extend(validate_schema(it, schema['items'], '%s[%d]' % (where, i)))
    return errs


# ── SECTORS do index.html (para conferência do organograma) ────────────────

def sectors_from_index():
    src = io.open(path('index.html'), encoding='utf-8').read()
    m = re.search(r'const SECTORS = \[(.*?)\n\];', src, re.S)
    if not m:
        return set()
    ids = set(re.findall(r"\{id:'([^']+)'", m.group(1)))
    for subs in re.findall(r"subs:\[([^\]]*)\]", m.group(1)):
        ids.update(re.findall(r"'([^']+)'", subs))
    return ids


def select_options_from_index():
    src = io.open(path('index.html'), encoding='utf-8').read()
    m = re.search(r'<select class="fs" id="inSetor">(.*?)</select>', src, re.S)
    return set(re.findall(r'<option>([^<]+)</option>', m.group(1))) if m else set()
