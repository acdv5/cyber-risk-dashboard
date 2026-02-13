import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Configuration de la page
st.set_page_config(
    page_title="Cyber Risk Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# CSS personnalisé
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .metric-container {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🛡️ Analyseur risques cyber</h1>', unsafe_allow_html=True)
st.markdown("**Calcul de l'ALE (Annual Loss Expectancy) et du ROI des mesures de sécurité**")
st.markdown("---")

# Tabs pour organiser le contenu
tab1, tab2, tab3, tab4 = st.tabs(["📊 Analyse d'un Risque", "💰 ROI des Mesures", "📈 Multi-Risques", "ℹ️ Méthodologie"])

# ============================================
# TAB 1 : ANALYSE D'UN RISQUE UNIQUE
# ============================================
with tab1:
    st.header("Analyse d'un Risque Cyber")
    
    col_input, col_results = st.columns([1, 1])
    
    with col_input:
        st.subheader("Paramètres du Risque")
        
        # Sélection du type de risque (avec exemples pré-configurés)
        risk_type = st.selectbox(
            "Type de risque",
            ["Personnalisé", "Ransomware", "Fuite de données", "DDoS", "Phishing", "Panne système"]
        )
        
        # Pré-remplissage selon le type de risque
        if risk_type == "Ransomware":
            default_name = "Attaque Ransomware sur serveur de production"
            default_value = 500000
            default_prob = 15
            default_impact = 80
        elif risk_type == "Fuite de données":
            default_name = "Fuite de données clients (RGPD)"
            default_value = 300000
            default_prob = 10
            default_impact = 70
        elif risk_type == "DDoS":
            default_name = "Attaque DDoS sur site e-commerce"
            default_value = 200000
            default_prob = 20
            default_impact = 60
        elif risk_type == "Phishing":
            default_name = "Campagne de phishing ciblée"
            default_value = 100000
            default_prob = 30
            default_impact = 50
        elif risk_type == "Panne système":
            default_name = "Panne système critique"
            default_value = 400000
            default_prob = 12
            default_impact = 75
        else:
            default_name = "Mon risque personnalisé"
            default_value = 100000
            default_prob = 10
            default_impact = 50
        
        asset_name = st.text_input("Nom de l'actif / scénario", default_name)
        asset_value = st.number_input("Valeur de l'actif (€)", 0, 10000000, default_value, step=10000, 
                                     help="Valeur de l'actif ou coût estimé de l'incident")
        
        probability = st.slider("Probabilité annuelle (%)", 0, 100, default_prob,
                               help="Probabilité que le risque se réalise dans l'année")
        
        impact_factor = st.slider("Facteur d'impact (%)", 0, 100, default_impact,
                                 help="Pourcentage de la valeur de l'actif affecté")
        
        st.info("💡 **Astuce** : Utilisez les exemples pré-configurés ou personnalisez vos valeurs")
    
    with col_results:
        st.subheader("📊 Résultats de l'Analyse")
        
        # Calculs
        sle = asset_value * (impact_factor / 100)
        aro = probability / 100
        ale = sle * aro
        
        # Affichage des métriques
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "SLE", 
                f"{sle:,.0f} €",
                help="Single Loss Expectancy : Perte estimée par incident"
            )
        
        with col2:
            st.metric(
                "ARO", 
                f"{aro:.2f}",
                help="Annual Rate of Occurrence : Fréquence annuelle attendue"
            )
        
        with col3:
            st.metric(
                "ALE", 
                f"{ale:,.0f} €",
                help="Annual Loss Expectancy : Perte annuelle attendue"
            )
        
        #Niveau de risque
        if ale > 100000:
            risk_level = "🔴 CRITIQUE"
            risk_color = "red"
        elif ale > 50000:
            risk_level = "🟠 ÉLEVÉ"
            risk_color = "orange"
        elif ale > 20000:
            risk_level = "🟡 MOYEN"
            risk_color = "gold"
        else:
            risk_level = "🟢 FAIBLE"
            risk_color = "green"
        
        st.markdown(f"### Niveau de risque : {risk_level}")
        
        # Graphique de décomposition
        st.markdown("#### Décomposition du risque")
        fig_breakdown = go.Figure(data=[
            go.Bar(
                x=['Valeur de l\'actif', 'SLE (avec impact)', 'ALE (avec probabilité)'],
                y=[asset_value, sle, ale],
                marker_color=['lightblue', 'orange', risk_color],
                text=[f"{asset_value:,.0f} €", f"{sle:,.0f} €", f"{ale:,.0f} €"],
                textposition='auto',
            )
        ])
        fig_breakdown.update_layout(
            title="Évolution du risque",
            yaxis_title="Montant (€)",
            showlegend=False,
            height=400
        )
        st.plotly_chart(fig_breakdown, use_container_width=True)

# ============================================
# TAB2 : ROI DES MESURES DE SÉCURITÉ
# ============================================
with tab2:
    st.header("💰 Calcul du ROI des Mesures de Sécurité")
    
    col_measure, col_roi = st.columns([1, 1])
    
    with col_measure:
        st.subheader("🛠️ Paramètres de la Mesure")
        
        # Rappel du risque actuel
        st.info(f"**Risque actuel analysé** : {asset_name}")
        st.metric("ALE avant mesure", f"{ale:,.0f} €")
        
        # Type de mesure
        measure_type = st.selectbox(
            "Type de mesure de sécurité",
            ["Personnalisée", "EDR/XDR", "Formation utilisateurs", "Firewall nouvelle génération", 
             "Solution de backup", "SIEM", "Audit de sécurité", "Pentesting"]
        )
        
        #Préremplissage selon le type de mesure
        if measure_type == "EDR/XDR":
            default_cost = 15000
            default_reduction = 70
        elif measure_type == "Formation utilisateurs":
            default_cost = 5000
            default_reduction = 40
        elif measure_type == "Firewall nouvelle génération":
            default_cost = 20000
            default_reduction = 60
        elif measure_type == "Solution de backup":
            default_cost = 8000
            default_reduction = 50
        elif measure_type == "SIEM":
            default_cost = 25000
            default_reduction = 55
        elif measure_type == "Audit de sécurité":
            default_cost = 12000
            default_reduction = 35
        elif measure_type == "Pentesting":
            default_cost = 10000
            default_reduction = 30
        else:
            default_cost = 10000
            default_reduction = 50
        
        control_cost = st.number_input(
            "Coût annuel de la mesure (€)", 
            0, 500000, default_cost, step=1000,
            help="Coût d'implémentation + maintenance annuelle"
        )
        
        risk_reduction = st.slider(
            "Réduction du risque (%)", 
            0, 100, default_reduction,
            help="De combien la mesure réduit-elle la probabilité d'occurrence ?"
        )
        
        new_probability = probability * (1 - risk_reduction / 100)
        
        st.info(f"📉 Nouvelle probabilité après mesure : **{new_probability:.1f}%** (au lieu de {probability}%)")
    
    with col_roi:
        st.subheader("📈 Résultats du ROI")
        
        # Calculs ROI
        new_ale = sle * (new_probability / 100)
        risk_reduction_value = ale - new_ale
        net_benefit = risk_reduction_value - control_cost
        roi = (net_benefit / control_cost) * 100 if control_cost > 0 else 0
        payback_period = control_cost / risk_reduction_value if risk_reduction_value > 0 else float('inf')
        
        # Métriques principales
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(
                "Nouvelle ALE", 
                f"{new_ale:,.0f} €",
                delta=f"-{((ale-new_ale)/ale*100):.0f}%" if ale > 0 else "0%",
                delta_color="inverse"
            )
        
        with col2:
            st.metric(
                "Réduction du risque", 
                f"{risk_reduction_value:,.0f} €/an"
            )
        
        col3, col4 = st.columns(2)
        
        with col3:
            st.metric(
                "Bénéfice net", 
                f"{net_benefit:,.0f} €/an",
                delta="Rentable ✅" if net_benefit > 0 else "Non rentable ❌"
            )
        
        with col4:
            st.metric(
                "ROI", 
                f"{roi:.0f}%",
                help="Return On Investment : (Gain - Coût) / Coût × 100"
            )
        
        # Période de retour sur investissement
        if payback_period < float('inf'):
            st.success(f"⏱️ **Période de retour sur investissement** : {payback_period:.1f} ans")
        else:
            st.error("⏱️ **Période de retour sur investissement** : Mesure non rentable")
        
        # Graphique comparatif avant/après
        st.markdown("#### Comparaison Avant / Après")
        fig_comparison = go.Figure(data=[
            go.Bar(
                name='Avant mesure',
                x=['ALE', 'Coût mesure', 'Total'],
                y=[ale, 0, ale],
                marker_color='red',
                text=[f"{ale:,.0f} €", "0 €", f"{ale:,.0f} €"],
                textposition='auto'
            ),
            go.Bar(
                name='Après mesure',
                x=['ALE', 'Coût mesure', 'Total'],
                y=[new_ale, control_cost, new_ale + control_cost],
                marker_color=['green', 'orange', 'purple'],
                text=[f"{new_ale:,.0f} €", f"{control_cost:,.0f} €", f"{new_ale + control_cost:,.0f} €"],
                textposition='auto'
            )
        ])
        fig_comparison.update_layout(
            barmode='group',
            title="Coût total du risque (ALE + Mesure)",
            yaxis_title="Montant (€)",
            height=400
        )
        st.plotly_chart(fig_comparison, use_container_width=True)
        
        # Recommandation
        if roi > 100:
            st.success(f"✅ **Recommandation** : Mesure **fortement recommandée** (ROI de {roi:.0f}%)")
        elif roi > 0:
            st.info(f"✅ **Recommandation** : Mesure **rentable** (ROI de {roi:.0f}%)")
        else:
            st.warning(f"⚠️ **Recommandation** : Mesure **non rentable** (ROI négatif de {roi:.0f}%)")

# ============================================
# TAB 3 : GESTION MULTI-RISQUES
# ============================================
with tab3:
    st.header("📈 Gestion de Plusieurs Risques")
    st.markdown("Gérez et priorisez plusieurs risques simultanément")
    
    # Initialiser la session state pour stocker les risques
    if 'risks_list' not in st.session_state:
        st.session_state.risks_list = [
            {"name": "Ransomware", "ale": 60000, "probability": 15, "impact": 400000},
            {"name": "Fuite de données", "ale": 21000, "probability": 10, "impact": 300000},
            {"name": "DDoS", "ale": 24000, "probability": 20, "impact": 200000},
        ]
    
    # Ajouter un nouveau risque
    with st.expander("➕ Ajouter un nouveau risque"):
        new_risk_name = st.text_input("Nom du risque", key="new_risk")
        col_a, col_b = st.columns(2)
        with col_a:
            new_prob = st.number_input("Probabilité (%)", 0, 100, 10, key="new_prob")
        with col_b:
            new_impact = st.number_input("Impact (€)", 0, 10000000, 100000, step=10000, key="new_impact")
        
        if st.button("Ajouter ce risque"):
            new_ale = (new_impact * (new_prob / 100))
            st.session_state.risks_list.append({
                "name": new_risk_name,
                "ale": new_ale,
                "probability": new_prob,
                "impact": new_impact
            })
            st.success(f"✅ Risque '{new_risk_name}' ajouté !")
            st.rerun()
    
    # Affichage du tableau des risques
    if st.session_state.risks_list:
        df_risks = pd.DataFrame(st.session_state.risks_list)
        df_risks = df_risks.sort_values('ale', ascending=False).reset_index(drop=True)
        
        #Tableau formaté
        st.subheader("📋 Liste des Risques (par ordre de criticité)")
        
        #Formater pour l'affichage
        df_display = df_risks.copy()
        df_display['ale'] = df_display['ale'].apply(lambda x: f"{x:,.0f} €")
        df_display['probability'] = df_display['probability'].apply(lambda x: f"{x}%")
        df_display['impact'] = df_display['impact'].apply(lambda x: f"{x:,.0f} €")
        df_display.columns = ['Risque', 'ALE', 'Probabilité', 'Impact']
        
        st.dataframe(df_display, use_container_width=True, hide_index=True)
        
        # Graphiques
        col_chart1, col_chart2 = st.columns(2)
        
        with col_chart1:
            # Top risques par ALE
            fig_top = px.bar(
                df_risks.head(10),
                x='ale',
                y='name',
                orientation='h',
                title='Top 10 des Risques par ALE',
                labels={'ale': 'ALE (€)', 'name': 'Risque'},
                color='ale',
                color_continuous_scale='Reds'
            )
            st.plotly_chart(fig_top, use_container_width=True)
        
        with col_chart2:
            # Matrice de risques
            fig_matrix = px.scatter(
                df_risks,
                x='probability',
                y='impact',
                size='ale',
                color='ale',
                hover_name='name',
                title='Matrice de Risques (Impact vs Probabilité)',
                labels={'probability': 'Probabilité (%)', 'impact': 'Impact (€)'},
                color_continuous_scale='RdYlGn_r',
                size_max=60
            )
            
            # Lignes de seuil
            fig_matrix.add_hline(y=df_risks['impact'].median(), line_dash="dash", line_color="gray", opacity=0.5)
            fig_matrix.add_vline(x=df_risks['probability'].median(), line_dash="dash", line_color="gray", opacity=0.5)
            
            st.plotly_chart(fig_matrix, use_container_width=True)
        
        # KPIs globaux
        st.subheader("📊 KPIs Globaux")
        col1, col2, col3, col4 = st.columns(4)
        
        total_ale = df_risks['ale'].sum()
        avg_ale = df_risks['ale'].mean()
        max_risk = df_risks.loc[df_risks['ale'].idxmax()]
        critical_risks = len(df_risks[df_risks['ale'] > 50000])
        
        col1.metric("ALE Total", f"{total_ale:,.0f} €")
        col2.metric("ALE Moyen", f"{avg_ale:,.0f} €")
        col3.metric("Risque Max", f"{max_risk['name']}", f"{max_risk['ale']:,.0f} €")
        col4.metric("Risques Critiques", critical_risks, f"ALE > 50k€")
        
        # Bouton pour réinitialiser
        if st.button("🗑️ Réinitialiser la liste des risques"):
            st.session_state.risks_list = []
            st.rerun()
    else:
        st.info("📝 Aucun risque enregistré. Ajoutez-en un ci-dessus !")

# ============================================
# TAB 4 : MÉTHODOLOGIE
# ============================================
with tab4:
    st.header("ℹ️ Méthodologie et Formules")
    
    st.markdown("""
    ### Concepts Clés
    
    #### ALE (Annual Loss Expectancy)
    L'**ALE** représente la perte financière annuelle attendue pour un risque donné.
    
    **Formule :**
    ```
    ALE = SLE × ARO
    ```
    
    Où :
    - **SLE** (Single Loss Expectancy) = Perte estimée par incident
    - **ARO** (Annual Rate of Occurrence) = Fréquence annuelle du risque
    
    #### SLE (Single Loss Expectancy)
    **Formule :**
    ```
    SLE = Valeur de l'actif × Facteur d'exposition
    ```
    
    #### ROI (Return On Investment)
    Le **ROI** mesure la rentabilité d'une mesure de sécurité.
    
    **Formule :**
    ```
    ROI = ((Réduction du risque - Coût de la mesure) / Coût de la mesure) × 100
    ```
    
    ---
    
    ### 📊 Niveaux de Risque
    
    | ALE | Niveau | Action recommandée |
    |-----|--------|-------------------|
    | > 100 000€ | 🔴 **CRITIQUE** | Action immédiate requise |
    | 50 000€ - 100 000€ | 🟠 **ÉLEVÉ** | Prioriser dans le plan d'action |
    | 20 000€ - 50 000€ | 🟡 **MOYEN** | Surveiller et planifier |
    | < 20 000€ | 🟢 **FAIBLE** | Accepter ou transférer |
    
    ---
    
    ### Interprétation du ROI
    
    - **ROI > 100%** : Investissement **très rentable** ✅
    - **ROI entre 0% et 100%** : Investissement **rentable** ✅
    - **ROI < 0%** : Investissement **non rentable** ❌
    
    ---
    
    ### Références
    
    - **ISO/IEC 27005** : Gestion des risques en sécurité de l'information
    - **NIST SP 800-30** : Guide for Conducting Risk Assessments
    - **EBIOS Risk Manager** : Méthode française d'analyse des risques
    - **FAIR** (Factor Analysis of Information Risk)
    
    ---
    
    ### À propos
    
    **Dashboard développé par** : Arnaud Champierre de Villeneuve
    
    **Technologies** : Python, Streamlit, Plotly
    
    **Contact** : arnauddvpro@gmail.com
    
    ---
    
    *Ce dashboard est un outil d'aide à la décision. Les valeurs doivent être ajustées selon votre contexte spécifique.*
    """)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
        <p>🛡️ Cyber Risk Dashboard v1.0 | Développé avec Streamlit | 
        <a href='https://github.com/acdv5/cyber-risk-dashboard' target='_blank'>Code source sur GitHub</a>
        </p>
    </div>
    """, 
    unsafe_allow_html=True
)
