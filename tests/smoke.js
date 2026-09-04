// Smoke test do Canvas Vivo (Playwright + Chromium pré-instalado). Uso: NODE_PATH=/opt/node22/lib/node_modules node smoke.js
const { chromium } = require('playwright');
process.on('unhandledRejection', e => { console.log('unhandledRejection:', String(e && e.message || e).split('\n')[0]); });
const { spawn } = require('child_process');
const fs = require('fs'); const path = require('path');
const ROOT = path.resolve(__dirname, '..'); const PORT = 8765; const BASE = 'http://127.0.0.1:' + PORT + '/';
const results = []; let failures = 0; let globalErrors = [];
function ok(name, cond, info) { results.push((cond ? 'PASS ' : 'FAIL ') + name + (info ? ' — ' + info : '')); if (!cond) failures++; }
const sleep = ms => new Promise(r => setTimeout(r, ms));
async function step(name, fn) { try { await fn(); } catch (e) { ok(name, false, String(e.message || e).split('\n')[0]); } }
const DIAG = { ecossistema: { dominio: 'Suprimentos e Materiais', subdominios: ['Recebimento'], contextos_vizinhos: ['PRAF'], sistemas: ['GMS'], normas: ['TCE-PR'], benchmarks: [] }, processos: [{ codigo_sugerido: 'ALM-09', nome: 'Processo de teste automatizado', tipo: 'processo', descricao: 'Processo criado pelo teste.', tipo_subdominio: 'core', gatilho: 'Demanda recebida', saida: 'Registro no GMS', atores: ['Div. de Almoxarifado'], sistemas: ['GMS'], artefatos: ['NF'], interfaces: ['PRAF'], evidencias: ['pb-almoxarifado'], maturidade: 2, criticidade: 0.7, frequencia: 0.6, risco_conformidade: 1, cobertura: 0.5, lacunas: ['kpi'], recomendacao: 'gerar_pop', pop_existente: '', justificativa: 'teste' }], lacunas_setor: ['teste'], licoes_propostas: [{ licao: 'Lição de teste', regra: 'Regra de teste', exemplo: 'ALM-09', origem: 'diag' }], observacoes: '' };
const PATCH = { tipo_mudanca: 'major', motivo: 'teste automatizado', autor: 'agente:app', fontes: ['pb-almoxarifado'], campos: { 'identificacao.responsavel': 'Chefe da Divisão de Almoxarifado', 'identificacao.periodicidade': 'Contínua', 'playbook.gatilho': { evento: 'Demanda recebida', origem: 'Requisitante' } }, passos_adicionados: [{ apos_n: 0, passo: { acao: 'Registrar no GMS', responsavel: 'Agente Universitário', sistema: 'GMS' } }, { apos_n: 0, passo: { acao: 'Conferir documentos', responsavel: 'Agente Universitário' } }, { apos_n: 0, passo: { acao: 'Receber a demanda', responsavel: 'Agente Universitário' } }], entrada_nova: ['Requisição'], saida_nova: ['Registro no GMS'], mapa_contexto_novo: [{ origem: 'Div. de Almoxarifado', destino: 'PRAF', relacao: 'informa', artefato: 'Relatório', canal: 'e-Protocolo' }], bpmn_delta: { regenerar_de_passos: true }, licoes_propostas: [{ licao: 'L teste patch', regra: 'R teste patch', origem: 'pop' }] };
const ENTRY = { titulo: 'Entrada de teste', resumo: 'Resumo', responsavel: 'Chefe da Divisão', entrada: 'Insumo', processamento: 'Etapas', saida: 'Entregável', procedimento: ['Passo 1', 'Passo 2'], atencoes: ['Atenção'], kpi: '', contingencia: '', normativa: 'Nao especificada', class: 'PROCESSO' };
function mockFor(body) { const txt = JSON.stringify(body.messages || ''); let payload = ENTRY; if (/diagn[oó]stico de processos/i.test(txt)) payload = DIAG; else if (/PATCH incremental/i.test(txt)) payload = PATCH; return { content: [{ type: 'text', text: JSON.stringify(payload) }], stop_reason: 'end_turn', usage: { input_tokens: 10, output_tokens: 10 } }; }
(async () => {
  const server = spawn('python3', ['-m', 'http.server', String(PORT), '--bind', '127.0.0.1'], { cwd: ROOT, stdio: 'ignore' });
  await sleep(1200);
  const browser = await chromium.launch();
  try {
    const ctx = await browser.newContext({ acceptDownloads: true, viewport: { width: 1280, height: 900 } });
    const page = await ctx.newPage();
    const errors = []; globalErrors = errors; page.on('pageerror', e => errors.push('pageerror: ' + e.message)); page.on('console', m => { if (m.type() === 'error' && !/Failed to load resource/.test(m.text())) errors.push('console: ' + m.text()); }); page.on('requestfailed', r => { if (/127\.0\.0\.1/.test(r.url())) errors.push('requestfailed: ' + r.url()); });
    page.on('dialog', async d => { if (d.type() === 'prompt') await d.accept('Novo formulário de teste'); else await d.accept(); });
    const dataJson = fs.readFileSync(path.join(ROOT, 'data.json'), 'utf8');
    await page.route('**/jessefers.github.io/canvas-vivo-atdg/data.json*', r => r.fulfill({ status: 200, contentType: 'application/json', body: dataJson }));
    await page.route('**/api.anthropic.com/**', r => { const body = JSON.parse(r.request().postData() || '{}'); r.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify(mockFor(body)) }); });
    await page.goto(BASE + 'index.html'); await sleep(1500);
    ok('carregamento sem erros', errors.length === 0, errors.join(' | '));
    const popsCount = await page.evaluate(() => JSON.parse(localStorage.getItem('cv-atdg-pops-v1') || '[]').length);
    ok('data.json sincronizado (pops no localStorage)', popsCount >= 70, 'pops=' + popsCount);
    const tabs = ['entrada', 'canvas', 'buscar', 'manuais', 'agentes', 'hist', 'config'];
    for (const t of tabs) { const before = errors.length; await page.click(`button.tb[onclick*="sw('${t}'"]`); await sleep(400); ok('aba ' + t + ' sem erros', errors.length === before, errors.slice(before).join(' | ')); }
    await page.click(`button.tb[onclick*="sw('canvas'"]`); await sleep(300);
    ok('Canvas renderiza setores', (await page.locator('#canvasContent .secc').count()) > 5);
    ok('Canvas mostra botão BPMN em setor com entradas', (await page.locator('#canvasContent .manual-actions').count()) > 0);
    await page.click(`button.tb[onclick*="sw('manuais'"]`); await sleep(300);
    ok('Manuais preenche grid', (await page.locator('#manuaisGrid .man-card').count()) > 0);
    // Config
    await page.click(`button.tb[onclick*="sw('config'"]`); await sleep(300);
    await page.fill('#apiKeyInput', 'sk-ant-teste-0000'); await page.click('button:has-text("Salvar")'); await sleep(200);
    ok('Config salva chave', (await page.textContent('#apiKeyStatus')).includes('Chave configurada'));
    ok('Config seletor de modelo populado', (await page.locator('#cfgModel option').count()) >= 3);
    const dl1 = page.waitForEvent('download', { timeout: 8000 }).catch(() => null); await page.click('button:has-text("Exportar JSON")'); const d1 = await dl1; ok('Exportar JSON dispara download', !!d1 && /canvas-vivo-atdg-export/.test(d1.suggestedFilename()), d1 && d1.suggestedFilename());
    // Nova entrada com campos estruturados
    await page.click(`button.tb[onclick*="sw('entrada'"]`); await sleep(200);
    await page.fill('#uname', 'Teste QA'); await page.selectOption('#inSetor', 'Div. de Almoxarifado'); await page.selectOption('#inTipo', 'processo');
    await page.fill('#inDesc', 'Descrição de teste com contexto suficiente para o processamento automático da entrada.'); await page.fill('#inResponsavel', 'Chefe da Divisão'); await page.evaluate(() => { document.getElementById('proc-detail').classList.remove('closed'); }); await page.fill('#inEntrada', 'Insumo X'); await page.fill('#inKPI', 'Prazo médio');
    await page.click('#sbtn'); await sleep(1500);
    const last = await page.evaluate(() => { const a = JSON.parse(localStorage.getItem('cv-atdg-entries-v3') || '[]'); return a[a.length - 1]; });
    ok('Nova entrada persiste responsavel/estrutura', last && last.responsavel === 'Chefe da Divisão' && last.estrutura && last.estrutura.entrada === 'Insumo X' && last.estrutura.kpi === 'Prazo médio', JSON.stringify(last && { r: last.responsavel, e: last.estrutura }));
    ok('Nova entrada processada pela IA (mock)', last && last.p && last.p._source === 'ai');
    // Agentes
    const before2 = errors.length; await page.click(`button.tb[onclick*="sw('agentes'"]`); await sleep(500);
    ok('Aba Agentes renderiza resumo', (await page.locator('#agSummary .man-stat').count()) === 4);
    await page.click('#agTabs button[data-sub="pops"]'); await sleep(300);
    ok('Sub-aba POPs lista cards', (await page.locator('#agContent .man-card').count()) >= 70);
    await page.evaluate(() => verPop('ALM-01')); await sleep(200);
    ok('Modal do POP abre', await page.locator('#popModal.on').count() === 1);
    await page.waitForSelector('#popModalBody .mmd svg', { timeout: 20000 }).catch(() => {});
    const svgs = await page.locator('#popModalBody .mmd svg').count();
    ok('Mermaid renderiza organograma e fluxograma (vendor)', svgs >= 2, 'svgs=' + svgs);
    await step('Download Markdown', async () => { const dlMd = page.waitForEvent('download', { timeout: 8000 }).catch(() => null); await page.click('#popModalFooter button:has-text("Markdown")'); const dm = await dlMd; ok('Download Markdown do POP', !!dm && /ALM-01\.md$/.test(dm.suggestedFilename())); });
    await step('Download JSON', async () => { const dlJson = page.waitForEvent('download', { timeout: 8000 }).catch(() => null); await page.click('#popModalFooter button:has-text("JSON")'); const dj = await dlJson; ok('Download JSON do POP', !!dj && /ALM-01\.pop\.json$/.test(dj.suggestedFilename())); });
    await step('Download Word', async () => { const dlWord = page.waitForEvent('download', { timeout: 30000 }).catch(() => null); await page.click('#popModalFooter button:has-text("Word")'); const dw = await dlWord; ok('Download Word do POP', !!dw && /POP_ALM-01.*\.doc$/.test(dw.suggestedFilename()), dw && dw.suggestedFilename()); if (!dw) return; const wordHtml = fs.readFileSync(await dw.path(), 'utf8'); ok('Word contém fluxograma PNG embutido', /data:image\/png;base64,/.test(wordHtml)); });
    await step('Moldar agente', async () => { const dlAg = page.waitForEvent('download', { timeout: 8000 }).catch(() => null); await page.click('#popModalFooter button:has-text("Moldar agente")'); const da = await dlAg; if (!da) { const btns = await page.locator('#popModalFooter button').allTextContents(); ok('Moldar agente baixa pop-alm-01.md', false, 'sem download; botões: ' + btns.join(',') + ' | erros: ' + errors.slice(-3).join(' | ')); return; } ok('Moldar agente baixa pop-alm-01.md', da.suggestedFilename() === 'pop-alm-01.md'); const agMd = fs.readFileSync(await da.path(), 'utf8'); ok('Agente sem placeholders', !/\{\{[a-z_]+\}\}/.test(agMd) && /name: pop-alm-01/.test(agMd)); });
    await step('Miro', async () => { await page.click('#popModalFooter button:has-text("BPMN Miro")'); await sleep(300); ok('Miro abre modal BPMN', await page.locator('#bpmnModal.on').count() === 1); });
    await page.evaluate(() => { fecharBPMNModal(); fecharPopModal(); });
    // Diagnóstico (mock) → gerar POP (mock patch)
    await page.click('#agTabs button[data-sub="diag"]'); await sleep(300);
    await page.selectOption('#agSetorSel', 'S03.04-ALM'); await page.click('#agContent button:has-text("Diagnosticar")'); await sleep(1500);
    ok('Diagnóstico gravado', await page.evaluate(() => { const ds = JSON.parse(localStorage.getItem('cv-atdg-diag-v1') || '[]').filter(d => d.setor_codigo === 'S03.04-ALM'); return ds.length === 1 && (ds[0].processos || []).some(p => p.codigo_sugerido === 'ALM-09'); }));
    ok('Diagnóstico lista processo com prioridade', (await page.locator('#agContent table.pop-table tbody tr').count()) >= 1);
    ok('Lição proposta registrada', (await page.evaluate(() => JSON.parse(localStorage.getItem('cv-atdg-licoes-v1') || '[]').filter(l => l.status === 'proposta').length)) >= 1);
    await page.click('#agContent button:has-text("Gerar POP")'); await sleep(2500);
    const novo = await page.evaluate(() => JSON.parse(localStorage.getItem('cv-atdg-pops-v1') || '[]').find(p => p.codigo === 'ALM-09'));
    ok('Gerar POP cria ALM-09 e aplica patch (v1.0.0, 3 passos, em_validacao)', !!novo && novo.versao === '1.0.0' && novo.playbook.passos.length === 3 && novo.status === 'em_validacao', novo && (novo.versao + '/' + novo.playbook.passos.length + '/' + novo.status));
    ok('POP novo tem fluxograma com captura (mapa de contexto)', !!novo && novo.bpmn_spec.elementos.some(e => e.tipo === 'captura'));
    await page.evaluate(() => fecharPopModal());
    // Atualização incremental com insumo (prompt aceito pelo handler)
    await page.evaluate(() => atualizarPopIncremental('ALM-09')); await sleep(2500);
    const v2 = await page.evaluate(() => JSON.parse(localStorage.getItem('cv-atdg-pops-v1') || '[]').find(p => p.codigo === 'ALM-09'));
    ok('Atualizar incremental gera nova versão com changelog', !!v2 && v2.versao !== '1.0.0' && v2.changelog.length === 3, v2 && v2.versao);
    await page.evaluate(() => fecharPopModal());
    // Diretrizes/lições
    await page.click('#agTabs button[data-sub="diretrizes"]'); await sleep(300);
    ok('Painel de diretrizes lista diretrizes sincronizadas', (await page.locator('#agContent details.fc').count()) >= 9);
    await page.click('#agContent button:has-text("Aprovar")'); await sleep(200);
    ok('Aprovar lição muda status', (await page.evaluate(() => JSON.parse(localStorage.getItem('cv-atdg-licoes-v1') || '[]').filter(l => l.status === 'aprovada').length)) >= 8);
    ok('Aba Agentes sem erros de página', errors.length === before2, errors.slice(before2).join(' | '));
    // Fallback sem Mermaid
    const ctx2 = await browser.newContext(); const p2 = await ctx2.newPage(); const err2 = []; p2.on('pageerror', e => err2.push(e.message));
    await p2.route('**/jessefers.github.io/canvas-vivo-atdg/data.json*', r => r.fulfill({ status: 200, contentType: 'application/json', body: dataJson }));
    await p2.route('**/vendor/mermaid.min.js', r => r.abort());
    await p2.goto(BASE + 'index.html'); await sleep(1200); await p2.click(`button.tb[onclick*="sw('agentes'"]`); await sleep(300);
    await p2.evaluate(() => verPop('DCOM-01')); await sleep(1500);
    ok('Fallback HTML sem Mermaid', (await p2.locator('#popModalBody .mmd .bpmn-flow').count()) >= 1 && err2.length === 0, err2.join(' | '));
    await ctx2.close();
  } finally { await browser.close(); server.kill(); }
  console.log(results.join('\n')); if (typeof globalErrors !== 'undefined' && globalErrors.length) console.log('ERROS DE PÁGINA:\n' + globalErrors.join('\n')); console.log('\n' + (results.length - failures) + '/' + results.length + ' verificações OK'); process.exit(failures ? 1 : 0);
})().catch(e => { console.error('ERRO FATAL', e); process.exit(2); });
