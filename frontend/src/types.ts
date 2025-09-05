// Tipo que define a estrutura de uma URL encurtada
export type UrlItem = {
    short_id: string;         // Identificador único da URL encurtada
    original_url: string;     // URL original completa
    created_at: string;       // Data de criação no formato ISO
    is_active: boolean;       // Se a URL está ativa ou não
    failed_checks: number;    // Número de falhas de verificação
    last_check?: string | null;    // Data da última verificação
    short_url?: string | null;     // URL encurtada completa
};

// Tipo que define a estrutura das métricas de acesso
export type MetricItem = {
    short_id: string;         // Identificador único da URL encurtada
    last_hour: number;        // Acessos na última hora
    last_day: number;         // Acessos no último dia
    last_month: number;       // Acessos no último mês
};
