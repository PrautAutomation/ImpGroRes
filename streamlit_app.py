import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from datetime import datetime, time

# Konfigurace stránky
try:
    st.set_page_config(
        page_title="AI Orchestrator - Hotel Management",
        page_icon="🏨",
        layout="wide",
        initial_sidebar_state="expanded"
    )
except st.errors.StreamlitAPIException:
    pass

# Custom CSS s novou modrou barvou #007bff
st.markdown("""
<style>
/* Import moderních fontů */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

/* Globální styling */
.main-container {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

/* Header s gradientem */
.main-header {
    background: linear-gradient(135deg, #007bff 0%, #0056b3 100%);
    padding: 2.5rem;
    border-radius: 16px;
    color: white;
    text-align: center;
    margin-bottom: 2rem;
    box-shadow: 0 8px 32px rgba(0,123,255,0.25);
    border: none;
}

.main-header h1 {
    margin: 0 0 0.5rem 0;
    font-size: 2.2rem;
    font-weight: 700;
    text-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.main-header h2 {
    margin: 0 0 0.5rem 0;
    font-size: 1.4rem;
    font-weight: 500;
    opacity: 0.95;
}

.main-header p {
    margin: 0;
    font-size: 1rem;
    opacity: 0.85;
}

/* Karty komponent */
.component-card {
    background: #ffffff;
    padding: 1.5rem;
    border-radius: 12px;
    margin: 1rem 0;
    border-left: 4px solid #007bff;
    box-shadow: 0 4px 16px rgba(0,0,0,0.08);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    border: 1px solid #e9ecef;
}

.component-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0,123,255,0.15);
}

.component-card h3 {
    color: #212529;
    margin-bottom: 0.75rem;
    font-weight: 600;
    font-size: 1.2rem;
}

.component-card p {
    color: #6c757d;
    line-height: 1.6;
    margin-bottom: 1rem;
}

/* WoW karty */
.wow-card {
    background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
    padding: 2rem;
    border-radius: 16px;
    margin: 1.5rem 0;
    border: 2px solid rgba(0,123,255,0.15);
    box-shadow: 0 8px 24px rgba(0,123,255,0.12);
}

.wow-card h3 {
    color: #007bff;
    margin-bottom: 1rem;
    font-size: 1.3rem;
    font-weight: 600;
}

.wow-card p {
    color: #212529;
    font-size: 1.05rem;
    line-height: 1.6;
    margin-bottom: 1.5rem;
}

/* Metriky karty */
.metric-card {
    background: #ffffff;
    padding: 1.5rem;
    border-radius: 12px;
    text-align: center;
    margin: 0.5rem;
    border: 1px solid #e9ecef;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    transition: transform 0.2s ease;
}

.metric-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.1);
}

.metric-card h4 {
    color: #007bff;
    font-size: 0.9rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.metric-card h2 {
    color: #212529;
    font-size: 2rem;
    font-weight: 700;
    margin: 0.5rem 0;
}

.metric-card p {
    color: #28a745;
    font-size: 0.85rem;
    font-weight: 500;
    margin: 0;
}

/* Flow container */
.flow-container {
    background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
    padding: 2rem;
    border-radius: 16px;
    margin: 1rem 0;
    border: 1px solid #e9ecef;
    box-shadow: 0 4px 16px rgba(0,0,0,0.05);
}

/* Sidebar styling */
div[data-testid="stSidebar"] {
    background: #ffffff;
    border-right: 1px solid #e9ecef;
}

div[data-testid="stSidebar"] .css-1d391kg {
    background: #ffffff;
}

/* Sidebar header */
.sidebar-header {
    background: linear-gradient(135deg, #007bff 0%, #0056b3 100%);
    padding: 1.5rem;
    border-radius: 12px;
    color: white;
    text-align: center;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 12px rgba(0,123,255,0.3);
}

.sidebar-header h2 {
    margin: 0;
    font-size: 1.1rem;
    font-weight: 600;
}

/* Stats grid */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
    margin-bottom: 2rem;
}

/* Benefit list */
.benefit-list {
    list-style: none;
    padding: 0;
    margin: 1rem 0;
}

.benefit-list li {
    padding: 0.5rem 0;
    color: #212529;
    display: flex;
    align-items: center;
    font-size: 0.95rem;
    line-height: 1.5;
}

.benefit-list li::before {
    content: "✓";
    color: #28a745;
    font-weight: bold;
    font-size: 1.1rem;
    margin-right: 0.5rem;
    min-width: 1.2rem;
}

/* Example box */
.example-box {
    background: rgba(0,123,255,0.05);
    border: 1px solid rgba(0,123,255,0.2);
    border-radius: 8px;
    padding: 1rem;
    margin: 1rem 0;
    font-style: italic;
}

.example-box strong {
    color: #007bff;
    font-weight: 600;
}

/* Chat styling */
.chat-container {
    background: #ffffff;
    border: 1px solid #e9ecef;
    border-radius: 12px;
    padding: 1rem;
    margin-top: 1rem;
    max-height: 400px;
    overflow-y: auto;
}

.chat-message {
    margin-bottom: 1rem;
    padding: 0.75rem 1rem;
    border-radius: 12px;
    max-width: 80%;
}

.chat-message.user {
    background: #007bff;
    color: white;
    margin-left: auto;
    margin-right: 0;
    text-align: right;
}

.chat-message.assistant {
    background: #f8f9fa;
    color: #212529;
    border: 1px solid #e9ecef;
    margin-left: 0;
    margin-right: auto;
}

/* Footer */
.footer {
    background: linear-gradient(135deg, #007bff 0%, #0056b3 100%);
    padding: 2rem;
    border-radius: 16px;
    color: white;
    text-align: center;
    margin-top: 3rem;
}

.footer h3 {
    margin: 0 0 0.5rem 0;
    font-weight: 600;
}

.footer p {
    margin: 0.25rem 0;
    opacity: 0.9;
}

.footer em {
    opacity: 0.8;
    font-size: 0.9rem;
}

/* Streamlit specifické úpravy */
.stSelectbox > div > div {
    background-color: #ffffff;
    border: 1px solid #e9ecef;
    border-radius: 8px;
}

.stSelectbox > div > div:focus-within {
    border-color: #007bff;
    box-shadow: 0 0 0 3px rgba(0,123,255,0.1);
}

.stMetric {
    background: #ffffff;
    padding: 1rem;
    border-radius: 8px;
    border: 1px solid #e9ecef;
    margin-bottom: 0.5rem;
}

.stButton > button {
    background: #007bff;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 0.5rem 1rem;
    font-weight: 500;
    transition: background-color 0.2s ease;
}

.stButton > button:hover {
    background: #0056b3;
}

/* Responsivní design */
@media (max-width: 768px) {
    .stats-grid {
        grid-template-columns: 1fr;
    }
    
    .main-header {
        padding: 1.5rem;
    }
    
    .main-header h1 {
        font-size: 1.8rem;
    }
}
</style>
""", unsafe_allow_html=True)

# Hlavní nadpis
st.markdown("""
<div class="main-header">
    <h1>🤖 AI Orchestrator Agent</h1>
    <h2>🏨 Hotel Management System</h2>
    <p>Revoluce v hotelnictví pomocí umělé inteligence</p>
</div>
""", unsafe_allow_html=True)

# Data pro komponenty
components_data = {
    "Externí Interface": {
        "description": "Vstupní body pro komunikaci s hosty a systémy",
        "data_types": [
            "📧 Email rezervace, dotazy hostů, stížnosti",
            "💬 Chat zprávy (web, WhatsApp, Messenger)",
            "📞 Telefonní přepisy (speech-to-text)",
            "📋 Formuláře (booking.com, Airbnb, vlastní web)",
            "📄 Skenované dokumenty (smlouvy, faktury)",
            "🌡️ IoT senzory (teplota, obsazenost, čistota)"
        ],
        "icon": "🌐"
    },
    "Ollama LLM": {
        "description": "Centrální orchestrátor s umělou inteligencí",
        "data_types": [
            "🧠 Natural language understanding dotazů",
            "😊 Sentiment analýza recenzí a feedback",
            "📂 Automatické kategorizace problémů",
            "✍️ Generování personalizovaných odpovědí",
            "⚡ Rozhodovací logika pro eskalaci",
            "🔄 Workflow orchestrace"
        ],
        "icon": "🧠"
    },
    "Relační Database": {
        "description": "Strukturovaná data s přesnými vztahy",
        "data_types": [
            "👥 Profily hostů, preference, historie",
            "🏨 Rezervace, pricing, platby",
            "👨‍💼 Personální databáze zaměstnanců",
            "🤝 Dodavatelé, smlouvy, SLA",
            "📊 Rozvrhy služeb, qualifikace",
            "📈 Performance metriky, mzdy"
        ],
        "icon": "🗄️"
    },
    "Vektorová Database": {
        "description": "Nestrukturovaná data pro sémantické vyhledávání",
        "data_types": [
            "📚 Manuály, postupy, best practices",
            "⭐ Recenze hostů, feedback analýza",
            "🎨 Marketingové materiály, brand guidelines",
            "🎓 Training materiály pro personál",
            "📧 Email historie s kontextem",
            "🎵 Hlasové nahrávky, foto dokumentace"
        ],
        "icon": "🔍"
    }
}

# WoW efekty data
wow_effects = {
    "AI Concierge & Revenue Optimization": {
        "description": "Automatická personalizace a zvýšení tržeb",
        "benefits": [
            "💰 Revenue nárůst až +25% bez additional effort",
            "🎯 Personalizované upsell nabídky v real-time",
            "📈 Automatická analýza historie + preferences",
            "⚡ Instant nabídky při check-inu"
        ],
        "example": "Pan Novák (wellness lover) → automaticky spa balíček s 15% slevou při check-inu",
        "savings": 125000,
        "confidence": 90
    },
    "Prediktivní Maintenance & Cost Control": {
        "description": "AI předpovídá problémy a optimalizuje náklady",
        "benefits": [
            "🔧 Predikce poruch před jejich vznikem",
            "💡 Optimální timing pro nákupy",
            "👥 Smart staffing na základě predikce",
            "💰 15-30% úspora provozních nákladů"
        ],
        "example": "AI detekuje klimatizaci v pokoji 205 → plánuje výměnu před poruchou",
        "savings": 75000,
        "confidence": 85
    }
}

# Sidebar navigation
st.sidebar.markdown("""
<div class="sidebar-header">
    <h2>🧭 Navigation</h2>
</div>
""", unsafe_allow_html=True)

view_mode = st.sidebar.selectbox(
    "Vyberte pohled:",
    [
        "📊 Executive Dashboard",
        "🔍 Komponenty Deep Dive", 
        "✨ ROI & WoW Efekty",
        "📑 Strategická analýza",
        "🤖 Průzkum trhu pro AI a Hotelnictvi",
        "🔗 Odkazy pouzite v pruzkumu"
    ]
)

# Sidebar metriky
st.sidebar.markdown("---")
st.sidebar.markdown("### 📊 Klíčové Metriky")
st.sidebar.metric("💰 ROI", "143%", "↗️ +43% vs benchmark")
st.sidebar.metric("⏰ Payback", "7.4 měsíců", "↗️ 65% rychlejší")
st.sidebar.metric("🏨 Efektivita", "94%", "↗️ +24%")

# Přidání sekce "Použité odkazy" do sidebaru


# Načtení sekcí a odkazů ze souboru odkazy (pokud existuje)
import os

odkazy_dict = {
    "Pruzkum": [],
    "AI Agenti": [],
    "Imperial Pruzkum": []
}

if os.path.exists("odkazy"):
    current_section = None
    with open("odkazy", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.endswith(":"):
                current_section = line[:-1]
            elif current_section and current_section in odkazy_dict:
                odkazy_dict[current_section].append(line)


# Main content based on view mode
if view_mode == "📊 Executive Dashboard":
    st.markdown("## 🎯 Executive Dashboard")
    
    # Metriky v horní části
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h4>💰 Revenue Boost</h4>
            <h2>125%</h2>
            <p>↗️ +25% vs baseline</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h4>📉 Cost Reduction</h4>
            <h2>30%</h2>
            <p>↗️ -30% vs baseline</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        # Customer Satisfaction kruhový graf
        fig_satisfaction = go.Figure(data=[go.Pie(
            labels=['Spokojenost', 'Nespokojenost'], 
            values=[94, 6],
            hole=.6,
            marker_colors=['#007bff', '#e9ecef']
        )])
        fig_satisfaction.update_layout(
            title="Customer Satisfaction",
            height=200,
            margin=dict(l=20, r=20, t=40, b=20),
            showlegend=False,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_satisfaction, use_container_width=True)
    
    with col4:
        # AI Efficiency Growth čárový graf
        months = ['Q1', 'Q2', 'Q3', 'Q4']
        efficiency = [65, 78, 89, 94]
        
        fig_timeline = go.Figure(data=go.Scatter(
            x=months, y=efficiency,
            mode='lines+markers',
            line=dict(color='#007bff', width=3),
            marker=dict(size=8, color='#0056b3')
        ))
        fig_timeline.update_layout(
            title="AI Efficiency Growth",
            height=200,
            margin=dict(l=20, r=20, t=40, b=20),
            yaxis=dict(range=[50, 100]),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig_timeline, use_container_width=True)
    
    st.markdown("---")
    
    # System Architecture Overview
    st.markdown("## 🏗️ System Architecture Overview")
    
    col1, col2 = st.columns(2)
    
    with col1:
        for comp_name in ["Externí Interface", "Relační Database"]:
            comp = components_data[comp_name]
            st.markdown(f"""
            <div class="component-card">
                <h3>{comp['icon']} {comp_name}</h3>
                <p>{comp['description']}</p>
                <p><strong>Datové typy:</strong> {len(comp['data_types'])} kategorií</p>
            </div>
            """, unsafe_allow_html=True)
            
            with st.expander(f"📋 Detail {comp_name}"):
                for item in comp['data_types']:
                    st.write(f"• {item}")
    
    with col2:
        for comp_name in ["Ollama LLM", "Vektorová Database"]:
            comp = components_data[comp_name]
            st.markdown(f"""
            <div class="component-card">
                <h3>{comp['icon']} {comp_name}</h3>
                <p>{comp['description']}</p>
                <p><strong>Datové typy:</strong> {len(comp['data_types'])} kategorií</p>
            </div>
            """, unsafe_allow_html=True)
            
            with st.expander(f"📋 Detail {comp_name}"):
                for item in comp['data_types']:
                    st.write(f"• {item}")

elif view_mode == "🔍 Komponenty Deep Dive":
    st.markdown("## 🔬 Detailní Analýza Komponent")
    
    selected_component = st.selectbox(
        "Vyberte komponentu pro analýzu:",
        list(components_data.keys())
    )
    
    if selected_component:
        comp = components_data[selected_component]
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"""
            <div class="component-card">
                <h2>{comp['icon']} {selected_component}</h2>
                <p style="font-size: 1.1em;">{comp['description']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("### 📊 Distribuce Datových Typů")
            
            # Vytvoření dat pro koláčový graf
            labels = [item.split(" ", 1)[1] if " " in item else item for item in comp['data_types']]
            values = np.random.randint(15, 25, len(labels))
            
            fig = px.pie(
                values=values, 
                names=labels,
                title=f"Datová distribuce - {selected_component}",
                color_discrete_sequence=px.colors.sequential.Blues
            )
            fig.update_traces(textposition='inside', textinfo='percent+label')
            fig.update_layout(height=400, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("### 📈 Metriky Komponenty")
            
            throughput = np.random.randint(950, 1150)
            accuracy = np.random.uniform(0.94, 0.98)
            latency = np.random.randint(75, 95)
            
            st.markdown(f"""
            <div class="metric-card">
                <h4>⚡ Throughput</h4>
                <h2>{throughput}</h2>
                <p>req/min ↗️ +12%</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="metric-card">
                <h4>🎯 Accuracy</h4>
                <h2>{accuracy:.1%}</h2>
                <p>↗️ +2.3%</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="metric-card">
                <h4>⏱️ Latency</h4>
                <h2>{latency}ms</h2>
                <p>↘️ -15ms</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("### 📋 Kompletní Seznam Datových Typů")
        for i, item in enumerate(comp['data_types']):
            st.checkbox(f"{item}", value=True, key=f"check_{i}_{selected_component}")

elif view_mode == "✨ ROI & WoW Efekty":
    st.markdown("## 🚀 ROI Analýza & WoW Efekty")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_savings = sum([effect['savings'] for effect in wow_effects.values()])
        st.markdown(f"""
        <div class="metric-card">
            <h4>💰 Total Annual Savings</h4>
            <h2>${total_savings:,}</h2>
            <p>↗️ +$50k vs estimate</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        investment = 74000
        roi = ((total_savings - investment) / investment) * 100
        st.markdown(f"""
        <div class="metric-card">
            <h4>📊 ROI</h4>
            <h2>{roi:.0f}%</h2>
            <p>↗️ +43% vs industry</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        payback = investment / (total_savings / 12)
        st.markdown(f"""
        <div class="metric-card">
            <h4>⏰ Payback Period</h4>
            <h2>{payback:.1f}</h2>
            <p>měsíců ↗️ 65% rychlejší</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### 💹 ROI Waterfall Analysis")
    
    fig_waterfall = go.Figure(go.Waterfall(
        name="ROI Analysis",
        orientation="v",
        measure=["absolute", "relative", "relative", "relative", "total"],
        x=["Počáteční Investice", "Revenue Boost", "Cost Savings", "Operational Efficiency", "Net ROI"],
        textposition="outside",
        text=["-$74k", "+$125k", "+$75k", "+$25k", "$151k"],
        y=[-74000, 125000, 75000, 25000, 151000],
        connector={"line": {"color": "rgb(63, 63, 63)"}},
        decreasing={"marker": {"color": "#dc3545"}},
        increasing={"marker": {"color": "#007bff"}},
        totals={"marker": {"color": "#0056b3"}}
    ))
    fig_waterfall.update_layout(
        title="ROI Waterfall Chart", 
        height=400, 
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig_waterfall, use_container_width=True)
    
    st.markdown("---")
    
    # WoW efekty
    for effect_name, effect_data in wow_effects.items():
        st.markdown(f"""
        <div class="wow-card">
            <h3>⭐ {effect_name}</h3>
            <p>{effect_data['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("**🎯 Klíčové benefity:**")
            benefit_html = '<div class="benefit-list">'
            for benefit in effect_data['benefits']:
                benefit_html += f'<li>{benefit}</li>'
            benefit_html += '</div>'
            st.markdown(benefit_html, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="example-box">
                <strong>💡 Praktický příklad:</strong><br>
                {effect_data['example']}
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Confidence gauge
            fig_confidence = go.Figure(go.Indicator(
                mode="gauge+number",
                value=effect_data['confidence'],
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Confidence Level"},
                gauge={
                    'axis': {'range': [None, 100]},
                    'bar': {'color': "#007bff"},
                    'steps': [
                        {'range': [0, 70], 'color': "#e9ecef"},
                        {'range': [70, 100], 'color': "#dee2e6"}
                    ]
                }
            ))
            fig_confidence.update_layout(
                height=200, 
                paper_bgcolor='rgba(0,0,0,0)', 
                plot_bgcolor='rgba(0,0,0,0)'
            )
            st.plotly_chart(fig_confidence, use_container_width=True)
            
            st.markdown(f"""
            <div class="metric-card">
                <h4>💰 Annual Savings</h4>
                <h2>${effect_data['savings']:,}</h2>
            </div>
            """, unsafe_allow_html=True)

elif view_mode == "🤖 BOT":
    st.markdown("## 🤖 Interaktivní Firemní Bot")
    
    # Zde bude načtena React komponenta pro chat
    st.info("Bot sekce byla přidána. Připravuji integraci React komponenty...")
    
elif view_mode == "🤖 AI Concierge Demo":
    st.markdown("## 💬 Vyzkoušejte si AI Concierge (Demo)")
    st.markdown("""
    <div class="component-card">
        <p>Zeptejte se našeho AI Concierge na služby hotelu, rezervace nebo doporučení!</p>
    </div>
    """, unsafe_allow_html=True)

    # Chat inicializace
    if 'messages' not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Dobrý den! Jak Vám mohu dnes pomoci s Vaším pobytem v Imperial Group?"}
        ]

    # Chat container
    chat_container = st.container()
    with chat_container:
        # Zobrazení zpráv
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(f"""
                <div class="chat-message user">
                    {msg["content"]}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="chat-message assistant">
                    {msg["content"]}
                </div>
                """, unsafe_allow_html=True)

    # Chat input
    user_input = st.text_input("Vaše otázka:", key="chat_input")
    if st.button("Odeslat") and user_input:
        # Přidání uživatelské zprávy
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Jednoduchá AI odpověď
        response = "Omlouvám se, na tuto otázku zatím neumím odpovědět. Stále se učím."
        user_input_lower = user_input.lower()
        
        if "lázně" in user_input_lower or "spa" in user_input_lower or "wellness" in user_input_lower:
            response = "Nabízíme širokou škálu lázeňských a wellness procedur, včetně tradičních karlovarských kúr. Doporučuji například náš balíček 'Relaxační Sen' nebo program 'Medical Spa Classic'. Mám Vám ukázat detaily nebo zjistit dostupnost?"
        elif "rezervace" in user_input_lower or "booking" in user_input_lower or "pokoj" in user_input_lower:
            response = "Pro rezervaci pokoje můžete navštívit naši webovou stránku imperial-group.cz nebo kontaktovat přímo naši recepci. Mohu Vám pomoci najít kontaktní údaje nebo specifický typ pokoje?"
        elif "restaurace" in user_input_lower or "jídlo" in user_input_lower:
            response = "V našem hotelu Imperial naleznete několik restaurací, například Paris a Prague, a také Café Vienna. Každá nabízí unikátní kulinářské zážitky. Chcete si rezervovat stůl nebo se podívat na menu?"
        elif "děkuji" in user_input_lower or "díky" in user_input_lower:
            response = "Rádo se stalo! Pokud budete mít další dotazy, neváhejte se zeptat."
        
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

elif view_mode == "📑 Strategická analýza":
    st.markdown("## 🧩 Strategická analýza")
    try:
        with open("strategicka_analyza.md", "r", encoding="utf-8") as file:
            st.markdown(file.read())
    except FileNotFoundError:
        st.warning("Soubor strategicka_analyza.md nebyl nalezen.")

elif view_mode == "🤖 Průzkum trhu pro AI a Hotelnictvi":
    st.markdown("## 🧠 Průzkum trhu pro AI a Hotelnictví")
    try:
        with open("research.md", "r", encoding="utf-8") as file:
            st.markdown(file.read())
    except FileNotFoundError:
        st.warning("Soubor research.md nebyl nalezen.")

elif view_mode == "🔗 Odkazy pouzite v pruzkumu":
    st.markdown("""
    ### 🔍 Deep Research od Praut s.r.o.
    **Chytré rozhodování začíná hlubokou znalostí**

    Deep Research je náš proprietární nástroj pro automatizované zkoumání, třídění a syntézu komplexních informací pomocí umělé inteligence. Využívá pokročilé AI modely, které kombinují analýzu velkých dat s hlubokým porozuměním kontextu — a to vše ve službách vašeho rozhodování.

    **🧠 Jak funguje Deep Research?**
    - **Inteligentní sběr dat**  
      Automaticky prochází a shromažďuje informace z různorodých zdrojů – od otevřených webových databází přes odborné články až po interní dokumentaci, pokud je k dispozici.
    - **Kognitivní analýza**  
      Pomocí AI modelů provádí rozpoznávání vzorů, protichůdných tvrzení, slepých míst a klíčových bodů. Výstup není jen souhrn, ale interpretace — tedy informace s přidanou hodnotou.
    - **Prioritizace a filtrování**  
      Relevance je základ. Systém odfiltruje balast a zdůrazní to, co je pro vás a vaše rozhodnutí skutečně podstatné.
    - **Strukturovaný výstup**  
      Výsledky jsou přehledně organizované do reportu nebo interaktivního dashboardu, připraveného pro další akce, strategie nebo prezentaci.

    **✅ Co získáte?**
    - Komplexní přehled o dané problematice – faktech, trendech, hráčích i příležitostech.
    - Podklady pro rozhodování – hlubší vhled, který běžné rešerše nenabízí.
    - Zrychlení práce týmu – to, co by analytik hledal dny, máte do pár hodin.
    - Podporu strategie a inovací – např. při vstupu na nový trh, výběru dodavatele, konkurenci či analýze produktového portfolia.

    **🛠️ Komu Deep Research pomáhá?**
    Firmám, které:
    - potřebují kvalitní podklady pro strategická rozhodnutí,
    - chtějí nahradit manuální rešerše rychlejší a přesnější metodou,
    - pracují v dynamických odvětvích s vysokým objemem informací,
    - využívají AI k budování konkurenční výhody.

    **💡 Příklad využití:**  
    „Klient vstupoval na nový německý trh s digitální službou. Během 6 hodin jsme pomocí Deep Research dodali přehled konkurence, analýzu vývoje trhu, regulatorní rámec a doporučení k positioningové strategii. Z původně plánovaných 3 týdnů rešerše byly jen 2 dny.“
    """)

    # Dropdown menu s odkazy podle sekcí (přidej unikátní klíč)
    def parse_pruzkum_file(file_path):
        """Parsuje soubor pruzkum.txt a vrací strukturované odkazy podle sekcí"""
        odkazy_dict = {
            "Pruzkum": [],
            "AI Agents": [],
            "Imperial Pruzkum": []
        }
        
        if not os.path.exists(file_path):
            return odkazy_dict
            
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        current_section = None
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # Detekce sekce
            if line.endswith(" :") or line.endswith(":"):
                section_name = line.rstrip(": ").strip()
                if "Pruzkum" in section_name and "Imperial" not in section_name:
                    current_section = "Pruzkum"
                elif "AI Agenti" in section_name:
                    current_section = "AI Agenti"
                elif "Imperial" in section_name:
                    current_section = "Imperial Pruzkum"
                continue
            
            # Parsování odkazu
            if current_section and current_section in odkazy_dict:
                # Formát: "název, použito datum, URL"
                if "http" in line:
                    parts = line.split(", http")
                    if len(parts) >= 2:
                        nazev_a_datum = parts[0]
                        url = "http" + parts[1]
                        
                        # Oddělení názvu od data
                        if ", použito " in nazev_a_datum:
                            nazev = nazev_a_datum.split(", použito ")[0]
                            datum = nazev_a_datum.split(", použito ")[1] if len(nazev_a_datum.split(", použito ")) > 1 else ""
                        else:
                            nazev = nazev_a_datum
                            datum = ""
                        
                        odkazy_dict[current_section].append({
                            "nazev": nazev.strip(),
                            "datum": datum.strip(),
                            "url": url.strip()
                        })
        
        return odkazy_dict

    # Načtení a parsování odkazů z pruzkum.txt
    import os
    odkazy_dict = parse_pruzkum_file("pruzkum.txt")

    # Dropdown menu pro výběr sekce
    dropdown_section = st.selectbox(
        "Vyberte sekci odkazů:",
        list(odkazy_dict.keys()),
        key="odkazy_dropdown_pruzkum"
    )

    # Zobrazení odkazů pro vybranou sekci
    if odkazy_dict[dropdown_section]:
        st.markdown(f"#### 📋 {dropdown_section} ({len(odkazy_dict[dropdown_section])} odkazů)")
        
        # Přidání vyhledávání v rámci sekce
        search_term = st.text_input(
            "🔍 Vyhledávání v této sekci:", 
            placeholder="Zadejte klíčové slovo...",
            key=f"search_{dropdown_section}"
        )
        
        filtered_odkazy = odkazy_dict[dropdown_section]
        if search_term:
            filtered_odkazy = [
                odkaz for odkaz in odkazy_dict[dropdown_section] 
                if search_term.lower() in odkaz["nazev"].lower()
            ]
        
        if filtered_odkazy:
            # Zobrazení jako tabulka s lepším formátováním
            for i, odkaz in enumerate(filtered_odkazy, 1):
                with st.container():
                    col1, col2 = st.columns([4, 1])
                    
                    with col1:
                        # Funkční odkaz s číslem
                        st.markdown(f"**{i}.** [{odkaz['nazev']}]({odkaz['url']})")
                        if odkaz['datum']:
                            st.caption(f"📅 Použito: {odkaz['datum']}")
                    
                    with col2:
                        # Tlačítko pro kopírování URL
                        if st.button("📋", key=f"copy_{dropdown_section}_{i}", help="Kopírovat odkaz"):
                            st.write(f"URL: `{odkaz['url']}`")
                    
                    st.divider()
        else:
            st.info(f"Žádné odkazy neodpovídají vyhledávání '{search_term}'")
    else:
        st.info("V této sekci nejsou žádné odkazy.")

    # Statistiky
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📊 Celkem odkazů", sum(len(odkazy) for odkazy in odkazy_dict.values()))
    with col2:
        st.metric("🔬 Pruzkum", len(odkazy_dict.get("Pruzkum", [])))
    with col3:
        st.metric("🤖 AI Agenti", len(odkazy_dict.get("AI Agenti", [])))
    with col4:
        st.metric("🏨 Imperial", len(odkazy_dict.get("Imperial Pruzkum", [])))

    # New statistics section
    st.markdown("---")
    st.markdown("## 📊 Statistika")
    st.markdown("### Přehled odkazů podle kategorií")
    
    # Calculate statistics
    total_links = sum(len(odkazy) for odkazy in odkazy_dict.values())
    pruzkum_count = len(odkazy_dict.get("Pruzkum", []))
    ai_count = len(odkazy_dict.get("AI Agenti", []))
    imperial_count = len(odkazy_dict.get("Imperial Pruzkum", []))
    
    # Display statistics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Celkový počet odkazů", total_links)
    with col2:
        st.metric("Odkazy v kategorii Průzkum", pruzkum_count)
    with col3:
        st.metric("Odkazy v kategorii AI", ai_count)
        
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Odkazy v kategorii Imperial", imperial_count)

    # Export možnosti
    st.markdown("---")
    st.markdown("### 📤 Export odkazů")
    
    export_format = st.selectbox(
        "Vyberte formát exportu:",
        ["Markdown", "CSV", "JSON"],
        key="export_format"
    )
    
    if st.button("⬇️ Stáhnout odkazy", key="download_odkazy"):
        if export_format == "Markdown":
            export_content = "# Odkazy z průzkumu\n\n"
            for section, odkazy in odkazy_dict.items():
                if odkazy:
                    export_content += f"## {section}\n\n"
                    for i, odkaz in enumerate(odkazy, 1):
                        export_content += f"{i}. [{odkaz['nazev']}]({odkaz['url']})\n"
                        if odkaz['datum']:
                            export_content += f"   - Použito: {odkaz['datum']}\n"
                    export_content += "\n"
            
            st.download_button(
                label="📄 Stáhnout jako Markdown",
                data=export_content,
                file_name="odkazy_pruzkum.md",
                mime="text/markdown"
            )
        
        elif export_format == "CSV":
            import pandas as pd
            
            rows = []
            for section, odkazy in odkazy_dict.items():
                for odkaz in odkazy:
                    rows.append({
                        "Sekce": section,
                        "Název": odkaz['nazev'],
                        "URL": odkaz['url'],
                        "Datum": odkaz['datum']
                    })
            
            if rows:
                df = pd.DataFrame(rows)
                csv = df.to_csv(index=False, encoding='utf-8')
                st.download_button(
                    label="📊 Stáhnout jako CSV",
                    data=csv,
                    file_name="odkazy_pruzkum.csv",
                    mime="text/csv"
                )
        
        elif export_format == "JSON":
            import json
            json_data = json.dumps(odkazy_dict, ensure_ascii=False, indent=2)
            st.download_button(
                label="🔧 Stáhnout jako JSON",
                data=json_data,
                file_name="odkazy_pruzkum.json",
                mime="application/json"
            )

elif view_mode == "🤖 AI Agenti":
    st.markdown("## 🤖 AI Agenti")
    try:
        with open("ai_agenty.md", "r", encoding="utf-8") as file:
            st.markdown(file.read())
    except FileNotFoundError:
        st.warning("Soubor ai_agenty.md nebyl nalezen.")

# Ostatní view módy můžete přidat podobně...

# Footer
st.markdown("---")
st.markdown("""
<div class="footer">
    <h3>🏨 AI Orchestrator Hotel Management System</h3>
    <p>Vytvořeno pro maximální efektivitu hotelového managementu</p>
    <p><em>Powered by AI • Vyvořil Martin Švanda • Praut s.r.o.</em></p>
    <p><strong>🚀 ROI: 143% za první rok | Payback: 7.4 měsíců</strong></p>
</div>
""", unsafe_allow_html=True)
