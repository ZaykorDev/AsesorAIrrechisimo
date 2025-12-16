# Administrador de Portafolio de Papá

Una aplicación Streamlit con un asesor financiero venezolano sarcástico pero brillante, potenciado por Claude AI.

## Guía de Configuración para el Regalo de Navidad

### Requisitos Previos
- Python 3.8 o superior
- Una API key de Anthropic ([Consíguela aquí](https://console.anthropic.com/))

### Pasos de Instalación

1. **Instalar paquetes de Python:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Ejecutar la aplicación:**
   ```bash
   streamlit run portfolio_manager.py
   ```

3. **Acceder a la app:**
   - La app se abrirá automáticamente en tu navegador
   - Usualmente en: `http://localhost:8501`

### Configuración Inicial

1. **Ingresar API Key:**
   - En la barra lateral, ingresa tu API key de Anthropic
   - La key se guarda solo para la sesión (no permanentemente)
   - Consigue una key en: https://console.anthropic.com/

2. **Configurar Perfil de Riesgo:**
   - Elige entre: Conservador, Moderado, o Agresivo
   - O selecciona "Personalizado" para describir preferencias específicas

3. **Agregar Holdings del Portafolio:**
   - Ve a la pestaña "Manejo del Portafolio"
   - Haz clic en "Agregar Nuevo Holding"
   - Ingresa detalles para cada ETF, acción o bono

### Características

#### Habla con el Venezolano
- Haz preguntas sobre tu portafolio
- Obtén análisis del mercado y recomendaciones
- Investiga acciones o ETFs específicos
- El asesor usa búsqueda web para obtener datos actuales del mercado

**Ejemplos de preguntas:**
- "Analiza la diversidad de mi portafolio"
- "¿Qué opinas de VTI?"
- "¿Debería rebalancear mi portafolio?"
- "¿Hay algún riesgo en mis holdings actuales?"

#### Manejo del Portafolio
- Agregar/eliminar holdings
- Ver asignación de activos
- Rastrear valor total del portafolio
- Exportar datos del portafolio a CSV

#### Análisis Rápido
Botones de análisis de un click para:
- Evaluación de riesgos
- Análisis por sector
- Mejores rendimientos
- Recomendaciones de rebalanceo
- Perspectiva futura
- Advertencias de riesgo

### Cómo Funciona

1. **Contexto del Portafolio:** Claude tiene visibilidad completa de tus holdings, cantidades y precios
2. **Consciente del Riesgo:** Las recomendaciones se adaptan a tu perfil de riesgo declarado
3. **Datos Actuales:** Usa búsqueda web para obtener información del mercado en tiempo real
4. **Conversacional:** Interfaz de chat natural - ¡solo haz preguntas!
5. **Personalidad Venezolana:** Respuestas con humor sarcástico venezolano pero análisis serio

### La Personalidad Venezolana

Tu asesor financiero es un venezolano sarcástico que:
- Habla SIEMPRE en español
- Usa expresiones venezolanas: "chamo", "vale", "arrecho", "pana", "coño"
- Hace comentarios irónicos pero útiles
- Da consejos financieros EXCELENTES
- Referencia la economía venezolana para perspectiva
- Es directo y honesto (sin pelos en la lengua)

**Ejemplo:**
```
Tú: "¿Cómo está mi portafolio?"

El Venezolano: "Chamo, tu portafolio está más diversificado 
que una hallaca bien hecha, te felicito verga. VTI subió 0.8% 
hoy (arrecho). Con tu perfil conservador, déjalo tranquilo pana, 
ese ETF es más estable que... bueno, que cualquier cosa en 
Venezuela coño."
```

### Ejemplos de Flujos de Trabajo

#### Comenzando
1. Agregar todos los holdings actuales al portafolio
2. Configurar perfil de riesgo en la barra lateral
3. Preguntar a Claude: "Por favor dame un resumen de mi portafolio"

#### Chequeos Regulares
1. Hacer clic en "¿Cómo está el mercado hoy?" 
2. Revisar cualquier rebalanceo sugerido
3. Preguntar sobre holdings específicos si hay preocupación

#### Modo Investigación
1. "Investiga [TICKER] - ¿es buena compra ahora?"
2. "Compara VTI vs VOO para mi portafolio"
3. "¿Qué dicen los analistas sobre [TICKER]?"

### Tips para Mejores Resultados

- **Sé específico:** En lugar de "¿Qué piensas?", pregunta "¿Debería aumentar mi asignación en bonos?"
- **Actualiza regularmente:** Mantén tus holdings del portafolio actualizados
- **Haz seguimientos:** Claude recuerda el contexto de la conversación
- **Usa Análisis Rápido:** Genial para chequeos rutinarios

### Notas de Seguridad

- Las API keys se guardan solo en memoria de sesión (no en disco)
- Los datos del portafolio permanecen locales en tu computadora
- No se comparten datos excepto con Claude API para análisis
- Considera la función de exportación CSV para respaldo

### Solución de Problemas

**"Por favor ingresa tu API key"**
- Ingresa tu API key de Anthropic en la barra lateral
- Asegúrate que comience con "sk-ant-"

**"Error comunicándose con Claude"**
- Verifica tu conexión a internet
- Verifica que tu API key sea válida
- Asegúrate de tener créditos API restantes

**El portafolio no se muestra**
- Asegúrate de agregar holdings en la pestaña Manejo del Portafolio
- Verifica que cantidad y precio sean mayores que 0

### Conseguir una API Key

1. Ve a https://console.anthropic.com/
2. Regístrate o inicia sesión
3. Navega a "API Keys"
4. Crea una nueva key
5. Copia y pega en la app

**Costo:** La API de Claude es de pago por uso. Uso típico:
- Cada mensaje de chat: ~$0.01-0.05
- Análisis rápido: ~$0.02-0.10
- ¡Muy accesible para uso personal!

### Descargo de Responsabilidad

Esta herramienta es solo con fines informativos y educativos. No constituye asesoría financiera. Siempre consulta con un asesor financiero calificado antes de tomar decisiones de inversión.

### Soporte

Si encuentras problemas:
1. Revisa este README
2. Asegúrate de que todos los requisitos estén instalados
3. Verifica la versión de Python (3.8+)
4. Verifica que la API key sea válida

---

Potenciado por un Venezolano Virtual y Claude AI