# 📁 Archivos Generados en la Carpeta `outputs/`

Esta carpeta contendrá todos los archivos generados por el script `visualizacion_hoteles.py`.

## 🎨 Visualizaciones Estáticas (PNG)

### 1. `01_lineas_temporales_ingresos_hoteles.png`
- **Tipo**: Gráfico de líneas temporales
- **Descripción**: Evolución de ingresos por complejo (1993-1995)
- **Características**: 
  - Líneas con marcadores para cada complejo
  - Etiquetas de valor en cada punto
  - Métricas de cambio porcentual
  - Paleta colorblind-friendly
  - Resolución: 300 DPI

### 2. `02_slopegraph_1993_vs_1995.png`
- **Tipo**: Slopegraph comparativo
- **Descripción**: Comparación directa entre 1993 y 1995
- **Características**:
  - Líneas de conexión entre años
  - Etiquetas de valor para cada año
  - Cambios porcentuales destacados
  - Ordenamiento por rendimiento
  - Resolución: 300 DPI

## 🌐 Visualización Interactiva (HTML)

### 3. `03_dashboard_interactivo_hoteles.html`
- **Tipo**: Dashboard interactivo con Plotly
- **Descripción**: 4 visualizaciones en un solo dashboard
- **Características**:
  - Gráfico de líneas temporal
  - Comparación de barras 1993 vs 1995
  - Variación interanual (YoY)
  - Índice base 1993=100
  - Tooltips interactivos
  - Exportable a HTML

## 📊 Datos y Métricas (CSV)

### 4. `metricas_evolucion_hoteles.csv`
- **Contenido**: Dataset original + métricas calculadas
- **Métricas incluidas**:
  - Variación interanual (YoY %)
  - Cambio absoluto (USD)
  - Índice base 1993=100
  - Cambio total 1993-1995
  - Cambio total porcentual

### 5. `resumen_ejecutivo_hoteles.csv`
- **Contenido**: Resumen agregado por complejo
- **Columnas**:
  - Ingreso_1993: Ingresos del año inicial
  - Ingreso_1995: Ingresos del año final
  - Cambio_Total_%: Cambio porcentual total
  - YoY_Promedio_%: Promedio de variación interanual
  - YoY_DesvEst_%: Desviación estándar de YoY

## 🔄 Flujo de Generación

1. **Ejecutar script**: `python src/visualizacion_hoteles.py`
2. **Verificación**: El script verifica librerías y entorno
3. **Procesamiento**: Carga datos y calcula métricas
4. **Generación**: Crea visualizaciones estáticas e interactivas
5. **Exportación**: Guarda archivos en esta carpeta
6. **Verificación**: Confirma que todos los archivos se crearon

## 📋 Notas Importantes

- **Resolución**: Todas las imágenes PNG se generan a 300 DPI
- **Formato**: Los archivos CSV usan codificación UTF-8
- **Compatibilidad**: El HTML funciona en cualquier navegador moderno
- **Tamaño**: Los archivos se optimizan para web y presentaciones

---

**💡 Tip**: Abre el archivo HTML en tu navegador para explorar las visualizaciones interactivas.
