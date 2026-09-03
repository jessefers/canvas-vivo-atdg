#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""licoes — governa diretrizes/07-licoes-aprendidas.md (append-only) e sincroniza data.json.

Uso:
  python3 scripts/licoes.py listar [--status proposta|aprovada|rejeitada]
  python3 scripts/licoes.py propor "<lição>" "<regra proposta>" [--origem curador]
  python3 scripts/licoes.py aprovar L-NNN
  python3 scripts/licoes.py rejeitar L-NNN "<motivo>"
Aprovar/rejeitar move a linha da tabela de propostas para a tabela correspondente (nova linha; a original é removida
da tabela de pendentes, preservando id, data e origem).
"""
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canvas_lib as cl  # noqa: E402

ARQ = os.path.join(cl.DIR_DIR, '07-licoes-aprendidas.md')
SEC_VIG = '## Regras vigentes (aprovadas)'
SEC_PEND = '## Propostas pendentes'
SEC_REJ = '## Rejeitadas'


def ler():
    return io.open(ARQ, encoding='utf-8').read()


def gravar(txt):
    io.open(ARQ, 'w', encoding='utf-8', newline='\n').write(txt)


def secoes(txt):
    """Divide o arquivo em (cabecalho, vigentes, pendentes, rejeitadas) mantendo os títulos."""
    i1, i2, i3 = txt.index(SEC_VIG), txt.index(SEC_PEND), txt.index(SEC_REJ)
    return txt[:i1], txt[i1:i2], txt[i2:i3], txt[i3:]


def linha_de(sec, lid):
    for line in sec.splitlines():
        if line.startswith('| %s |' % lid):
            return line
    return None


def bump_versao_arquivo(txt):
    fm = cl.read_front_matter(txt)
    nova = cl.bump_version(fm.get('versao', '1.0.0') + ('.0' if fm.get('versao', '').count('.') == 1 else ''), 'minor')
    nova = '.'.join(nova.split('.')[:2])
    txt = re.sub(r'^versao: "[^"]*"', 'versao: "%s"' % nova, txt, count=1, flags=re.M)
    txt = re.sub(r'^atualizado_em: "[^"]*"', 'atualizado_em: "%s"' % cl.today(), txt, count=1, flags=re.M)
    return txt


def propor(licao, regra, origem='curador'):
    txt = ler()
    lid = cl.next_licao_id()
    cab, vig, pend, rej = secoes(txt)
    pend = pend.rstrip('\n') + '\n| %s | %s | %s | %s | %s | proposta |\n\n' % (lid, cl.today(), origem.replace('|', '/'), licao.replace('|', '/').replace('\n', ' '), regra.replace('|', '/').replace('\n', ' '))
    gravar(bump_versao_arquivo(cab + vig + pend + rej))
    print('%s registrada como proposta' % lid)
    return lid


def mover(lid, destino, motivo=''):
    txt = ler()
    cab, vig, pend, rej = secoes(txt)
    linha = linha_de(pend, lid)
    if not linha:
        raise SystemExit('%s não está entre as propostas pendentes' % lid)
    cells = [c.strip() for c in linha.strip().strip('|').split('|')]
    pend = '\n'.join(l for l in pend.splitlines() if not l.startswith('| %s |' % lid)) + '\n\n'
    if destino == 'aprovada':
        vig = vig.rstrip('\n') + '\n| %s | %s | %s | %s | %s | aprovada |\n\n' % (cells[0], cl.today(), cells[2], cells[3], cells[4])
    else:
        rej = rej.rstrip('\n') + '\n| %s | %s | %s | %s | %s | rejeitada |\n' % (cells[0], cl.today(), cells[2], cells[3], (motivo or cells[4]).replace('|', '/'))
    gravar(bump_versao_arquivo(cab + vig + pend + rej))
    print('%s → %s' % (lid, destino))


def listar(status=None):
    for l in cl.parse_licoes(ler()):
        if not status or l['status'] == status:
            print('%s [%s] %s — %s' % (l['id'], l['status'], l['licao'][:80], l['regra'][:100]))


def sync():
    import sync_data
    sync_data.to_data()


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a:
        print(__doc__)
        sys.exit(1)
    cmd = a[0]
    if cmd == 'listar':
        listar(a[a.index('--status') + 1] if '--status' in a else None)
    elif cmd == 'propor':
        origem = a[a.index('--origem') + 1] if '--origem' in a else 'curador'
        propor(a[1], a[2], origem)
        sync()
    elif cmd == 'aprovar':
        mover(a[1], 'aprovada')
        sync()
    elif cmd == 'rejeitar':
        mover(a[1], 'rejeitada', a[2] if len(a) > 2 else '')
        sync()
    else:
        print(__doc__)
        sys.exit(1)
