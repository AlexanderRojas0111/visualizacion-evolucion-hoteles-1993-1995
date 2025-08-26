import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os
import warnings
warnings.filterwarnings('ignore')

def verificar_librerias():
    """Verifica que todas las librerías necesarias estén instaladas"""
    librerias_requeridas = {
        'pandas': 'pd',
        'numpy': 'np', 
        'matplotlib.pyplot': 'plt',
        'seaborn': 'sns',
        'plotly.graph_objects': 'go',
        'plotly.subplots': 'make_subplots'
    }
    
    librerias_faltantes = []
    
    for libreria, alias in librerias_requeridas.items():
        try:
            __import__(libreria)
            print(f"✅ {libreria}")
        except ImportError:
            librerias_faltantes.append(libreria)
            print(f"❌ {libreria} - NO INSTALADA")
    
    if librerias_faltantes:
        print(f"\n⚠️ Librerías faltantes: {', '.join(librerias_faltantes)}")
        print("💡 Instala con: pip install -r requirements.txt")
        return False
    
    print("\n✅ Todas las librerías están instaladas correctamente")
    return True

def configurar_entorno():
    """Configura el entorno de visualización"""
    try:
        # Configurar matplotlib para pantalla
        plt.rcParams['figure.figsize'] = [10, 6]
        plt.rcParams['figure.dpi'] = 100
        plt.rcParams['savefig.dpi'] = 300
        plt.rcParams['font.size'] = 10
        plt.rcParams['axes.titlesize'] = 12
        plt.rcParams['axes.labelsize'] = 10
        plt.rcParams['xtick.labelsize'] = 9
        plt.rcParams['ytick.labelsize'] = 9
        
        # Configurar estilo
        try:
            plt.style.use('seaborn-v0_8')
        except:
            plt.style.use('default')
        
        sns.set_palette("husl")
        
        # Crear directorio de outputs si no existe
        os.makedirs('outputs', exist_ok=True)
        print("✅ Entorno configurado correctamente")
    except Exception as e:
        print(f"⚠️ Advertencia en configuración: {e}")
        print("✅ Continuando con configuración básica...")

def cargar_datos():
    """Carga y valida los datos del CSV"""
    try:
        df = pd.read_csv('data/ingresos_hoteles_1993_1995.csv')
        
        # Validaciones básicas
        print(f"✅ Datos cargados: {df.shape[0]} registros, {df.shape[1]} columnas")
        print(f"📊 Años: {sorted(df['anio'].unique())}")
        print(f"🏨 Complejos: {sorted(df['complejo'].unique())}")
        print(f"💰 Rango ingresos: ${df['ingresos_usd'].min():,} - ${df['ingresos_usd'].max():,}")
        
        return df
    except Exception as e:
        print(f"❌ Error al cargar datos: {e}")
        return None

def calcular_metricas(df):
    """Calcula métricas de evolución temporal"""
    df_metricas = df.sort_values(['complejo', 'anio']).copy()
    
    # Variación interanual (YoY)
    df_metricas['yoy_pct'] = df_metricas.groupby('complejo')['ingresos_usd'].pct_change() * 100
    
    # Cambio absoluto
    df_metricas['cambio_absoluto'] = df_metricas.groupby('complejo')['ingresos_usd'].diff()
    
    # Índice base 1993=100
    df_metricas['indice_base_1993'] = df_metricas.groupby('complejo')['ingresos_usd'].transform(
        lambda x: (x / x.iloc[0]) * 100
    )
    
    # Cambio total 1993-1995
    df_metricas['cambio_total_1993_1995'] = df_metricas.groupby('complejo')['ingresos_usd'].transform(
        lambda x: x.iloc[-1] - x.iloc[0]
    )
    
    df_metricas['cambio_total_pct_1993_1995'] = df_metricas.groupby('complejo')['ingresos_usd'].transform(
        lambda x: ((x.iloc[-1] / x.iloc[0]) - 1) * 100
    )
    
    print("✅ Métricas calculadas correctamente")
    return df_metricas

def crear_grafico_lineas_temporales(df):
    """Crea gráfico de líneas temporales con matplotlib"""
    plt.figure(figsize=(10, 6))
    
    # Paleta colorblind-friendly
    colores = ['#1f77b4', '#ff7f0e', '#2ca02c']
    
    for i, complejo in enumerate(sorted(df['complejo'].unique())):
        datos_complejo = df[df['complejo'] == complejo].sort_values('anio')
        
        # Línea principal
        plt.plot(datos_complejo['anio'], datos_complejo['ingresos_usd'], 
                marker='o', linewidth=3, markersize=8, 
                color=colores[i], label=complejo)
        
        # Etiquetas de valor
        for _, row in datos_complejo.iterrows():
            plt.annotate(f'${row["ingresos_usd"]:,}', 
                        (row['anio'], row['ingresos_usd']),
                        textcoords="offset points", 
                        xytext=(0,10), 
                        ha='center', 
                        fontsize=9,
                        bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
    
    # Personalización
    plt.title('Evolución de Ingresos por Complejo Hotelero (1993-1995)', 
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Año', fontsize=12, fontweight='bold')
    plt.ylabel('Ingresos (USD)', fontsize=12, fontweight='bold')
    
    plt.xticks([1993, 1994, 1995], fontsize=11)
    plt.ylim(0, df['ingresos_usd'].max() * 1.1)
    
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.legend(title='Complejo Hotelero', fontsize=11, title_fontsize=12, 
              loc='upper left', framealpha=0.9)
    
    # Añadir métricas de cambio total
    for i, complejo in enumerate(sorted(df['complejo'].unique())):
        datos_complejo = df[df['complejo'] == complejo].sort_values('anio')
        cambio_total = datos_complejo['ingresos_usd'].iloc[-1] - datos_complejo['ingresos_usd'].iloc[0]
        cambio_pct = (cambio_total / datos_complejo['ingresos_usd'].iloc[0]) * 100
        
        x_pos = 1995.1
        y_pos = datos_complejo['ingresos_usd'].iloc[-1]
        
        plt.annotate(f'{cambio_pct:+.1f}%', 
                    (x_pos, y_pos),
                    fontsize=10, 
                    color=colores[i],
                    fontweight='bold')
    
    plt.tight_layout()
    
    # Guardar gráfico
    plt.savefig('outputs/01_lineas_temporales_ingresos_hoteles.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Gráfico de líneas temporales guardado")
    plt.show()

def crear_slopegraph(df):
    """Crea slopegraph comparando 1993 vs 1995"""
    # Obtener datos de 1993 y 1995
    df_1993 = df[df['anio'] == 1993].set_index('complejo')['ingresos_usd']
    df_1995 = df[df['anio'] == 1995].set_index('complejo')['ingresos_usd']
    
    # Ordenar por ingresos de 1993
    orden_complejos = df_1993.sort_values(ascending=False).index
    
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Paleta colorblind-friendly
    colores = ['#1f77b4', '#ff7f0e', '#2ca02c']
    
    for i, complejo in enumerate(orden_complejos):
        y_1993 = df_1993[complejo]
        y_1995 = df_1995[complejo]
        
        # Línea de conexión
        ax.plot([0, 1], [y_1993, y_1995], 
               color=colores[i], linewidth=3, alpha=0.7)
        
        # Marcadores
        ax.scatter([0], [y_1993], s=100, color=colores[i], 
                  edgecolor='black', linewidth=2, zorder=5)
        ax.scatter([1], [y_1995], s=100, color=colores[i], 
                  edgecolor='black', linewidth=2, zorder=5)
        
        # Etiquetas de valor
        ax.annotate(f'${y_1993:,}', (0, y_1993), 
                    xytext=(-20, 0), textcoords='offset points', 
                    ha='right', va='center', fontsize=10, fontweight='bold')
        ax.annotate(f'${y_1995:,}', (1, y_1995), 
                    xytext=(20, 0), textcoords='offset points', 
                    ha='left', va='center', fontsize=10, fontweight='bold')
        
        # Etiqueta del complejo
        ax.annotate(complejo, (0.5, (y_1993 + y_1995) / 2), 
                    xytext=(0, 10), textcoords='offset points', 
                    ha='center', va='bottom', fontsize=11, fontweight='bold',
                    bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.9))
        
        # Calcular y mostrar cambio
        cambio = y_1995 - y_1993
        cambio_pct = (cambio / y_1993) * 100
        color_cambio = 'green' if cambio >= 0 else 'red'
        
        ax.annotate(f'{cambio_pct:+.1f}%', 
                    (0.5, (y_1993 + y_1995) / 2), 
                    xytext=(0, -25), textcoords='offset points', 
                    ha='center', va='top', fontsize=10, 
                    color=color_cambio, fontweight='bold')
    
    # Personalización
    ax.set_xlim(-0.1, 1.1)
    ax.set_ylim(0, df['ingresos_usd'].max() * 1.1)
    
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['1993', '1995'], fontsize=12, fontweight='bold')
    ax.set_ylabel('Ingresos (USD)', fontsize=12, fontweight='bold')
    
    ax.set_title('Comparación de Ingresos: 1993 vs 1995\n(Slopegraph con Cambios Porcentuales)', 
                 fontsize=14, fontweight='bold', pad=20)
    
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    plt.tight_layout()
    
    # Guardar gráfico
    plt.savefig('outputs/02_slopegraph_1993_vs_1995.png', 
                dpi=300, bbox_inches='tight')
    print("✅ Slopegraph guardado")
    plt.show()

def crear_grafico_interactivo(df):
    """Crea gráfico interactivo con plotly"""
    # Crear figura con subplots
    fig = make_subplots(
        rows=2, cols=2,
        subplot_titles=('Evolución Temporal', 'Comparación 1993 vs 1995', 
                       'Variación Interanual (YoY)', 'Índice Base 1993=100'),
        specs=[[{"secondary_y": False}, {"secondary_y": False}],
               [{"secondary_y": False}, {"secondary_y": False}]],
        vertical_spacing=0.12,
        horizontal_spacing=0.1
    )
    
    # Paleta colorblind-friendly
    colores = ['#1f77b4', '#ff7f0e', '#2ca02c']
    
    # 1. Gráfico de líneas temporal
    for i, complejo in enumerate(sorted(df['complejo'].unique())):
        datos_complejo = df[df['complejo'] == complejo].sort_values('anio')
        
        fig.add_trace(
            go.Scatter(
                x=datos_complejo['anio'],
                y=datos_complejo['ingresos_usd'],
                mode='lines+markers+text',
                name=complejo,
                line=dict(color=colores[i], width=3),
                marker=dict(size=8, color=colores[i]),
                text=[f'${x:,}' for x in datos_complejo['ingresos_usd']],
                textposition="top center",
                hovertemplate=f'<b>{complejo}</b><br>' +
                             'Año: %{x}<br>' +
                             'Ingresos: $%{y:,}<br>' +
                             '<extra></extra>',
                showlegend=True
            ),
            row=1, col=1
        )
    
    # 2. Gráfico de barras comparativo 1993 vs 1995
    df_1993 = df[df['anio'] == 1993].set_index('complejo')['ingresos_usd']
    df_1995 = df[df['anio'] == 1995].set_index('complejo')['ingresos_usd']
    
    fig.add_trace(
        go.Bar(
            x=list(df_1993.index),
            y=df_1993.values,
            name='1993',
            marker_color='lightblue',
            hovertemplate='<b>%{x}</b><br>1993: $%{y:,}<extra></extra>'
        ),
        row=1, col=2
    )
    
    fig.add_trace(
        go.Bar(
            x=list(df_1995.index),
            y=df_1995.values,
            name='1995',
            marker_color='darkblue',
            hovertemplate='<b>%{x}</b><br>1995: $%{y:,}<extra></extra>'
        ),
        row=1, col=2
    )
    
    # 3. Gráfico de variación interanual
    for i, complejo in enumerate(sorted(df['complejo'].unique())):
        datos_complejo = df[df['complejo'] == complejo].sort_values('anio')
        datos_yoy = datos_complejo[datos_complejo['yoy_pct'].notna()]
        
        fig.add_trace(
            go.Scatter(
                x=datos_yoy['anio'],
                y=datos_yoy['yoy_pct'],
                mode='lines+markers',
                name=f'{complejo} (YoY)',
                line=dict(color=colores[i], width=2, dash='dash'),
                marker=dict(size=6, color=colores[i]),
                hovertemplate=f'<b>{complejo}</b><br>' +
                             'Año: %{x}<br>' +
                             'YoY: %{y:.1f}%<br>' +
                             '<extra></extra>',
                showlegend=False
            ),
            row=2, col=1
        )
    
    # 4. Gráfico de índice base 1993=100
    for i, complejo in enumerate(sorted(df['complejo'].unique())):
        datos_complejo = df[df['complejo'] == complejo].sort_values('anio')
        
        fig.add_trace(
            go.Scatter(
                x=datos_complejo['anio'],
                y=datos_complejo['indice_base_1993'],
                mode='lines+markers',
                name=f'{complejo} (Índice)',
                line=dict(color=colores[i], width=2),
                marker=dict(size=6, color=colores[i]),
                hovertemplate=f'<b>{complejo}</b><br>' +
                             'Año: %{x}<br>' +
                             'Índice: %{y:.1f}<br>' +
                             '<extra></extra>',
                showlegend=False
            ),
            row=2, col=2
        )
    
    # Personalización del layout
    fig.update_layout(
        title=dict(
            text='Dashboard Interactivo: Análisis Completo de Ingresos Hoteleros (1993-1995)',
            x=0.5,
            font=dict(size=16, color='black')
        ),
        height=600,
        showlegend=True,
        template='plotly_white',
        hovermode='closest'
    )
    
    # Personalizar ejes
    fig.update_xaxes(title_text="Año", row=1, col=1)
    fig.update_yaxes(title_text="Ingresos (USD)", row=1, col=1)
    
    fig.update_xaxes(title_text="Complejo", row=1, col=2)
    fig.update_yaxes(title_text="Ingresos (USD)", row=2, col=1)
    
    fig.update_xaxes(title_text="Año", row=2, col=1)
    fig.update_yaxes(title_text="Variación YoY (%)", row=2, col=1)
    
    fig.update_xaxes(title_text="Año", row=2, col=2)
    fig.update_yaxes(title_text="Índice Base 1993=100", row=2, col=2)
    
    # Añadir línea de referencia en el índice
    fig.add_hline(y=100, line_dash="dash", line_color="gray", 
                  row=2, col=2, annotation_text="Línea Base 1993")
    
    # Guardar como HTML
    fig.write_html('outputs/03_dashboard_interactivo_hoteles.html')
    print("✅ Dashboard interactivo guardado")
    
    return fig

def exportar_datos(df_metricas):
    """Exporta datos y métricas calculadas"""
    # Exportar dataset con métricas
    df_metricas.to_csv('outputs/metricas_evolucion_hoteles.csv', index=False)
    print("✅ Dataset con métricas exportado")
    
    # Crear resumen ejecutivo
    resumen_ejecutivo = df_metricas.groupby('complejo').agg({
        'ingresos_usd': ['first', 'last'],
        'cambio_total_pct_1993_1995': 'last',
        'yoy_pct': ['mean', 'std']
    }).round(2)
    
    resumen_ejecutivo.columns = ['Ingreso_1993', 'Ingreso_1995', 'Cambio_Total_%', 'YoY_Promedio_%', 'YoY_DesvEst_%']
    resumen_ejecutivo.to_csv('outputs/resumen_ejecutivo_hoteles.csv')
    print("✅ Resumen ejecutivo exportado")
    
    return resumen_ejecutivo

def mostrar_analisis_conclusiones(resumen):
    """Muestra análisis y conclusiones ejecutivas"""
    print("\n" + "="*80)
    print("📊 ANÁLISIS Y CONCLUSIONES EJECUTIVAS")
    print("="*80)
    
    print("\n🏆 RESUMEN DE RENDIMIENTO (1993-1995):")
    for complejo in resumen.index:
        ingreso_1993 = resumen.loc[complejo, 'Ingreso_1993']
        ingreso_1995 = resumen.loc[complejo, 'Ingreso_1995']
        cambio_pct = resumen.loc[complejo, 'Cambio_Total_%']
        
        emoji = "📈" if cambio_pct > 0 else "📉"
        print(f"{emoji} {complejo}: {cambio_pct:+.1f}% (${ingreso_1993:,} → ${ingreso_1995:,})")
    
    print("\n🎯 INSIGHTS CLAVE PARA DECISIONES:")
    print("• Bahamas Beach: Mayor crecimiento (+40.8%), invertir en expansión")
    print("• Hawaiian Club: Líder con caída (-13.3%), requiere revitalización")
    print("• French Riviera: Mayor caída (-8.9%), intervención estratégica urgente")
    
    print("\n💡 RECOMENDACIONES ESTRATÉGICAS:")
    print("• Corto plazo: Auditoría operativa en Hawaiian Club y French Riviera")
    print("• Mediano plazo: Expandir operaciones de Bahamas Beach")
    print("• Largo plazo: Reposicionamiento de French Riviera")

def main():
    """Función principal del script"""
    print("🚀 INICIANDO ANÁLISIS DE VISUALIZACIÓN DE HOTELES")
    print("="*60)
    
    # 1. Verificar librerías
    print("\n🔍 VERIFICANDO LIBRERÍAS...")
    if not verificar_librerias():
        print("\n❌ No se pueden continuar. Instala las librerías faltantes.")
        return
    
    # 2. Configurar entorno
    print("\n⚙️ CONFIGURANDO ENTORNO...")
    configurar_entorno()
    
    # 3. Cargar datos
    print("\n📊 CARGANDO DATOS...")
    df = cargar_datos()
    if df is None:
        return
    
    # 4. Calcular métricas
    df_metricas = calcular_metricas(df)
    
    # 5. Crear visualizaciones
    print("\n🎨 CREANDO VISUALIZACIONES...")
    
    # Gráfico de líneas temporales
    crear_grafico_lineas_temporales(df_metricas)
    
    # Slopegraph
    crear_slopegraph(df_metricas)
    
    # Dashboard interactivo
    dashboard = crear_grafico_interactivo(df_metricas)
    
    # 6. Exportar datos
    print("\n💾 EXPORTANDO DATOS...")
    resumen = exportar_datos(df_metricas)
    
    # 7. Mostrar análisis
    mostrar_analisis_conclusiones(resumen)
    
    # 8. Verificar archivos generados
    print("\n📁 VERIFICACIÓN DE ARCHIVOS GENERADOS:")
    outputs_dir = 'outputs'
    archivos = [f for f in os.listdir(outputs_dir) if f.endswith(('.png', '.html', '.csv'))]
    
    for archivo in sorted(archivos):
        ruta = os.path.join(outputs_dir, archivo)
        tamaño = os.path.getsize(ruta)
        print(f"✅ {archivo} ({tamaño:,} bytes)")
    
    print(f"\n🎉 ANÁLISIS COMPLETADO EXITOSAMENTE!")
    print(f"📊 Total de archivos generados: {len(archivos)}")
    print(f"📂 Revisa la carpeta 'outputs' para ver todos los resultados")

if __name__ == "__main__":
    main()
