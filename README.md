# 📊 Visualización de Evolución Temporal de Ingresos Hoteleros (1993-1995)

Análisis completo de la evolución temporal de ingresos de tres complejos hoteleros con visualizaciones estáticas e interactivas.

## 🚀 Ejecución Rápida

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Ejecutar análisis
```bash
python src/visualizacion_hoteles.py
```

## 📁 Estructura del Proyecto

```
Act1/
├── data/
│   └── ingresos_hoteles_1993_1995.csv    # Dataset principal
├── src/
│   └── visualizacion_hoteles.py          # Script de análisis
├── outputs/                               # Archivos generados
├── requirements.txt                       # Dependencias
└── README.md
```

## 🎨 Visualizaciones Generadas

- **Gráfico de Líneas Temporales**: Evolución de ingresos por complejo (1993-1995)
- **Slopegraph**: Comparación directa 1993 vs 1995 con cambios porcentuales
- **Dashboard Interactivo**: Análisis completo con Plotly (4 subplots)
- **Métricas Calculadas**: YoY, índices base, cambios totales y resumen ejecutivo

## 📊 Análisis Incluido

- Evolución temporal de ingresos por complejo
- Variación interanual (YoY) y cambios absolutos
- Índice base 1993=100 para comparación relativa
- Análisis ejecutivo con recomendaciones estratégicas

## ⚠️ Requisitos

- Python ≥ 3.9
- pip

## 🔧 Solución de Problemas

Si falta alguna librería:
```bash
pip install pandas numpy matplotlib seaborn plotly
```

---

💡 El script verifica automáticamente las librerías y te informa si falta alguna.
