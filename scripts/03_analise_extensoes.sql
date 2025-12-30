-- Análise das extensões mais comuns no filesystem

SELECT
    regexp_extract(full_path, '(\\.[^\\.\\\\]+)$') AS extensao,
    COUNT(*) AS quantidade
FROM files
WHERE full_path LIKE '%.%'
GROUP BY extensao
ORDER BY quantidade DESC
LIMIT 20;
