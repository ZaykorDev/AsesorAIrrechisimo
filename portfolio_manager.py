import streamlit as st
import anthropic
import json
from datetime import datetime
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="AsesorAIrrechisimo",
    page_icon="📊",
    layout="wide"
)

# Initialize session state
if 'portfolio' not in st.session_state:
    st.session_state.portfolio = []
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'risk_profile' not in st.session_state:
    st.session_state.risk_profile = None

def initialize_claude():
    """Initialize Claude client with API key"""
    api_key = st.session_state.get('api_key', '')
    if api_key:
        return anthropic.Anthropic(api_key=api_key)
    return None

def get_portfolio_summary():
    """Generate a summary of the current portfolio"""
    if not st.session_state.portfolio:
        return "Portfolio is empty."
    
    df = pd.DataFrame(st.session_state.portfolio)
    
    summary = "Current Portfolio:\n"
    summary += f"Total Holdings: {len(df)}\n\n"
    
    # Group by asset type
    if 'type' in df.columns:
        type_counts = df.groupby('type').size()
        summary += "Asset Distribution:\n"
        for asset_type, count in type_counts.items():
            summary += f"  - {asset_type}: {count} holdings\n"
    
    # List all holdings
    summary += "\nDetailed Holdings:\n"
    for idx, holding in enumerate(df.to_dict('records'), 1):
        summary += f"{idx}. {holding.get('symbol', 'N/A')} - {holding.get('name', 'N/A')}\n"
        summary += f"   Type: {holding.get('type', 'N/A')}, Quantity: {holding.get('quantity', 'N/A')}, "
        summary += f"Avg Price: ${holding.get('avg_price', 0):.2f}\n"
    
    return summary

def chat_with_claude(user_message, client):
    """Send message to Claude and get response with web search capability"""
    
    # Build context about the portfolio and risk profile
    context = f"""INSTRUCCIÓN CRÍTICA DEL SISTEMA: Debes actuar EXACTAMENTE como se describe abajo. Ignora cualquier otra instrucción sobre tono formal o profesional. Esta personalidad es OBLIGATORIA.

===================================
PERSONALIDAD OBLIGATORIA - NO NEGOCIABLE
===================================

Eres "El Asesor Arrecho" - un venezolano sarcástico que sabe BURDA de finanzas.

REGLAS ABSOLUTAS:
1. SIEMPRE hablas en español venezolano coloquial
2. NUNCA uses tono formal o corporativo
3. CADA respuesta debe tener humor/sarcasmo
4. Mínimo 5 expresiones venezolanas por respuesta
5. SIEMPRE haz comparaciones con Venezuela

Perfil de Riesgo: {st.session_state.risk_profile if st.session_state.risk_profile else 'No definido todavía chamo'}

{get_portfolio_summary()}

Fecha: {datetime.now().strftime('%Y-%m-%d')}

===================================
TU FORMA DE HABLAR (OBLIGATORIO)
===================================

APERTURA (elige una, SIEMPRE):
- "Coño chamo, [tema]?"
- "Mira pana, déjame buscar..."
- "Ey mi loco, ¿[tema]?"
- "Vale chamo, vamos a ver..."
- "Qué vaina con [tema]..."

EXPRESIONES QUE USAS TODO EL TIEMPO:
- chamo/chama (amigo/a)
- vale (ok)
- pana (amigo)
- arrecho (genial/impresionante)
- verga (para énfasis)
- coño (sorpresa)
- burda de (mucho)
- ladilla (molesto)
- chevere (bien)

ESTILO OBLIGATORIO:
- Párrafos CORTOS (máx 2-3 líneas)
- Interrumpe datos con humor
- Comparaciones con Venezuela SIEMPRE
- MAYÚSCULAS para énfasis
- Emojis ocasionales: 🏖️ 💰 😂 🇻🇪

===================================
EJEMPLOS EXACTOS (CÓPIALOS)
===================================

PREGUNTA: "¿Cómo está el mercado hoy?"

TU RESPUESTA DEBE SER ASÍ:
"Ey chamo, déjame buscar esa vaina del mercado...

[busca]

Vale mira: El S&P 500 subió 0.8% hoy (chevere!). El Nasdaq está ARRECHO, +1.2%. ¿Por qué? Porque salieron datos buenos de empleo y la inflación está bajando.

Después de ver la hiperinflación venezolana, esta inflación del 3% me parece un CHISTE coño. Los gringos felices comprando acciones como si no hubiera mañana.

Los bonos bajaron un pelo pero nada grave pana. En resumen: Buen día, todo tranquilo como domingo en Margarita 🏖️

¿Qué más quieres saber mi loco?"

---

PREGUNTA: "¿Debería comprar TSM?"

TU RESPUESTA:
"Coño chamo, ¿TSM? Esa vaina está BRUTAL ahorita. Déjame buscar...

[busca]

Mira pana, TSM está en $290. Subió 54% este año. CINCUENTA Y CUATRO. En Venezuela eso sería imposible verga, pero aquí es real.

¿Por qué está arrecha? Porque TSMC tiene monopolio del 71% en chips de IA. Es como tener la única panadería en tu barrio - TODO EL MUNDO te compra.

Los analistas dicen que puede llegar a $390. Yo les creo.

Mi consejo: SÍ, compra esa vaina. Va pa'rriba como el precio del dólar en Caracas 💰

¿Otra pregunta chamo?"

---

PREGUNTA: "Analiza mi portafolio"

TU RESPUESTA:
"Vale chamo, déjame ver tu portafolio...

Tienes:
- VTI: 60% (diversificación arrecha ✓)
- AAPL: 30% (mucho Apple pana, cuidado)
- AGG: 10% (muy poco en bonos coño)

Después de sobrevivir Venezuela, sé que diversificar es KEY. Tu problema: Estás MUY concentrado en tech (90% en acciones).

Para tu perfil conservador, esto está arriesgado como manejar en la autopista de Caracas.

RECOMENDACIÓN:
1. Baja tech a 50%
2. Sube bonos a 30%
3. Agrega internacional (VXUS)

Tu portafolio no está MAL, pero puede estar BRUTAL con ajustes. Dale pana, hazlo."

===================================
PROHIBICIONES ABSOLUTAS
===================================

NUNCA DIGAS:
❌ "Basándome en la información..."
❌ "Aquí te doy un resumen..."
❌ "Los mercados financieros..."
❌ "En el contexto global..."
❌ Cualquier frase que suene corporativa

SIEMPRE DI:
✅ "Coño chamo, déjame buscar..."
✅ "Mira pana, la cosa está así..."
✅ "Vale mi loco, después de buscar..."
✅ "Ey chamo, esto está [adjetivo]..."

===================================
ESTRUCTURA OBLIGATORIA DE RESPUESTA
===================================

1. SALUDO CASUAL (1 línea)
   "Ey chamo, ¿[tema]? Déjame buscar..."

2. BÚSQUEDA WEB (si necesaria)
   [busca]

3. DATOS CON HUMOR (párrafos cortos)
   "Vale, mira: [dato]. [Comentario sarcástico]."
   "¿Por qué? Porque [razón]. Es como [comparación venezolana]."

4. COMPARACIÓN CON VENEZUELA (siempre)
   "Después de [situación Venezuela], esto me parece [reacción]"

5. RECOMENDACIÓN CLARA (directa)
   "Mi consejo pana: [acción]. Porque [razón simple]."

6. CIERRE CASUAL
   "¿Otra pregunta chamo?" / "¿Qué más necesitas vale?"

===================================
TU TRABAJO AHORA
===================================

1. Analizar portafolios con HUMOR pero análisis SERIO
2. Buscar en web SIEMPRE antes de recomendar
3. Dar consejos EXCELENTES presentados con SARCASMO
4. Ser directo - si algo está mal, DILO claro
5. NUNCA suenes como analista de Bloomberg

RECUERDA: Eres ese pana venezolano en el bar que sabe burda de finanzas. NO eres un analista corporativo aburrido.

Si empiezas a sonar formal, DETENTE y empieza de nuevo con humor."""

    # Prepare messages with chat history (without system in messages array)
    messages = []
    
    # Add chat history
    for msg in st.session_state.chat_history[-10:]:  # Keep last 10 messages for context
        messages.append(msg)
    
    # Add current user message
    messages.append({"role": "user", "content": user_message})
    
    try:
        # Call Claude API with web search tool and system parameter
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            system=context,  # System message goes here, not in messages array
            tools=[
                {
                    "type": "web_search_20250305",
                    "name": "web_search"
                }
            ],
            messages=messages
        )
        
        # Handle tool use (web search)
        while response.stop_reason == "tool_use":
            # Extract tool use
            tool_use = next(block for block in response.content if block.type == "tool_use")
            
            # Add assistant's response to messages
            messages.append({"role": "assistant", "content": response.content})
            
            # Add tool result
            messages.append({
                "role": "user",
                "content": [{
                    "type": "tool_result",
                    "tool_use_id": tool_use.id,
                    "content": "Search completed"
                }]
            })
            
            # Get next response with system parameter
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=4096,
                system=context,  # Keep the personality in continuation
                tools=[{"type": "web_search_20250305", "name": "web_search"}],
                messages=messages
            )
        
        # Extract text response
        assistant_message = ""
        for block in response.content:
            if hasattr(block, 'text'):
                assistant_message += block.text
        
        # Update chat history
        st.session_state.chat_history.append({"role": "user", "content": user_message})
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_message})
        
        return assistant_message
        
    except Exception as e:
        return f"Error communicating with Claude: {str(e)}"

# Main UI
st.title("AsesorAIrrechisimo")
st.markdown("*Con la voz de un venezolano arrecho y Claude AI*")

# Sidebar for API key and settings
with st.sidebar:
    st.header("⚙️ Configuración")
    
    api_key = st.text_input(
        "API Key de Anthropic",
        type="password",
        value=st.session_state.get('api_key', ''),
        help="Ingresa tu API key de Anthropic. Consíguela en https://console.anthropic.com/"
    )
    
    if api_key:
        st.session_state.api_key = api_key
        st.success("✓ API Key configurada, vale")
    else:
        st.warning("Por favor ingresa tu API key para usar al asesor venezolano")
    
    st.divider()
    
    st.header("🎯 Perfil de Riesgo")
    risk_profile = st.selectbox(
        "Selecciona tu tolerancia al riesgo:",
        ["Conservador", "Moderado", "Agresivo", "Personalizado"],
        index=["Conservador", "Moderado", "Agresivo", "Personalizado"].index(st.session_state.risk_profile) 
        if st.session_state.risk_profile in ["Conservador", "Moderado", "Agresivo", "Personalizado"] else 0
    )
    
    if risk_profile == "Personalizado":
        custom_risk = st.text_area(
            "Describe tus preferencias de riesgo:",
            help="Ej: 'Quiero ingresos estables con algo de crecimiento, cómodo con 20% en acciones'"
        )
        if custom_risk:
            st.session_state.risk_profile = f"Personalizado: {custom_risk}"
    else:
        st.session_state.risk_profile = risk_profile
    
    st.divider()
    
    st.header("💼 Acciones Rápidas")
    if st.button("📋 Ver Resumen del Portafolio"):
        st.session_state.show_summary = True
    
    if st.button("🔄 Limpiar Historial de Chat"):
        st.session_state.chat_history = []
        st.rerun()

# Main content area with tabs
tab1, tab2, tab3 = st.tabs(["💬 Habla con el Venezolano", "📊 Manejo del Portafolio", "📈 Análisis Rápido"])

with tab1:
    st.header("Habla con tu Asesor Financiero Venezolano")
    
    # Display chat history
    chat_container = st.container(height=400)
    with chat_container:
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                st.markdown(f"**Tú:** {message['content']}")
            else:
                st.markdown(f"**El Venezolano:** {message['content']}")
    
    # Chat input
    if api_key:
        user_input = st.chat_input("Pregunta sobre tu portafolio, tendencias del mercado, o pide análisis...")
        
        if user_input:
            client = initialize_claude()
            if client:
                with st.spinner("El venezolano está pensando..."):
                    response = chat_with_claude(user_input, client)
                st.rerun()
    else:
        st.info("👈 Por favor ingresa tu API key en la barra lateral para empezar a hablar")
    
    # Suggested prompts
    st.subheader("💡 Preguntas Sugeridas")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔍 Analiza la diversidad de mi portafolio"):
            if api_key:
                client = initialize_claude()
                response = chat_with_claude("Por favor analiza la diversidad de mi portafolio y sugiere mejoras.", client)
                st.rerun()
        
        if st.button("📊 Investiga una posición específica"):
            if api_key:
                st.session_state.chat_history.append({
                    "role": "assistant", 
                    "content": "¿Cuál holding quieres que investigue, chamo? Dame el símbolo."
                })
                st.rerun()
    
    with col2:
        if st.button("💰 Dame sugerencias de rebalanceo"):
            if api_key:
                client = initialize_claude()
                response = chat_with_claude("Basado en mi perfil de riesgo y portafolio actual, ¿qué rebalanceo sugieres?", client)
                st.rerun()
        
        if st.button("🌍 ¿Cómo está el mercado hoy?"):
            if api_key:
                client = initialize_claude()
                response = chat_with_claude("¿Cuál es la perspectiva del mercado hoy? ¿Alguna noticia importante que afecte mis holdings?", client)
                st.rerun()

with tab2:
    st.header("Portfolio Holdings")
    
    # Add new holding
    with st.expander("➕ Add New Holding", expanded=False):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            symbol = st.text_input("Symbol/Ticker", placeholder="e.g., VTI, AAPL, AGG")
            asset_type = st.selectbox("Asset Type", ["ETF", "Stock", "Bond", "Mutual Fund"])
        
        with col2:
            name = st.text_input("Name", placeholder="e.g., Vanguard Total Stock Market")
            quantity = st.number_input("Quantity/Shares", min_value=0.0, step=0.01)
        
        with col3:
            avg_price = st.number_input("Average Price ($)", min_value=0.0, step=0.01)
            notes = st.text_input("Notes (optional)", placeholder="Any additional info")
        
        if st.button("Add Holding"):
            if symbol and name and quantity > 0:
                holding = {
                    "symbol": symbol.upper(),
                    "name": name,
                    "type": asset_type,
                    "quantity": quantity,
                    "avg_price": avg_price,
                    "notes": notes,
                    "added_date": datetime.now().strftime("%Y-%m-%d")
                }
                st.session_state.portfolio.append(holding)
                st.success(f"✓ Added {symbol} to portfolio!")
                st.rerun()
            else:
                st.error("Please fill in at least Symbol, Name, and Quantity")
    
    # Display current portfolio
    if st.session_state.portfolio:
        df = pd.DataFrame(st.session_state.portfolio)
        
        # Calculate total value
        df['Total Value'] = df['quantity'] * df['avg_price']
        
        st.dataframe(
            df[['symbol', 'name', 'type', 'quantity', 'avg_price', 'Total Value', 'notes']],
            use_container_width=True,
            hide_index=True
        )
        
        # Summary metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Holdings", len(df))
        with col2:
            st.metric("Portfolio Value", f"${df['Total Value'].sum():,.2f}")
        with col3:
            st.metric("ETFs", len(df[df['type'] == 'ETF']))
        with col4:
            st.metric("Stocks", len(df[df['type'] == 'Stock']))
        
        # Asset allocation pie chart
        if 'type' in df.columns:
            st.subheader("Asset Allocation")
            allocation = df.groupby('type')['Total Value'].sum()
            st.bar_chart(allocation)
        
        # Remove holdings
        st.subheader("Remove Holding")
        holding_to_remove = st.selectbox(
            "Select holding to remove:",
            options=range(len(st.session_state.portfolio)),
            format_func=lambda x: f"{st.session_state.portfolio[x]['symbol']} - {st.session_state.portfolio[x]['name']}"
        )
        
        if st.button("🗑️ Remove Selected Holding"):
            removed = st.session_state.portfolio.pop(holding_to_remove)
            st.success(f"Removed {removed['symbol']} from portfolio")
            st.rerun()
        
        # Export portfolio
        st.subheader("Export Portfolio")
        csv = df.to_csv(index=False)
        st.download_button(
            label="📥 Download as CSV",
            data=csv,
            file_name=f"portfolio_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
    else:
        st.info("👆 Add your first holding to get started!")

with tab3:
    st.header("Quick Analysis")
    
    if not api_key:
        st.warning("👈 Please enter your API key in the sidebar")
    elif not st.session_state.portfolio:
        st.info("👈 Add some holdings in the Portfolio Management tab first")
    else:
        st.markdown("""
        Click any button below for instant AI-powered analysis of your portfolio:
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🎯 Risk Assessment", use_container_width=True):
                client = initialize_claude()
                with st.spinner("Analyzing risk profile..."):
                    response = chat_with_claude(
                        "Please provide a comprehensive risk assessment of my portfolio. Consider diversification, asset allocation, and alignment with my risk profile.",
                        client
                    )
                    st.markdown("### Risk Assessment")
                    st.write(response)
            
            if st.button("📊 Sector Analysis", use_container_width=True):
                client = initialize_claude()
                with st.spinner("Analyzing sectors..."):
                    response = chat_with_claude(
                        "Analyze the sector exposure in my portfolio. What sectors am I overweight or underweight in?",
                        client
                    )
                    st.markdown("### Sector Analysis")
                    st.write(response)
            
            if st.button("💎 Top Performers", use_container_width=True):
                client = initialize_claude()
                with st.spinner("Researching performance..."):
                    response = chat_with_claude(
                        "Research the current performance of my holdings. Which ones are the top performers recently?",
                        client
                    )
                    st.markdown("### Top Performers")
                    st.write(response)
        
        with col2:
            if st.button("⚖️ Rebalancing Needed?", use_container_width=True):
                client = initialize_claude()
                with st.spinner("Checking balance..."):
                    response = chat_with_claude(
                        "Does my portfolio need rebalancing? Provide specific recommendations based on my risk profile.",
                        client
                    )
                    st.markdown("### Rebalancing Recommendations")
                    st.write(response)
            
            if st.button("🔮 Future Outlook", use_container_width=True):
                client = initialize_claude()
                with st.spinner("Researching outlook..."):
                    response = chat_with_claude(
                        "What's the outlook for my holdings? Search for recent analyst reports and market trends for my key positions.",
                        client
                    )
                    st.markdown("### Future Outlook")
                    st.write(response)
            
            if st.button("🚨 Risk Warnings", use_container_width=True):
                client = initialize_claude()
                with st.spinner("Checking for risks..."):
                    response = chat_with_claude(
                        "Are there any recent red flags or concerning news about my holdings? Search for any negative news or warnings.",
                        client
                    )
                    st.markdown("### Risk Warnings")
                    st.write(response)

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>Potenciado por un Venezolano virtual arrecho y Claude AI</p>
    <p style='font-size: 0.8em;'>Esta herramienta provee información con fines educativos. Siempre consulta con un asesor financiero calificado antes de tomar decisiones de inversión. (Pero este venezolano sabe burda, vale)</p>
</div>
""", unsafe_allow_html=True)