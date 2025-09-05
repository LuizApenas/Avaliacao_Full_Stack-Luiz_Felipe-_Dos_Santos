import type { UrlItem } from "../types";

// Função para buscar todas as URLs cadastradas no backend
export async function fetchUrls(): Promise<UrlItem[]> {
    const resposta = await fetch("/api/urls");
    if (!resposta.ok) throw new Error("Falha ao buscar URLs do servidor");
    return resposta.json();
}

// Tipo que define a estrutura das métricas de acesso
export type MetricItem = {
    short_id: string;      // Identificador único da URL encurtada
    last_hour: number;     // Número de acessos na última hora
    last_day: number;      // Número de acessos no último dia
    last_month: number;    // Número de acessos no último mês
}

// Função para buscar métricas de acesso do backend
export async function fetchMetrics(): Promise<MetricItem[]> {
    const resposta = await fetch("/api/metrics");
    if (!resposta.ok) throw new Error("Falha ao buscar métricas do servidor");
    return resposta.json();
}

// Função para registrar uma métrica quando o usuário clica no botão "Abrir"
export async function recordMetric(shortId: string): Promise<string> {
    const resposta = await fetch(`/api/metrics/${shortId}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        }
    });
    
    if (!resposta.ok) {
        throw new Error("Falha ao registrar métrica");
    }
    
    const dados = await resposta.json();
    return dados.original_url;
}