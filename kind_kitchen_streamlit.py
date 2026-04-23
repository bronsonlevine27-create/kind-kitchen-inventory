# ================================================================
#  🍽️  THE KIND KITCHEN — Inventory Manager (Streamlit)
#
#  HOW TO RUN:
#  1. Install:  pip install streamlit pandas
#  2. Save this file as:  kind_kitchen.py
#  3. Run:      streamlit run kind_kitchen.py
#  4. Opens at: http://localhost:8501
#
#  TO DEPLOY FREE (shareable link for your whole group):
#  1. Push to GitHub
#  2. Go to share.streamlit.io → connect repo → deploy!
# ================================================================

import streamlit as st
import pandas as pd
import datetime

# ── Page Config ─────────────────────────────────────────────
st.set_page_config(
    page_title="The Kind Kitchen – Inventory",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ───────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800&family=Lato:wght@300;400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Lato', sans-serif;
}

/* Background */
.stApp {
    background: linear-gradient(135deg, #fdf6ee 0%, #f5ede0 100%);
}

/* Header banner */
.kk-banner {
    background: #2d2318;
    border-radius: 16px;
    padding: 24px 32px;
    margin-bottom: 24px;
    display: flex;
    align-items: center;
    gap: 18px;
    box-shadow: 0 4px 20px rgba(45,35,24,0.18);
}
.kk-banner-title {
    font-family: 'Playfair Display', Georgia, serif;
    color: #e8a045;
    font-size: 32px;
    font-weight: 800;
    margin: 0;
    line-height: 1.1;
}
.kk-banner-sub {
    color: #a08060;
    font-size: 12px;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-top: 4px;
}

/* Stat cards */
.kk-stat-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 14px;
    margin-bottom: 24px;
}
.kk-stat {
    background: #ffffff;
    border: 1.5px solid #e8d8c0;
    border-radius: 12px;
    padding: 16px 20px;
    display: flex;
    align-items: center;
    gap: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}
.kk-stat-alert { border-color: #e8a045 !important; background: #fff8f0 !important; }
.kk-stat-icon  { font-size: 30px; }
.kk-stat-val   { font-size: 26px; font-weight: 700; color: #2d2318; line-height: 1; }
.kk-stat-lbl   { font-size: 11px; color: #a08060; letter-spacing: 1.5px; text-transform: uppercase; margin-top: 3px; }

/* Table styling */
.kk-table-wrap {
    background: #fff;
    border-radius: 14px;
    border: 1.5px solid #e8d8c0;
    overflow: hidden;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
}
.kk-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
    font-family: 'Lato', sans-serif;
}
.kk-table thead tr { background: #2d2318; }
.kk-table th {
    color: #e8a045;
    padding: 13px 16px;
    text-align: left;
    font-size: 11px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    font-weight: 700;
}
.kk-table td { padding: 13px 16px; border-top: 1px solid #f0e4d4; vertical-align: middle; }
.kk-table tr:hover td { background: #fdf0e0; }
.kk-row-low td { background: #fff8f0 !important; }

/* Stock bar */
.kk-bar-wrap { display: flex; align-items: center; gap: 8px; }
.kk-bar-bg   { width: 72px; height: 8px; background: #f0e4d4; border-radius: 4px; overflow: hidden; }
.kk-bar-fill { height: 100%; border-radius: 4px; }

/* Category badge */
.kk-badge {
    border-radius: 20px;
    padding: 3px 11px;
    font-size: 12px;
    font-weight: 700;
    display: inline-block;
}

/* Alert cards */
.kk-alert-card {
    background: #fff;
    border: 1.5px solid #e8a045;
    border-radius: 12px;
    padding: 16px 20px;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 14px;
    box-shadow: 0 2px 8px rgba(232,160,69,0.08);
}
.kk-ok {
    background: #f0fff4;
    border: 1.5px solid #5cb85c;
    border-radius: 12px;
    padding: 28px;
    text-align: center;
    color: #3a7a3a;
    font-size: 17px;
    font-weight: 600;
}

/* Category summary cards */
.kk-cat-card {
    background: #fff;
    border-radius: 12px;
    padding: 18px 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    margin-bottom: 12px;
}

/* Section headers */
.kk-section-title {
    font-family: 'Playfair Display', Georgia, serif;
    color: #2d2318;
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 16px;
    padding-bottom: 8px;
    border-bottom: 2px solid #e8d8c0;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #2d2318 !important;
}
section[data-testid="stSidebar"] * {
    color: #e8d8c0 !important;
}
section[data-testid="stSidebar"] .stSelectbox label,
section[data-testid="stSidebar"] .stTextInput label,
section[data-testid="stSidebar"] .stNumberInput label {
    color: #a08060 !important;
    font-size: 12px;
    letter-spacing: 1px;
    text-transform: uppercase;
}
section[data-testid="stSidebar"] h2 {
    color: #e8a045 !important;
    font-family: 'Playfair Display', Georgia, serif !important;
}

/* Streamlit button overrides */
.stButton > button {
    background: #e8a045;
    color: #2d2318;
    border: none;
    border-radius: 8px;
    font-weight: 700;
    font-family: 'Lato', sans-serif;
    padding: 8px 20px;
    transition: background 0.2s;
}
.stButton > button:hover { background: #d4903a; color: #fff; }

div[data-testid="stMetricValue"] {
    font-family: 'Playfair Display', Georgia, serif;
    color: #2d2318;
}

/* Tab styling */
.stTabs [data-baseweb="tab-list"] {
    background: #fff;
    border-radius: 10px 10px 0 0;
    border-bottom: 2px solid #e8d8c0;
    gap: 4px;
    padding: 0 8px;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'Lato', sans-serif;
    font-weight: 700;
    color: #a08060;
    border-radius: 8px 8px 0 0;
    padding: 10px 20px;
}
.stTabs [aria-selected="true"] {
    background: #2d2318 !important;
    color: #e8a045 !important;
}

/* Success / error messages */
.stSuccess { background: #f0fff4 !important; border-left: 4px solid #5cb85c !important; }
.stError   { background: #fff0f0 !important; border-left: 4px solid #e87070 !important; }
.stWarning { background: #fff8f0 !important; border-left: 4px solid #e8a045 !important; }
</style>
""", unsafe_allow_html=True)

# ── Category Config ──────────────────────────────────────────
CATEGORIES = ["Pantry", "Produce", "Grains", "Dairy", "Protein", "Spices", "Other"]
CAT_COLORS = {
    "Pantry":  ("#e8a045", "#fff3d6"),
    "Produce": ("#5cb85c", "#e8f8e8"),
    "Grains":  ("#c4935c", "#f5eade"),
    "Dairy":   ("#7ec8e3", "#e3f5fb"),
    "Protein": ("#e87070", "#fde8e8"),
    "Spices":  ("#b07fd4", "#f2e8fb"),
    "Other":   ("#aaaaaa", "#f0f0f0"),
}

# ── Session State (in-memory database) ──────────────────────
if "inventory" not in st.session_state:
    st.session_state.inventory = [
        {"id": 1, "name": "Olive Oil",       "category": "Pantry",  "qty": 8,  "unit": "bottles", "min_stock": 4,  "cost": 12.99, "emoji": "🫙"},
        {"id": 2, "name": "Canned Tomatoes", "category": "Pantry",  "qty": 2,  "unit": "cans",    "min_stock": 10, "cost": 1.49,  "emoji": "🥫"},
        {"id": 3, "name": "Carrots",         "category": "Produce", "qty": 15, "unit": "lbs",     "min_stock": 5,  "cost": 0.89,  "emoji": "🥕"},
        {"id": 4, "name": "Onions",          "category": "Produce", "qty": 20, "unit": "lbs",     "min_stock": 8,  "cost": 0.69,  "emoji": "🧅"},
        {"id": 5, "name": "Brown Rice",      "category": "Grains",  "qty": 3,  "unit": "bags",    "min_stock": 6,  "cost": 4.99,  "emoji": "🌾"},
        {"id": 6, "name": "Chicken Broth",   "category": "Pantry",  "qty": 12, "unit": "cartons", "min_stock": 6,  "cost": 3.29,  "emoji": "🍲"},
        {"id": 7, "name": "Lentils",         "category": "Grains",  "qty": 5,  "unit": "lbs",     "min_stock": 4,  "cost": 1.99,  "emoji": "🫘"},
        {"id": 8, "name": "Spinach",         "category": "Produce", "qty": 1,  "unit": "bags",    "min_stock": 4,  "cost": 3.49,  "emoji": "🥬"},
    ]
if "next_id" not in st.session_state:
    st.session_state.next_id = 9
if "log" not in st.session_state:
    st.session_state.log = []

inv = st.session_state.inventory

# ── Helper Functions ─────────────────────────────────────────
def total_value():
    return sum(i["qty"] * i["cost"] for i in inv)

def low_stock():
    return [i for i in inv if i["qty"] < i["min_stock"]]

def add_log(msg):
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    st.session_state.log.insert(0, f"[{ts}] {msg}")
    if len(st.session_state.log) > 20:
        st.session_state.log = st.session_state.log[:20]

def stock_bar_html(item):
    pct = min(100, int(item["qty"] / max(item["min_stock"] * 2, 1) * 100))
    color = "#e87070" if pct < 30 else "#e8a045" if pct < 60 else "#5cb85c"
    warn  = "⚠️" if item["qty"] < item["min_stock"] else ""
    qty_color = "#c87000" if item["qty"] < item["min_stock"] else "#2d2318"
    return (
        f'<div class="kk-bar-wrap">'
        f'<div class="kk-bar-bg"><div class="kk-bar-fill" style="width:{pct}%;background:{color}"></div></div>'
        f'<span style="font-weight:700;color:{qty_color}">{item["qty"]}</span>{warn}'
        f'</div>'
    )

def cat_badge_html(cat):
    fg, bg = CAT_COLORS.get(cat, ("#aaa", "#f0f0f0"))
    return f'<span class="kk-badge" style="color:{fg};background:{bg};border:1px solid {fg}">{cat}</span>'

# ── Header Banner ────────────────────────────────────────────
st.markdown("""
<div class="kk-banner">
  <span style="font-size:48px">🍽️</span>
  <div>
    <div class="kk-banner-title">The Kind Kitchen</div>
    <div class="kk-banner-sub">Inventory Manager · Palm Beach Gardens, FL</div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Stat Strip ───────────────────────────────────────────────
low = low_stock()
cats_active = len(set(i["category"] for i in inv))
alert_cls = "kk-stat kk-stat-alert" if low else "kk-stat"

st.markdown(f"""
<div class="kk-stat-grid">
  <div class="kk-stat">
    <span class="kk-stat-icon">📦</span>
    <div><div class="kk-stat-val">{len(inv)}</div><div class="kk-stat-lbl">Total Items</div></div>
  </div>
  <div class="{alert_cls}">
    <span class="kk-stat-icon">⚠️</span>
    <div><div class="kk-stat-val" style="color:{'#c87000' if low else '#2d2318'}">{len(low)}</div>
    <div class="kk-stat-lbl">Low Stock</div></div>
  </div>
  <div class="kk-stat">
    <span class="kk-stat-icon">💰</span>
    <div><div class="kk-stat-val">${total_value():.2f}</div><div class="kk-stat-lbl">Total Value</div></div>
  </div>
  <div class="kk-stat">
    <span class="kk-stat-icon">🗂️</span>
    <div><div class="kk-stat-val">{cats_active}</div><div class="kk-stat-lbl">Categories</div></div>
  </div>
</div>
""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ➕ Add New Item")
    st.markdown("---")

    s_emoji = st.text_input("Icon (emoji)", value="📦")
    s_name  = st.text_input("Item Name *")
    s_cat   = st.selectbox("Category", CATEGORIES)
    s_unit  = st.text_input("Unit (e.g. lbs, cans) *")

    col1, col2 = st.columns(2)
    with col1:
        s_qty = st.number_input("Qty *", min_value=0.0, step=1.0)
    with col2:
        s_min = st.number_input("Min Stock", min_value=0.0, step=1.0)

    s_cost = st.number_input("Cost per unit ($)", min_value=0.0, step=0.01, format="%.2f")

    if st.button("➕ Add Item", use_container_width=True):
        if not s_name.strip() or not s_unit.strip():
            st.error("Name and unit are required.")
        else:
            inv.append({
                "id": st.session_state.next_id,
                "name": s_name.strip(),
                "category": s_cat,
                "qty": s_qty,
                "unit": s_unit.strip(),
                "min_stock": s_min,
                "cost": s_cost,
                "emoji": s_emoji or "📦",
            })
            st.session_state.next_id += 1
            add_log(f"✅ Added {s_name.strip()}")
            st.success(f"Added {s_emoji} {s_name}!")
            st.rerun()

    st.markdown("---")
    st.markdown("## 🔧 Adjust Quantity")
    if inv:
        item_names = [f"{i['emoji']} {i['name']}" for i in inv]
        adj_sel   = st.selectbox("Item", item_names, key="adj_sel")
        adj_delta = st.number_input("Change by (+ add / − remove)", step=1, value=0, key="adj_delta")
        if st.button("✅ Apply Adjustment", use_container_width=True):
            for item in inv:
                if f"{item['emoji']} {item['name']}" == adj_sel:
                    item["qty"] = max(0, item["qty"] + adj_delta)
                    add_log(f"{'➕' if adj_delta>=0 else '➖'} {item['name']} → {item['qty']} {item['unit']}")
                    st.success(f"Updated! {item['name']} is now {item['qty']} {item['unit']}")
                    st.rerun()

    st.markdown("---")
    st.markdown("## 🗑️ Remove Item")
    if inv:
        del_names = [f"{i['emoji']} {i['name']}" for i in inv]
        del_sel   = st.selectbox("Item to remove", del_names, key="del_sel")
        if st.button("🗑️ Delete Item", use_container_width=True):
            for item in inv:
                if f"{item['emoji']} {item['name']}" == del_sel:
                    inv.remove(item)
                    add_log(f"🗑️ Removed {item['name']}")
                    st.warning(f"Removed {item['name']}")
                    st.rerun()

    if st.session_state.log:
        st.markdown("---")
        st.markdown("## 📋 Activity Log")
        for entry in st.session_state.log[:8]:
            st.markdown(f"<small style='color:#a08060'>{entry}</small>", unsafe_allow_html=True)

# ── Main Tabs ────────────────────────────────────────────────
tab_inv, tab_alerts, tab_summary = st.tabs(["📦 Inventory", "⚠️ Alerts", "📊 Summary"])

# ── TAB 1: Inventory ─────────────────────────────────────────
with tab_inv:
    st.markdown('<div class="kk-section-title">All Inventory</div>', unsafe_allow_html=True)

    fc1, fc2, fc3 = st.columns([3, 2, 2])
    with fc1:
        search = st.text_input("🔍 Search", placeholder="Search items...", label_visibility="collapsed")
    with fc2:
        cat_filter = st.selectbox("Category", ["All"] + CATEGORIES, label_visibility="collapsed")
    with fc3:
        sort_by = st.selectbox("Sort", ["Name", "Quantity", "Low Stock First"], label_visibility="collapsed")

    # Filter & sort
    rows = [i for i in inv
            if (cat_filter == "All" or i["category"] == cat_filter)
            and search.lower() in i["name"].lower()]
    if sort_by == "Name":           rows.sort(key=lambda x: x["name"])
    elif sort_by == "Quantity":     rows.sort(key=lambda x: x["qty"])
    elif sort_by == "Low Stock First": rows.sort(key=lambda x: x["qty"] - x["min_stock"])

    # Build HTML table
    if not rows:
        st.info("No items match your search.")
    else:
        rows_html = ""
        for item in rows:
            low_cls = 'class="kk-row-low"' if item["qty"] < item["min_stock"] else ""
            value   = item["qty"] * item["cost"]
            rows_html += f"""
            <tr {low_cls}>
              <td>
                <span style="font-size:20px">{item['emoji']}</span>
                <strong style="margin-left:8px;color:#2d2318">{item['name']}</strong>
                <span style="color:#a08060;font-size:11px;margin-left:4px">({item['unit']})</span>
              </td>
              <td>{cat_badge_html(item['category'])}</td>
              <td>{stock_bar_html(item)}</td>
              <td style="color:#a08060;text-align:center">{int(item['min_stock'])}</td>
              <td style="font-weight:700;color:#2d2318">${value:.2f}</td>
            </tr>"""

        st.markdown(f"""
        <div class="kk-table-wrap">
          <table class="kk-table">
            <thead><tr>
              <th>Item</th>
              <th>Category</th>
              <th>Stock</th>
              <th style="text-align:center">Min Stock</th>
              <th>Value</th>
            </tr></thead>
            <tbody>{rows_html}</tbody>
          </table>
        </div>
        """, unsafe_allow_html=True)

    # CSV Export
    st.markdown("<br>", unsafe_allow_html=True)
    if inv:
        df = pd.DataFrame([{
            "Name": i["name"], "Category": i["category"],
            "Qty": i["qty"], "Unit": i["unit"],
            "Min Stock": i["min_stock"], "Cost/Unit": i["cost"],
            "Total Value": round(i["qty"] * i["cost"], 2)
        } for i in inv])
        csv = df.to_csv(index=False)
        st.download_button(
            "⬇️ Export CSV",
            data=csv,
            file_name=f"kind_kitchen_inventory_{datetime.date.today()}.csv",
            mime="text/csv",
        )

# ── TAB 2: Alerts ────────────────────────────────────────────
with tab_alerts:
    st.markdown('<div class="kk-section-title">⚠️ Low Stock Alerts</div>', unsafe_allow_html=True)
    low = low_stock()
    if not low:
        st.markdown('<div class="kk-ok">✅ All items are well stocked — nothing to reorder!</div>',
                    unsafe_allow_html=True)
    else:
        for item in sorted(low, key=lambda x: x["qty"] - x["min_stock"]):
            needed = int(item["min_stock"] - item["qty"])
            fg, bg = CAT_COLORS.get(item["category"], ("#aaa","#f0f0f0"))
            st.markdown(f"""
            <div class="kk-alert-card">
              <span style="font-size:34px">{item['emoji']}</span>
              <div style="flex:1">
                <div style="font-size:17px;font-weight:700;color:#2d2318">{item['name']}</div>
                <div style="font-size:12px;color:#a08060">{item['category']} · {item['unit']}</div>
              </div>
              <div style="text-align:right;margin-right:16px">
                <div style="font-size:28px;font-weight:700;color:#c87000">{int(item['qty'])}</div>
                <div style="font-size:11px;color:#a08060">of {int(item['min_stock'])} min</div>
              </div>
              <div style="background:#e8a045;color:#fff;border-radius:10px;
                          padding:8px 16px;font-weight:700;font-size:13px;white-space:nowrap">
                Need {needed} {item['unit']}
              </div>
            </div>
            """, unsafe_allow_html=True)

# ── TAB 3: Summary ───────────────────────────────────────────
with tab_summary:
    st.markdown('<div class="kk-section-title">📊 Inventory Summary</div>', unsafe_allow_html=True)

    cats_present = [c for c in CATEGORIES if any(i["category"] == c for i in inv)]
    cols = st.columns(len(cats_present) if cats_present else 1)

    for idx, cat in enumerate(cats_present):
        items_c = [i for i in inv if i["category"] == cat]
        val_c   = sum(i["qty"] * i["cost"] for i in items_c)
        low_c   = sum(1 for i in items_c if i["qty"] < i["min_stock"])
        fg, bg  = CAT_COLORS.get(cat, ("#aaa", "#f0f0f0"))
        with cols[idx]:
            st.markdown(f"""
            <div class="kk-cat-card" style="border:2px solid {fg}">
              <div style="font-size:11px;font-weight:700;letter-spacing:1.5px;
                          text-transform:uppercase;color:{fg};margin-bottom:8px">{cat}</div>
              <div style="font-size:28px;font-weight:700;color:#2d2318;line-height:1">
                {len(items_c)}<span style="font-size:13px;color:#a08060;font-weight:400"> items</span>
              </div>
              <div style="font-size:14px;color:#5a4a38;margin-top:6px">
                Value: <strong>${val_c:.2f}</strong>
              </div>
              {"<div style='color:#c87000;font-size:12px;font-weight:700;margin-top:6px'>⚠️ "+str(low_c)+" low stock</div>" if low_c else ""}
            </div>
            """, unsafe_allow_html=True)

    # Total value box
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background:#2d2318;border-radius:14px;padding:24px 32px;margin-top:8px">
      <div style="font-family:'Playfair Display',Georgia,serif;color:#e8a045;
                  font-size:18px;font-weight:700;margin-bottom:8px">Total Inventory Value</div>
      <div style="font-size:48px;font-weight:700;color:#fff;font-family:'Playfair Display',Georgia,serif">
        ${total_value():.2f}
      </div>
      <div style="font-size:13px;color:#a08060;margin-top:6px">
        {len(inv)} items across {len(cats_present)} categories
        {" · " + str(len(low_stock())) + " alerts" if low_stock() else " · fully stocked ✅"}
      </div>
    </div>
    """, unsafe_allow_html=True)
