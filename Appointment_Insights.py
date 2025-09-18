import streamlit as st
import pandas as pd

# Set page config for wide layout
st.set_page_config(
    page_title="Sales & Business Appointment Insights", 
    layout="wide",
    page_icon="📊",
    initial_sidebar_state="expanded"
)

# =========================
# Custom CSS Styling
# =========================
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.8rem;
        color: #2c3e50;
        border-bottom: 2px solid #3498db;
        padding-bottom: 0.3rem;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    .product-card {
        background-color: #f8f9fa;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #3498db;
    }
    .metric-card {
        background-color: #e8f4fc;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .insight-card {
        background-color: #fff4e6;
        border-radius: 10px;
        padding: 1.2rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #ffa94d;
    }
    .manager-card {
        background-color: #e6f7ff;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .customer-list {
        background-color: #f0f7ff;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
    }
    .highlight {
        background-color: #fffacd;
        padding: 0.2rem 0.4rem;
        border-radius: 4px;
        font-weight: bold;
    }
    .bullet-point {
        margin-left: 1.5rem;
        padding-left: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# =========================
# Data
# =========================

# Yearly Summary Table
yearly_summary_table = [
    {"Product": "Lutemax 2020",
     "Key Customers/Partners": "Herbalife, P&G, Church & Dwight, Lang Pharma, Danone, Nutricost, Nutritunes, NutraQ, Nutrafol, NutraCap Labs",
     "Application/Format": "Gummies, multivitamins, oral strips, cognition",
     "Sales Insight / Trend": "Replacing FloraGLO, focus on cognition, children's health, repeat orders, new launches"},
    {"Product": "Lutemax Kids",
     "Key Customers/Partners": "Herbalife, Danone, Nutricharge, Nutritunes, NutraQ, Nutrafol, NutraCap Labs",
     "Application/Format": "Gummies, multivitamins, oral strips",
     "Sales Insight / Trend": "Strong growth in children's health, new launches, pilot batches, stability focus"},
    {"Product": "EnXtra",
     "Key Customers/Partners": "Herbalife, P&G, USV India, Plix, Zoeuticals, Tabs Labs, A Plus Nutrition Lab, MacroCap Labs",
     "Application/Format": "Energy, cognition, hydration, protein bars, stick packs, oral strips, chewing gum",
     "Sales Insight / Trend": "Caffeine alternative/amplifier, repeat orders, new launches, innovative formats"},
    {"Product": "Sleeproot",
     "Key Customers/Partners": "MegaFood, New Chapter, Nature's Bounty, Pharmavite, P&G, Rasi Labs, Nutrafol, NutraCap Labs",
     "Application/Format": "Sleep support, gummies, capsules, lozenges, liquid fills",
     "Sales Insight / Trend": "Melatonin-free, day 1 benefit, strong interest from major brands, new launches"},
    {"Product": "CurcuWIN Ultra+",
     "Key Customers/Partners": "Qunol, Pharmavite, Rasi Labs, Vitaquest, NutraCap Labs, Vivaldis",
     "Application/Format": "Joint health, anti-inflammatory, menopause, pet health, RTM, gummies",
     "Sales Insight / Trend": "Fast-acting joint comfort, replacing Wacker/Tamaflex, aggressive pricing, pet health"},
    {"Product": "Capsimax",
     "Key Customers/Partners": "Pharmavite, Vitaquest, NutraCap Labs, MacroCap Labs, 3S-ProSsups",
     "Application/Format": "Weight management, energy, pre-workout, RTM, gummies",
     "Sales Insight / Trend": "New compliance (Capsimax Next), stick packs, capsules, beverages, price-sensitive"},
    {"Product": "Zenroot",
     "Key Customers/Partners": "Nutrafol, PetIQ, Vitaquest, MacroCap Labs",
     "Application/Format": "Stress, women's health, pet health",
     "Sales Insight / Trend": "Ashwagandha alternative, regulatory advantage, new launches"}
]

yearly_actionable_insights = [
    "Focus on children's health, cognition, and sleep for new product development and marketing.",
    "Leverage science-backed claims and fast-acting benefits to differentiate from competitors.",
    "Support customers with technical, regulatory, and supply chain solutions to address stability, compliance, and cost challenges.",
    "Monitor and nurture relationships with key CMOs and brand partners to ensure repeat business and early adoption of new ingredients."
]

# Complete Yearly Sales Breakdown with all 13 products
yearly_sales_breakdown = [
    {"Product": "ENXTRA",
     "Number of Appointments": 10,
     "Key Customers": ["Herbalife (EnXtra - H24 Lift-off Hydration)", "MacroCap Labs", "Tabs Labs", "Zoeuticals", "Plix",
                       "USV India (Protein Bar)", "Benefic", "Nutrition Formulators, Inc.", "Amare Global",
                       "Others (various NPD and innovation sessions)"],
     "Sales Notes": ["EnXtra is being widely adopted in energy, cognition, hydration, and functional food/beverage projects.",
                     "Used in stick packs, protein bars, oral strips, chewing gum, and as a caffeine alternative/amplifier.",
                     "Repeat orders and new launches in India, US, and Asia.",
                     "Focus on innovative delivery formats and partnerships with both established and emerging brands."]},
    {"Product": "LUTEMAX 2020",
     "Number of Appointments": 9,
     "Key Customers": ["Biovation Labs LLC", "Lang Pharma Nutrition", "Danone", "Nutricharge", "Signutra",
                       "Dr. Reddy's", "Viteyes (Vitamin Health, Inc.)", "Herbalife (Kids Gummies)",
                       "Others (multivitamin and cognition projects)"],
     "Sales Notes": ["Lutemax 2020 is a flagship for eye health, cognition, and children's health.",
                     "Focus on replacing FloraGLO, with launches in gummies, multivitamins, and oral strips.",
                     "Stability and efficacy are key selling points.",
                     "Multiple pilot batches and new launches in the US, India, and Asia."]},
    {"Product": "SLEEPROOT",
     "Number of Appointments": 3,
     "Key Customers": ["New Chapter", "Proctor & Gamble", "Rasi Laboratories"],
     "Sales Notes": ["Sleeproot is being adopted as a melatonin-free sleep solution.",
                     "Highlighted for its 'Day 1 benefit' and improved organoleptics over traditional valerian.",
                     "Launches in capsules, gummies, and liquid fills.",
                     "Interest from major supplement brands for 2025–2026 launches."]},
    {"Product": "MUVZ",
     "Number of Appointments": 5,
     "Key Customers": ["Rasi Laboratories", "USV India (Protein Bar)", "MacroCap Labs", "Vitaquest International, LLC"],
     "Sales Notes": ["Muvz is being positioned for joint health and active ageing.",
                     "Used in combination with other joint health ingredients.",
                     "Noted for its fast-acting benefits and as an alternative to glucosamine/collagen."]},
    {"Product": "CAPSIMAX",
     "Number of Appointments": 4,
     "Key Customers": ["Amare Global", "Benefic", "Nutrition Formulators, Inc.", "MacroCap Labs"],
     "Sales Notes": ["Capsimax Next is being promoted for improved compliance and cost-in-use.",
                     "Used in weight management, energy, pre-workout, and RTM (ready-to-mix) products.",
                     "Focus on stick packs, capsules, and beverages."]},
    {"Product": "ZENROOT",
     "Number of Appointments": 4,
     "Key Customers": ["MacroCap Labs", "Nutrition Formulators, Inc.", "Vitaquest International, LLC", "PetIQ"],
     "Sales Notes": ["Zenroot is positioned as an ashwagandha alternative, especially for regulatory-challenged markets.",
                     "Interest in women's health and pet health.",
                     "New launches and pilot projects in 2025."]},
    {"Product": "GREEN TEA",
     "Number of Appointments": 2,
     "Key Customers": ["Flavor Materials"],
     "Sales Notes": ["Used in beverage and supplement projects.",
                     "Focus on supply chain and product equivalence."]},
    {"Product": "CURCUWIN",
     "Number of Appointments": 1,
     "Key Customers": ["Haleon"],
     "Sales Notes": ["CurcuWIN Ultra+ is being positioned for joint health and fast-acting benefits.",
                     "Compared to Tamaflex and other turmeric-based joint health products."]},
    {"Product": "CAFFEINE",
     "Number of Appointments": 1,
     "Key Customers": ["Prinova Nutrition LLC"],
     "Sales Notes": ["Focus on natural caffeine supply and compliance."]},
    {"Product": "GINGEVER",
     "Number of Appointments": 1,
     "Key Customers": ["Dynamic Nutraceuticals"],
     "Sales Notes": ["Used in supplement and functional food projects."]},
    {"Product": "TURMERIC",
     "Number of Appointments": 1,
     "Key Customers": ["MK Marketing, LLC (Qunol)"],
     "Sales Notes": ["Qunol & OmniActive Turmeric Supply Chain Integration.",
                     "Focus on vertical integration, cost control, and supply security."]},
    {"Product": "BLACK TEA",
     "Number of Appointments": 1,
     "Key Customers": ["Herbalife (Orange Pekoe)"],
     "Sales Notes": ["Product equivalence and supply chain focus."]},
    {"Product": "GREEN COFFEE",
     "Number of Appointments": 1,
     "Key Customers": ["Not specified"],
     "Sales Notes": ["Strategic focus."]}
]

yearly_total_appointments = [
    {"Sales Manager": "Kayla Samson", "Total Appointments": 21},
    {"Sales Manager": "Jen BETHEA", "Total Appointments": 20},
    {"Sales Manager": "Mayank Agrawal", "Total Appointments": 13},
    {"Sales Manager": "Kratika Gupta", "Total Appointments": 10},
    {"Sales Manager": "Dinesh Venkateswaran", "Total Appointments": 9},
    {"Sales Manager": "Parth Shah", "Total Appointments": 25},
    {"Sales Manager": "Nitesh Devadiga", "Total Appointments": 2},
    {"Sales Manager": "Gracey Matlosz", "Total Appointments": 1},
    {"Sales Manager": "Chelsea Simpkins", "Total Appointments": 1},
    {"Sales Manager": "Vishal Agrawal", "Total Appointments": 1},
    {"Sales Manager": "Sayantan Bhattacharya", "Total Appointments": 1},
    {"Sales Manager": "Michael Falso", "Total Appointments": 1},
    {"Sales Manager": "Omkar Sohoni", "Total Appointments": 1}
]

# Last 3 Months Data
last_3_months_data = [
    {"Product": "Curcuwin Ultra+", "Number of Appointments": 2,
     "Key Customers": ["The J.M. Smucker Company", "Qunol(MK Marketing, LLC)"],
     "Sales Notes": ["JMS completed caffeine mitigation research; pilot with Curcuwin Ultra+; results inconclusive but opportunity for functional coffee.",
                     "Qunol & OmniActive Turmeric Supply Chain Integration: vertical integration, cost control, supply security."]},
    {"Product": "Enxtra", "Number of Appointments": 1,
     "Key Customers": ["The J.M. Smucker Company"],
     "Sales Notes": ["Opportunity in 'beanless coffee' and functional beverages; focus on caffeine-free energy."]},
    {"Product": "Muvz", "Number of Appointments": 1,
     "Key Customers": ["Rasi Laboratories"],
     "Sales Notes": ["Rasi awarded new Pharmavite formulas; Muvz included in 3-in-1 joint formula. Handling and processing instructions discussed."]},
    {"Product": "Capsimax Next", "Number of Appointments": 1,
     "Key Customers": ["Vitaquest International, LLC"],
     "Sales Notes": ["Compliance and new launches in weight management and energy."]},
    {"Product": "CAPSIMAX", "Number of Appointments": 1,
     "Key Customers": ["Amare Global"],
     "Sales Notes": ["Ongoing interest in weight management and energy products."]},
    {"Product": "CU+", "Number of Appointments": 1,
     "Key Customers": ["New Chapter"],
     "Sales Notes": ["Recommended by P&G for new launches; focus on women's health and joint support."]},
    {"Product": "Lutemax 2020", "Number of Appointments": 1,
     "Key Customers": ["Lutemax2020 multivitamin (project)"],
     "Sales Notes": ["Multivitamin project with stability testing; potential for Lutemax2020 inclusion pending results."]},
    {"Product": "Lutemax Lutein", "Number of Appointments": 1,
     "Key Customers": ["New Chapter"],
     "Sales Notes": ["Interest in eye health product; hexane-free requirement for acceptance."]},
    {"Product": "Blink Nutritears", "Number of Appointments": 1,
     "Key Customers": ["Bausch + Lomb (Dan Stein, Carina Grassman, Andreas)"],
     "Sales Notes": ["Nutritears expansion in EU; pilot batch for gummies; focus on dry eye claims and stability."]},
    {"Product": "GINGEVER", "Number of Appointments": 1,
     "Key Customers": ["Dynamic Nutraceuticals"],
     "Sales Notes": ["Used in supplement and functional food projects."]}
]

last_3_months_total = [
    {"Sales Manager": "Kayla Samson", "Total Appointments": 18},
    {"Sales Manager": "Parth Shah", "Total Appointments": 7},
    {"Sales Manager": "Dinesh Venkateswaran", "Total Appointments": 5},
    {"Sales Manager": "Jen BETHEA", "Total Appointments": 4},
    {"Sales Manager": "Vishal Agrawal", "Total Appointments": 1},
    {"Sales Manager": "Omkar Sohoni", "Total Appointments": 1},
    {"Sales Manager": "Michael Falso", "Total Appointments": 1}
]

# Last Week Data
last_week_data = [
    {"Product": "(No product data found for last week)",
     "Number of Appointments": 0,
     "Key Customers": ["–"],
     "Sales Notes": ["–"]}
]

last_week_total = [{"Sales Manager": "-", "Total Appointments": 0}]

# =========================
# Page Header
# =========================
st.markdown("<h1 class='main-header'>📊 Appointment Insights Dashboard</h1>", unsafe_allow_html=True)
st.markdown("***")

# =========================
# Sidebar: Timeframe Selection
# =========================
with st.sidebar:
    st.markdown("### ⏰ Timeframe Selection")
    timeframe = st.radio(
        "Select Timeframe:",
        ["Yearly", "Last 3 Months", "Last Week"],
        index=0
    )
    
    st.markdown("***")
    st.markdown("### 📈 Quick Stats")
    
    if timeframe == "Yearly":
        total_appts = sum(item["Total Appointments"] for item in yearly_total_appointments)
        st.metric("Total Appointments", total_appts)
        st.metric("Products Tracked", len(yearly_sales_breakdown))
        st.metric("Sales Managers", len(yearly_total_appointments))
    elif timeframe == "Last 3 Months":
        total_appts = sum(item["Total Appointments"] for item in last_3_months_total)
        st.metric("Total Appointments", total_appts)
        st.metric("Products Tracked", len(last_3_months_data))
        st.metric("Sales Managers", len(last_3_months_total))
    else:
        st.metric("Total Appointments", 0)
        st.metric("Products Tracked", 0)
        st.metric("Sales Managers", 0)

# =========================
# Display Functions
# =========================
def display_yearly_insights():
    st.markdown("<h2 class='sub-header'>Yearly Insights (April 2025 Onwards)</h2>", unsafe_allow_html=True)
    
    # Summary Table
    st.markdown("#### 📋 Product Summary")
    summary_df = pd.DataFrame(yearly_summary_table)
    st.dataframe(summary_df, use_container_width=True)
    
    # Actionable Insights
    st.markdown("#### 💡 Actionable Insights")
    for insight in yearly_actionable_insights:
        st.markdown(f"<div class='insight-card'>• {insight}</div>", unsafe_allow_html=True)
    
    # Sales Breakdown
    st.markdown("#### 📊 Detailed Sales Breakdown by Product")
    
    # Create tabs for better organization of the 13 products
    tab_names = [f"{product['Product']} ({product['Number of Appointments']})" for product in yearly_sales_breakdown]
    tabs = st.tabs(tab_names)
    
    for i, tab in enumerate(tabs):
        with tab:
            product = yearly_sales_breakdown[i]
            st.markdown(f"<div class='product-card'>", unsafe_allow_html=True)
            
            st.markdown(f"##### {product['Product']} <span style='color: #1f77b4;'>({product['Number of Appointments']} appointments)</span>", unsafe_allow_html=True)
            
            st.markdown("**Key Customers/Companies:**")
            st.markdown("<div class='customer-list'>", unsafe_allow_html=True)
            for cust in product["Key Customers"]:
                st.markdown(f"<div class='bullet-point'>• {cust}</div>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.markdown("**Sales/Business Notes:**")
            for note in product["Sales Notes"]:
                st.markdown(f"<div class='bullet-point'>• {note}</div>", unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)
    
    # Sales Manager Performance
    st.markdown("#### 👥 Total Appointments by Sales Manager")
    manager_df = pd.DataFrame(yearly_total_appointments)
    st.dataframe(manager_df, use_container_width=True)
    
    # Visual representation
    col1, col2, col3 = st.columns(3)
    with col1:
        top_performer = max(yearly_total_appointments, key=lambda x: x['Total Appointments'])
        st.metric("Top Performer", f"{top_performer['Sales Manager']} ({top_performer['Total Appointments']})")
    with col2:
        avg_appointments = sum(item['Total Appointments'] for item in yearly_total_appointments) / len(yearly_total_appointments)
        st.metric("Average Appointments", f"{avg_appointments:.1f}")
    with col3:
        total_appts = sum(item['Total Appointments'] for item in yearly_total_appointments)
        st.metric("Total Appointments", total_appts)

def display_3month_insights():
    st.markdown("<h2 class='sub-header'>Last 3 Months Insights (from 18 June 2025)</h2>", unsafe_allow_html=True)
    
    # Actionable Insights
    last_3_months_insights = [
        "Curcuwin Ultra+ and Enxtra are being positioned for innovation in functional beverages, especially as caffeine alternatives or enhancers.",
        "Muvz is gaining traction in joint health, with new launches in combination formulas.",
        "Capsimax Next and CAPSIMAX continue to be relevant for weight management and energy, with compliance and new product launches.",
        "Lutemax 2020 and Lutemax Lutein are being considered for new multivitamin and eye health products, with a focus on stability and regulatory requirements.",
        "Blink Nutritears is expanding in the EU, with a focus on dry eye claims and new delivery formats (gummies).",
        "GINGEVER is being used in supplement and functional food innovation."
    ]
    
    st.markdown("#### 💡 Key Trends & Insights")
    for insight in last_3_months_insights:
        st.markdown(f"<div class='insight-card'>• {insight}</div>", unsafe_allow_html=True)
    
    # Sales Breakdown
    st.markdown("#### 📊 Product Performance")
    for item in last_3_months_data:
        st.markdown(f"<div class='product-card'>", unsafe_allow_html=True)
        st.markdown(f"##### {item['Product']} <span style='color: #1f77b4;'>({item['Number of Appointments']} appointments)</span>", unsafe_allow_html=True)
        
        st.markdown("**Key Customers:**")
        for cust in item["Key Customers"]:
            st.markdown(f"<div class='bullet-point'>• {cust}</div>", unsafe_allow_html=True)
        
        st.markdown("**Sales Notes:**")
        for note in item["Sales Notes"]:
            st.markdown(f"<div class='bullet-point'>• {note}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Sales Manager Performance
    st.markdown("#### 👥 Sales Manager Performance")
    manager_df = pd.DataFrame(last_3_months_total)
    st.dataframe(manager_df, use_container_width=True)
    
    # Visual metrics
    col1, col2 = st.columns(2)
    with col1:
        top_performer = max(last_3_months_total, key=lambda x: x['Total Appointments'])
        st.metric("Top Performer", f"{top_performer['Sales Manager']} ({top_performer['Total Appointments']})")
    with col2:
        total_appts = sum(item['Total Appointments'] for item in last_3_months_total)
        st.metric("Total Appointments", total_appts)

def display_last_week_insights():
    st.markdown("<h2 class='sub-header'>Last Week Insights</h2>", unsafe_allow_html=True)
    st.info("No major appointments recorded last week.")
    
    # Placeholder data
    st.markdown("#### 📊 Product Performance")
    st.markdown("<div class='product-card'>", unsafe_allow_html=True)
    st.markdown("##### No product data available")
    st.markdown("**Key Customers:** • –")
    st.markdown("**Sales Notes:** • –")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("#### 👥 Sales Manager Performance")
    manager_df = pd.DataFrame(last_week_total)
    st.dataframe(manager_df, use_container_width=True)

# =========================
# Display based on selection
# =========================
if timeframe == "Yearly":
    display_yearly_insights()
elif timeframe == "Last 3 Months":
    display_3month_insights()
else:
    display_last_week_insights()

# =========================
# Footer
# =========================
st.markdown("***")
st.markdown("<div style='text-align: center; color: #7f8c8d; margin-top: 2rem;'>Sales & Business Appointment Insights Dashboard • Updated regularly</div>", unsafe_allow_html=True)