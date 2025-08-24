# 🚀 Instrucciones para Subir a GitHub

## 📋 Pasos para Publicar el Repositorio

### 1. **Crear Repositorio en GitHub**
- Ve a [github.com](https://github.com)
- Haz clic en "New repository"
- Nombre: `visualizacion-evolucion-hoteles-1993-1995`
- Descripción: `Análisis completo de evolución temporal de ingresos hoteleros con visualizaciones estáticas e interactivas`
- Público o Privado (según prefieras)
- **NO** inicialices con README, .gitignore o LICENSE (ya los tenemos)

### 2. **Conectar Repositorio Local con GitHub**
```bash
# Agregar el repositorio remoto (reemplaza TU_USUARIO con tu nombre de usuario)
git remote add origin https://github.com/TU_USUARIO/visualizacion-evolucion-hoteles-1993-1995.git

# Verificar que se agregó correctamente
git remote -v
```

### 3. **Subir Código a GitHub**
```bash
# Subir la rama principal
git branch -M main
git push -u origin main
```

### 4. **Verificar en GitHub**
- Ve a tu repositorio en GitHub
- Verifica que todos los archivos estén presentes
- El README.md se mostrará automáticamente en la página principal

## 📁 Archivos Incluidos en el Repositorio

- ✅ **Código fuente**: `src/visualizacion_hoteles.py`
- ✅ **Datos**: `data/ingresos_hoteles_1993_1995.csv`
- ✅ **Dependencias**: `requirements.txt`
- ✅ **Documentación**: `README.md`, `LICENSE`
- ✅ **Outputs**: Gráficos PNG, HTML interactivo, CSVs con métricas
- ✅ **Configuración**: `.gitignore`

## 🔧 Comandos Útiles para Futuras Actualizaciones

```bash
# Ver estado de cambios
git status

# Agregar cambios
git add .

# Hacer commit
git commit -m "Descripción de los cambios"

# Subir cambios
git push origin main
```

## 📊 Características del Proyecto

- **Análisis completo** de evolución temporal de ingresos
- **3 tipos de visualizaciones**: líneas temporales, slopegraph, dashboard interactivo
- **Métricas calculadas**: YoY, índices base, cambios totales
- **Análisis ejecutivo** con recomendaciones estratégicas
- **Código optimizado** y listo para producción
- **Documentación completa** en español

---

🎉 **¡Tu proyecto está listo para ser compartido en GitHub!**
