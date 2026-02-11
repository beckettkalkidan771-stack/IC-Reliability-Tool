import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# 设置字体 - 支持中文
import matplotlib.font_manager as fm
import os

# 查找系统可用的中文字体
chinese_fonts = ['SimHei', 'Microsoft YaHei', 'Noto Sans CJK SC', 'WenQuanYi Micro Hei', 'Droid Sans Fallback']
available_font = None

for font in chinese_fonts:
    if font in [f.name for f in fm.fontManager.ttflist]:
        available_font = font
        break

if available_font:
    plt.rcParams['font.sans-serif'] = [available_font]
    plt.rcParams['axes.unicode_minus'] = False
else:
    # 如果没有中文字体，使用英文标签
    st.warning("⚠️ 系统未检测到中文字体，图表将使用英文标签")

# 定义图表字体设置函数
def set_chart_style():
    if available_font:
        plt.rcParams['font.family'] = available_font
    plt.rcParams['axes.unicode_minus'] = False

# ==================== 自定义CSS样式 - 教育科技风格 ====================
st.markdown("""
<style>
    /* 主色调 */
    :root {
        --primary-color: #1E88E5;
        --secondary-color: #00ACC1;
        --accent-color: #7C4DFF;
        --success-color: #43A047;
        --warning-color: #FB8C00;
        --bg-gradient: linear-gradient(135deg, #1E88E5 0%, #00ACC1 100%);
    }

    /* 标题样式 */
    .main-title {
        font-size: 2.2rem !important;
        font-weight: 700 !important;
        color: #1565C0 !important;
        text-align: center;
        padding: 1rem 0;
        border-bottom: 3px solid #1E88E5;
        margin-bottom: 1.5rem !important;
    }

    /* 副标题样式 */
    .section-title {
        font-size: 1.4rem !important;
        font-weight: 600 !important;
        color: #00838F !important;
        padding: 0.5rem 1rem;
        background: linear-gradient(90deg, #E3F2FD 0%, transparent 100%);
        border-left: 4px solid #00ACC1;
        margin: 1rem 0 !important;
    }

    /* 公式卡片样式 */
    .formula-card {
        background: linear-gradient(135deg, #FAFAFA 0%, #E3F2FD 100%);
        border: 1px solid #BBDEFB;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }

    .formula-title {
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        color: #1565C0 !important;
        margin-bottom: 0.8rem !important;
    }

    /* 理论说明卡片 */
    .theory-card {
        background: #FFFDE7;
        border: 1px solid #FFF59D;
        border-radius: 10px;
        padding: 1rem 1.2rem;
        margin: 0.8rem 0;
        font-size: 0.95rem;
        line-height: 1.6;
    }

    /* 输入区域卡片 */
    .input-card {
        background: #F5F5F5;
        border-radius: 12px;
        padding: 1.2rem;
        margin: 0.5rem 0;
        border: 1px solid #E0E0E0;
    }

    /* 结果卡片 */
    .result-card {
        background: linear-gradient(135deg, #E8F5E9 0%, #C8E6C9 100%);
        border: 1px solid #A5D6A7;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        margin: 1rem 0;
    }

    .result-value {
        font-size: 2.5rem !important;
        font-weight: 700 !important;
        color: #2E7D32 !important;
    }

    .result-label {
        font-size: 1rem !important;
        color: #558B2F !important;
        margin-top: 0.5rem !important;
    }

    /* 提示卡片 */
    .info-box {
        background: linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 100%);
        border-left: 4px solid #1E88E5;
        padding: 1rem;
        border-radius: 0 8px 8px 0;
        margin: 1rem 0;
    }

    /* 表格样式 */
    .dataframe {
        font-size: 0.9rem !important;
    }

    /* 侧边栏样式 */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #E3F2FD 0%, #FFFFFF 100%);
    }
</style>
""", unsafe_allow_html=True)

# ==================== 页面配置 ====================
st.set_page_config(
    page_title="IC封装可靠性加速寿命计算器",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== 页面标题 ====================
st.markdown('<p class="main-title">🔬 集成电路封装可靠性加速寿命计算器</p>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #666; font-size: 1rem;">适用于《可靠性验证工程与失效分析》课程教学演示</p>', unsafe_allow_html=True)

# ==================== 第一部分：理论模型介绍 ====================
st.markdown('<p class="section-title">📚 第一部分：加速寿命模型理论</p>', unsafe_allow_html=True)

col_theory1, col_theory2 = st.columns(2)

with col_theory1:
    # 阿伦尼乌斯模型
    st.markdown("""
    <div class="formula-card">
        <p class="formula-title">📐 阿伦尼乌斯模型 (Arrhenius Model)</p>
    </div>
    """, unsafe_allow_html=True)

    st.latex(r"AF_{temp} = \exp\left[\frac{E_a}{k_B}\left(\frac{1}{T_{use}}-\frac{1}{T_{stress}}\right)\right]")

    st.markdown("""
    <div class="theory-card">
        <b>模型说明：</b>阿伦尼乌斯模型描述温度对化学反应速率的影响。<br>
        • <b>Eₐ</b>：激活能 (eV)，典型值 0.4~1.1 eV<br>
        • <b>k_B</b>：玻尔兹曼常数 (8.617×10⁻⁵ eV/K)<br>
        • <b>T</b>：绝对温度 (K)<br>
        • <b>应用场景</b>：HTOL 高温工作寿命测试
    </div>
    """, unsafe_allow_html=True)

with col_theory2:
    # 佩克模型
    st.markdown("""
    <div class="formula-card">
        <p class="formula-title">📐 佩克模型 (Peck Model)</p>
    </div>
    """, unsafe_allow_html=True)

    st.latex(r"AF_{Peck} = \left(\frac{RH_{stress}}{RH_{use}}\right)^n \cdot \exp\left[\frac{E_a}{k_B}\left(\frac{1}{T_{use}}-\frac{1}{T_{stress}}\right)\right]")

    st.markdown("""
    <div class="theory-card">
        <b>模型说明：</b>佩克模型在阿伦尼乌斯基础上增加了湿度因子。<br>
        • <b>RH</b>：相对湿度 (%)<br>
        • <b>n</b>：湿度指数，典型值 2.0~4.0 (常取 3.0)<br>
        • <b>应用场景</b>：HAST/THB 温湿度加速测试
    </div>
    """, unsafe_allow_html=True)

# ==================== 第二部分：实验标准参考 ====================
st.markdown('<p class="section-title">📋 第二部分：JEDEC 可靠性测试标准</p>', unsafe_allow_html=True)

st.markdown("""
<div class="info-box">
<b>JEDEC 标准参考：</b>集成电路可靠性验证的典型测试条件
</div>
""", unsafe_allow_html=True)

col_std1, col_std2, col_std3 = st.columns(3)

with col_std1:
    st.markdown("""
    <div style="background: #E3F2FD; padding: 1rem; border-radius: 10px; border-left: 4px solid #1E88E5;">
        <b style="color: #1565C0;">🌡️ HTOL - 高温工作寿命</b><br><br>
        <b>典型条件：</b>125°C, 1000h<br>
        <b>测试目的：</b>评估长期电热应力下的稳定性<br>
        <b>适用模型：</b>Arrhenius
    </div>
    """, unsafe_allow_html=True)

with col_std2:
    st.markdown("""
    <div style="background: #E8F5E9; padding: 1rem; border-radius: 10px; border-left: 4px solid #43A047;">
        <b style="color: #2E7D32;">💧 HAST - 高加速应力测试</b><br><br>
        <b>典型条件：</b>130°C, 85%RH, 96h<br>
        <b>测试目的：</b>评估非气密封装的防潮能力<br>
        <b>适用模型：</b>Peck
    </div>
    """, unsafe_allow_html=True)

with col_std3:
    st.markdown("""
    <div style="background: #FFF3E0; padding: 1rem; border-radius: 10px; border-left: 4px solid #FB8C00;">
        <b style="color: #E65100;">🌡️💧 THB - 温湿度偏置</b><br><br>
        <b>典型条件：</b>85°C, 85%RH, 1000h<br>
        <b>测试目的：</b>传统湿度可靠性测试<br>
        <b>适用模型：</b>Peck
    </div>
    """, unsafe_allow_html=True)

# ==================== 第三部分：参数配置 ====================
st.markdown('<p class="section-title">⚙️ 第三部分：物理参数配置</p>', unsafe_allow_html=True)

col_param1, col_param2 = st.columns([1, 3])

with col_param1:
    st.info("💡 **教学提示**：调整侧边栏参数观察加速因子变化")
    ea = st.sidebar.slider("激活能 Ea (eV)", 0.4, 1.1, 0.7, help="HTOL/HAST典型值取0.7eV")
    n_factor = st.sidebar.slider("湿度指数 n", 2.0, 4.0, 3.0, help="Peck模型典型值取3.0")
    k_boltzmann = 8.617e-5

    # 模型选择
    st.markdown("### 🎯 选择加速模型")
    model_type = st.radio("请选择计算模型：", ["Arrhenius (仅温度 - HTOL)", "Peck (温度 + 湿度 - HAST/THB)"])

with col_param2:
    # 输入区卡片
    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🏠 正常使用条件 (Use)")
        t_use_c = st.number_input("使用环境温度 (°C)", value=25, key='t_u', help="芯片实际使用环境的温度")
        rh_use = st.slider("使用环境相对湿度 (%)", 1, 100, 50, key='rh_u') if "Peck" in model_type else 1.0

    with col2:
        st.markdown("🧪 实验室测试条件 (Stress)")
        t_stress_c = st.number_input("测试环境温度 (°C)", value=130 if "Peck" in model_type else 125, key='t_s', help="加速测试的应力温度")
        rh_stress = st.slider("测试环境相对湿度 (%)", 1, 100, 85, key='rh_s') if "Peck" in model_type else 1.0
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== 第四部分：计算结果 ====================
st.markdown('<p class="section-title">📊 第四部分：计算结果与分析</p>', unsafe_allow_html=True)

# 计算逻辑
t_use_k = t_use_c + 273.15
t_stress_k = t_stress_c + 273.15

af_temp = np.exp((ea / k_boltzmann) * ((1 / t_use_k) - (1 / t_stress_k)))
if "Peck" in model_type:
    rh_use_safe = max(rh_use, 1)
    af_hum = (rh_stress / rh_use_safe) ** n_factor
else:
    af_hum = 1.0
af_total = af_temp * af_hum

# 拟定测试时长
test_hours = st.number_input("📅 拟定测试时长 (Hours)", value=96 if "Peck" in model_type else 1000)
equiv_years = (test_hours * af_total) / (24 * 365)
equiv_days = (test_hours * af_total) / 24

# 结果展示
col_res1, col_res2, col_res3 = st.columns(3)

with col_res1:
    st.markdown(f"""
    <div class="result-card" style="background: linear-gradient(135deg, #E3F2FD 0%, #BBDEFB 100%); border-color: #1E88E5;">
        <p class="result-value" style="color: #1565C0 !important;">{af_total:.1f}X</p>
        <p class="result-label">总加速因子 AF</p>
    </div>
    """, unsafe_allow_html=True)

with col_res2:
    st.markdown(f"""
    <div class="result-card">
        <p class="result-value">{equiv_years:.1f} 年</p>
        <p class="result-label">等效使用寿命</p>
    </div>
    """, unsafe_allow_html=True)

with col_res3:
    st.markdown(f"""
    <div class="result-card" style="background: linear-gradient(135deg, #FFF3E0 0%, #FFE0B2 100%); border-color: #FB8C00;">
        <p class="result-value" style="color: #E65100 !important;">{equiv_days:.0f} 天</p>
        <p class="result-label">等效天数</p>
    </div>
    """, unsafe_allow_html=True)

# 达标判断
if equiv_years < 10:
    st.warning(f"⚠️ **可靠性提醒**：等效寿命 {equiv_years:.1f} 年不足10年，可能无法满足车规级或工业级长寿命要求")
elif equiv_years < 20:
    st.info(f"📌 **可靠性提示**：等效寿命 {equiv_years:.1f} 年，满足工业级10年要求，但需注意车规级20年标准")
else:
    st.success(f"✅ **可靠性达标**：等效寿命 {equiv_years:.1f} 年，同时满足车规级(10年)和工业级(20年)要求")

# ==================== 第五部分：可视化分析 ====================
st.markdown('<p class="section-title">📈 第五部分：可视化分析</p>', unsafe_allow_html=True)

# 图表1：加速因子分解
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.markdown("#### 🎯 Acceleration Factor Breakdown")
    set_chart_style()
    fig1, ax = plt.subplots(figsize=(8, 5))

    if "Peck" in model_type:
        factors = ['Temp AF', 'Humidity AF', 'Total AF']
        values = [af_temp, af_hum, af_total]
        colors = ['#1E88E5', '#7C4DFF', '#E53935']
        labels = [f'{af_temp:.1f}X', f'{af_hum:.1f}X', f'{af_total:.1f}X']
    else:
        factors = ['Temp AF', 'Total AF']
        values = [af_temp, af_total]
        colors = ['#1E88E5', '#E53935']
        labels = [f'{af_temp:.1f}X', f'{af_total:.1f}X']

    bars = ax.bar(factors, values, color=colors, edgecolor='white', linewidth=2)
    ax.set_ylabel('Acceleration Factor (AF)', fontsize=12)
    ax.set_title(f'AF Composition (Ea={ea}eV)', fontsize=14, fontweight='bold', pad=10)

    for bar, val, label in zip(bars, values, labels):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(values)*0.02,
                label, ha='center', fontsize=12, fontweight='bold')
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height()/2,
                f'{val:.1f}', ha='center', va='center', fontsize=14, fontweight='bold', color='white')

    ax.set_ylim(0, max(values) * 1.25)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.tight_layout()
    st.pyplot(fig1)

with col_chart2:
    st.markdown("#### ⏱️ Time Equivalence Comparison")
    set_chart_style()
    fig2, axes = plt.subplots(1, 2, figsize=(10, 4.5))

    # 左图：小时
    ax1 = axes[0]
    hours_labels = ['Test Time', 'Equiv. Use Time']
    hours_values = [test_hours, test_hours * af_total]
    colors_hours = ['#FF6B6B', '#4ECDC4']
    bars1 = ax1.bar(hours_labels, hours_values, color=colors_hours, edgecolor='white', linewidth=2)
    ax1.set_ylabel('Time (hours)', fontsize=11)
    ax1.set_title('Hours Comparison', fontsize=12, fontweight='bold')
    ax1.bar_label(bars1, fmt='%.0f h', padding=3, fontsize=10)
    ax1.set_ylim(0, max(hours_values) * 1.15)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)

    # 右图：年
    ax2 = axes[1]
    years_values = [test_hours / (24 * 365), equiv_years]
    bars2 = ax2.bar(hours_labels, years_values, color=colors_hours, edgecolor='white', linewidth=2)
    ax2.set_ylabel('Time (years)', fontsize=11)
    ax2.set_title('Years Comparison', fontsize=12, fontweight='bold')
    ax2.bar_label(bars2, fmt='%.2f yr', padding=3, fontsize=10)
    ax2.set_ylim(0, max(years_values) * 1.15 if max(years_values) > 0 else 1)
    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)

    plt.tight_layout()
    st.pyplot(fig2)

# 图表2：多方案对比
st.markdown("#### 📋 Test Duration Comparison")
set_chart_style()
test_hours_options = [96, 168, 500, 1000, 2000]
equiv_years_list = [(h * af_total) / (24 * 365) for h in test_hours_options]

fig3, ax = plt.subplots(figsize=(11, 5))

# 颜色根据达标情况
colors = ['#E53935' if y < 10 else '#FB8C00' if y < 20 else '#43A047' for y in equiv_years_list]

bars = ax.bar([f'{h}h' for h in test_hours_options], equiv_years_list,
              color=colors, edgecolor='white', linewidth=2)

ax.axhline(y=10, color='#E53935', linestyle='--', linewidth=2, label='Automotive (10yr)')
ax.axhline(y=20, color='#FB8C00', linestyle='--', linewidth=2, label='Industrial (20yr)')

ax.set_xlabel('Test Duration', fontsize=12)
ax.set_ylabel('Equiv. Lifespan (years)', fontsize=12)
ax.set_title(f'Test Duration vs Lifespan (AF = {af_total:.1f}X)', fontsize=14, fontweight='bold', pad=10)
ax.legend(loc='upper left', fontsize=10)
ax.bar_label(bars, fmt='%.1f yr', padding=3, fontsize=10)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_ylim(0, max(equiv_years_list) * 1.25)

plt.tight_layout()
st.pyplot(fig3)

# ==================== 第六部分：结果汇总 ====================
st.markdown('<p class="section-title">📝 第六部分：计算结果汇总</p>', unsafe_allow_html=True)

result_df = pd.DataFrame({
    '参数': ['使用温度 (Use)', '测试温度 (Stress)', '使用湿度 (Use)', '测试湿度 (Stress)',
            '激活能 Ea', '湿度指数 n', '温度加速因子', '湿度加速因子',
            '总加速因子 AF', '拟定测试时长', '等效使用寿命'],
    '数值': [f'{t_use_c} °C', f'{t_stress_c} °C',
            f'{rh_use:.0f}%' if "Peck" in model_type else 'N/A',
            f'{rh_stress:.0f}%' if "Peck" in model_type else 'N/A',
            f'{ea} eV', f'{n_factor}', f'{af_temp:.2f}',
            f'{af_hum:.2f}' if "Peck" in model_type else '1.0 (不计)',
            f'{af_total:.2f}', f'{test_hours} 小时', f'{equiv_years:.2f} 年']
})

st.dataframe(result_df, use_container_width=True, hide_index=True)

# 教学总结
st.markdown("""
<div class="theory-card">
<b>📖 课堂小结：</b><br>
1. <b>加速因子 AF</b> 表示测试条件相对于使用条件的加速程度，AF 越大，测试时间越短<br>
2. <b>温度每升高 10°C</b>，反应速率约翻倍（经验法则）<br>
3. <b>等效使用寿命</b> = 测试时长 × AF<br>
4. <b>车规级芯片</b>通常要求等效寿命 ≥ 10 年，<b>工业级</b> ≥ 20 年
</div>
""", unsafe_allow_html=True)

# 页脚
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #888; font-size: 0.85rem;">
    <b>课程：</b>第三篇 第8章 可靠性验证工程与失效分析 |
    <b>参考：</b>JEDEC 标准 [cite: 129, 154, 157] |
    <b>激活能 Ea = {ea} eV</b> |
    <b>湿度指数 n = {n_factor}</b>
</div>
""", unsafe_allow_html=True)
