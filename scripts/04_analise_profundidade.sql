-- Análise da profundidade dos caminhos

SELECT
    array_length(string_split(full_path, '\\')) AS profundidade,
    COUNT(*) AS quantidade
FROM files
GROUP BY profundidade
ORDER BY profundidade DESC;
