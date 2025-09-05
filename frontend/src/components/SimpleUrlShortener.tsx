import { useState, useEffect } from 'react';
import { fetchUrls, fetchMetrics, recordMetric, type UrlItem, type MetricItem } from '../services/urls';

export function SimpleUrlShortener() {
  // Estados da aplicação para controlar dados e interface
  const [url, setUrl] = useState('');
  const [shortenedUrls, setShortenedUrls] = useState<UrlItem[]>([]);
  const [metrics, setMetrics] = useState<MetricItem[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [refreshKey, setRefreshKey] = useState(0);
  const [loadingMetrics, setLoadingMetrics] = useState<Set<string>>(new Set());
  const [searchFilter, setSearchFilter] = useState(''); // Novo estado para filtro de pesquisa

  // Carrega dados das URLs e métricas quando o componente é montado ou quando refreshKey muda
  useEffect(() => {
    const carregarDados = async () => {
      try {
        // Faz duas chamadas paralelas para otimizar o carregamento
        const [dadosUrls, dadosMetricas] = await Promise.all([
          fetchUrls(),    // Busca todas as URLs cadastradas no backend
          fetchMetrics()  // Busca as métricas de acesso do backend
        ]);
        setShortenedUrls(dadosUrls);
        setMetrics(dadosMetricas);
      } catch (error) {
        console.error('Erro ao carregar dados:', error);
        alert('Erro ao carregar dados do servidor');
      }
    };
    carregarDados();
  }, [refreshKey]); // Reexecuta quando refreshKey muda

  // Função para encurtar uma nova URL
  const handleEncurtarUrl = async () => {
    // Validação básica da entrada do usuário
    if (!url.trim()) {
      alert('Por favor, insira uma URL válida');
      return;
    }

    // Verifica se a URL tem protocolo http/https
    if (!url.startsWith('http://') && !url.startsWith('https://')) {
      alert('URL deve começar com http:// ou https://');
      return;
    }

    setIsLoading(true);
    
    try {
      // Faz requisição POST para o backend criar URL encurtada
      const resposta = await fetch("/api/urls", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ original_url: url }),
      });

      const dados = await resposta.json();
      if (!resposta.ok) throw new Error(dados.detail || "Falha ao encurtar URL");

      // Limpa o campo de entrada e recarrega os dados
      setUrl('');
      setRefreshKey(k => k + 1); // Força recarregamento dos dados
      alert('URL encurtada com sucesso!');
    } catch (erro: any) {
      alert(erro.message || "Erro inesperado ao encurtar URL");
    } finally {
      setIsLoading(false);
    }
  };

  // Função para copiar URL encurtada para área de transferência
  const copiarParaAreaTransferencia = (shortUrl: string) => {
    navigator.clipboard.writeText(shortUrl);
    alert('Link copiado para a área de transferência!');
  };

  // Função para abrir URL e registrar métrica automaticamente
  const handleAbrirUrl = async (shortId: string, shortUrl: string) => {
    // Adiciona o shortId ao set de loading
    setLoadingMetrics(prev => new Set(prev).add(shortId));
    
    try {
      // Registra a métrica antes de abrir a URL
      const originalUrl = await recordMetric(shortId);
      
      // Abre a URL original em nova aba
      window.open(originalUrl, '_blank');
      
      // Atualiza as métricas na interface sem recarregar a página
      setTimeout(async () => {
        try {
          const novasMetricas = await fetchMetrics();
          setMetrics(novasMetricas);
        } catch (error) {
          console.error('Erro ao atualizar métricas:', error);
        } finally {
          // Remove o shortId do set de loading
          setLoadingMetrics(prev => {
            const newSet = new Set(prev);
            newSet.delete(shortId);
            return newSet;
          });
        }
      }, 500); // Pequeno delay para garantir que a métrica foi salva
      
    } catch (error) {
      console.error('Erro ao registrar métrica:', error);
      // Remove o shortId do set de loading em caso de erro
      setLoadingMetrics(prev => {
        const newSet = new Set(prev);
        newSet.delete(shortId);
        return newSet;
      });
      // Em caso de erro, ainda abre a URL usando o método tradicional
      window.open(shortUrl, '_blank');
    }
  };

  // Função para formatar data/hora no padrão brasileiro
  const formatarData = (dataString: string) => {
    return new Date(dataString).toLocaleString('pt-BR');
  };

  // Função para filtrar métricas com base na pesquisa
  const metricasFiltradas = metrics.filter(metrica => 
    searchFilter === '' || metrica.short_id.toLowerCase().includes(searchFilter.toLowerCase())
  );

  return (
    <div className="app-container">
      {/* Cabeçalho da aplicação */}
      <header className="header">
        <h1>Encurtador de URL</h1>
        <p>Transforme suas URLs longas em links curtos e rastreáveis</p>
      </header>

      {/* Layout principal com duas colunas */}
      <div className="main-layout">
        {/* Seção do formulário (lado esquerdo) */}
        <section className="form-section">
          <h2>Encurtar Nova URL</h2>
          <div className="input-group">
            <label htmlFor="url-input">Cole sua URL aqui:</label>
            <textarea
              id="url-input"
              className="url-input"
              placeholder="https://exemplo.com/sua-url-muito-longa-aqui..."
              value={url}
              onChange={(e) => setUrl(e.target.value)}
              rows={4}
            />
          </div>
          
          <button 
            className="btn-primary"
            onClick={handleEncurtarUrl} 
            disabled={isLoading}
          >
            {isLoading ? 'Encurtando...' : 'Encurtar URL'}
          </button>
        </section>

        {/* Seção da lista de URLs (lado direito) */}
        <section className="urls-section">
          <h2>URLs Cadastradas</h2>
          {shortenedUrls.length === 0 ? (
            <div className="empty-state">
              <p>Nenhuma URL cadastrada ainda</p>
            </div>
          ) : (
            <div>
              {shortenedUrls.map((item) => (
                <div key={item.short_id} className="url-card">
                  {/* Cabeçalho do card com ID e ações */}
                  <div className="url-header">
                    <span className="short-id">{item.short_id}</span>
                    <div className="url-actions">
                      {item.short_url && (
                        <>
                          <button 
                            className="btn-small btn-copy"
                            onClick={() => copiarParaAreaTransferencia(item.short_url!)}
                            title="Copiar link"
                          >
                            Copiar
                          </button>
                          <button 
                            className="btn-small btn-open"
                            onClick={() => handleAbrirUrl(item.short_id, item.short_url!)}
                            title="Abrir link e registrar métrica"
                            disabled={loadingMetrics.has(item.short_id)}
                          >
                            {loadingMetrics.has(item.short_id) ? 'Abrindo...' : 'Abrir'}
                          </button>
                        </>
                      )}
                      <span className={`status-badge ${item.is_active ? 'status-active' : 'status-inactive'}`}>
                        {item.is_active ? 'Ativo' : 'Inativo'}
                      </span>
                    </div>
                  </div>
                  
                  {/* URL original */}
                  <div className="original-url">
                    {item.original_url}
                  </div>
                  
                  {/* Informações adicionais */}
                  <div className="url-info">
                    <span>Criada em: {formatarData(item.created_at)}</span>
                  </div>
                </div>
              ))}
            </div>
          )}
        </section>
      </div>

      {/* Seção de métricas (embaixo) */}
      <section className="metrics-section">
        <h2>Métricas de Acesso</h2>
        
        {/* Campo de pesquisa */}
        <div className="search-group">
          <label htmlFor="search-input">Pesquisar por Short ID:</label>
          <input
            id="search-input"
            type="text"
            className="search-input"
            placeholder="Digite o Short ID para filtrar..."
            value={searchFilter}
            onChange={(e) => setSearchFilter(e.target.value)}
          />
        </div>

        {metricasFiltradas.length === 0 ? (
          <div className="empty-state">
            <p>
              {searchFilter 
                ? `Nenhuma métrica encontrada para "${searchFilter}"` 
                : 'Nenhuma métrica disponível ainda'
              }
            </p>
          </div>
        ) : (
          <table className="metrics-table">
            <thead>
              <tr>
                <th>Short ID</th>
                <th>Última hora</th>
                <th>Último dia</th>
                <th>Último mês</th>
              </tr>
            </thead>
            <tbody>
              {metricasFiltradas.map((metrica) => (
                <tr key={metrica.short_id}>
                  <td>
                    <span className="short-id">{metrica.short_id}</span>
                  </td>
                  <td className="metric-value">{metrica.last_hour}</td>
                  <td className="metric-value">{metrica.last_day}</td>
                  <td className="metric-value">{metrica.last_month}</td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </section>
    </div>
  );
}
