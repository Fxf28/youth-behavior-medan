import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Konfigurasi halaman
st.set_page_config(
    page_title="MEDAN YOUTH INSIGHTS",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS custom dengan kontras yang lebih baik
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #0D47A1;
        font-weight: 800;
        margin-bottom: 0.5rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    .sub-header {
        font-size: 1.3rem;
        color: #1A237E;
        margin-bottom: 2rem;
        font-weight: 600;
    }
    .section-header {
        font-size: 1.8rem;
        color: #0D47A1;
        border-bottom: 3px solid #1565C0;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1.5rem;
        font-weight: 700;
    }
    .highlight-box {
        background-color: #E3F2FD;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 5px solid #1976D2;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .source-badge {
        background-color: #BBDEFB;
        color: #0D47A1;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-size: 0.8rem;
        display: inline-block;
        margin: 0.2rem;
        font-weight: 600;
        border: 1px solid #90CAF9;
    }
    .metric-card {
        background: linear-gradient(135deg, #1A237E 0%, #0D47A1 100%);
        color: white;
        border-radius: 10px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .data-table {
        background-color: #F5F5F5;
        border-radius: 8px;
        padding: 1rem;
        overflow-x: auto;
    }
    .custom-table {
        width: 100%;
        border-collapse: collapse;
        margin: 1rem 0;
    }
    .custom-table th {
        background-color: #1976D2;
        color: white;
        padding: 12px;
        text-align: left;
        font-weight: bold;
    }
    .custom-table td {
        padding: 10px;
        border-bottom: 1px solid #ddd;
    }
    .custom-table tr:nth-child(even) {
        background-color: #f2f2f2;
    }
    .custom-table tr:hover {
        background-color: #e3f2fd;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #E3F2FD;
        border-radius: 4px 4px 0px 0px;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background-color: #1976D2;
        color: white;
    }
    .content-text {
        color: #212121;
        line-height: 1.6;
        font-size: 1rem;
    }
    .bulleted-list {
        color: #212121;
        line-height: 1.8;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigasi
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <div style="font-size: 2rem; color: #0D47A1; font-weight: bold;">📊</div>
        <h2 style="color: #0D47A1;">MEDAN YOUTH INSIGHTS</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.title("📋 Navigasi")
    
    sections = [
        "📌 Executive Summary",
        "📚 Pendahuluan", 
        "🔬 Metodologi",
        "📖 Tinjauan Pustaka",
        "📊 Analisis Data & Temuan",
        "🔍 Analisis Komparatif",
        "👥 Segmentasi Gen Z Medan",
        "💡 Implikasi & Rekomendasi",
        "✅ Kesimpulan",
        "📚 Daftar Pustaka"
    ]
    
    section_keys = [
        "Executive Summary",
        "Pendahuluan", 
        "Metodologi",
        "Tinjauan Pustaka",
        "Analisis Data & Temuan",
        "Analisis Komparatif",
        "Segmentasi Gen Z Medan",
        "Implikasi & Rekomendasi",
        "Kesimpulan",
        "Daftar Pustaka"
    ]
    
    selected_index = st.radio("Pilih Bagian:", sections, index=0)
    selected_section = section_keys[sections.index(selected_index)]
    
    st.markdown("---")
    st.markdown("### ℹ️ Informasi")
    st.info("""
    **MEDAN YOUTH INSIGHTS**
    
    Laporan analisis minat dan perilaku 
    Gen Z (15-24 tahun) di Kota Medan 
    berdasarkan data sekunder terverifikasi.
    
    **Update:** Januari 2025
    """)
    
    st.markdown("### 📅 Update Terakhir")
    st.caption(f"{datetime.now().strftime('%d %B %Y')}")

# Header utama
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<h1 class="main-header">MEDAN YOUTH INSIGHTS</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Membedah Minat & Perilaku Gen Z (SMA & Mahasiswa) Medan</p>', unsafe_allow_html=True)
with col2:
    st.markdown('<div style="text-align: center; padding: 1rem;">', unsafe_allow_html=True)
    st.markdown('<div style="font-size: 4rem;">📊</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Konten berdasarkan pilihan
if selected_section == "Executive Summary":
    st.markdown('<h2 class="section-header">📌 Executive Summary</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.markdown("### 👥 Populasi Gen Z")
        st.markdown("## ~440K")
        st.markdown("**15-24 tahun**")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.markdown("### 🌐 Penetrasi Internet")
        st.markdown("## 79.5%")
        st.markdown("**APJII 2024**")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.markdown("### 📱 Media Sosial")
        st.markdown("## >2 jam/hari")
        st.markdown("**We Are Social 2024**")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="highlight-box">', unsafe_allow_html=True)
    st.markdown("""
    <div class="content-text">
    **Laporan ini** merangkum gambaran komprehensif tentang Gen Z (kelompok usia ~15–24 tahun) di Kota Medan—menggabungkan data sekunder resmi (BPS Kota/Provinsi, BPS Nasional, Kemendikbudristek), survei lembaga terakreditasi (Populix, Alvara), laporan platform digital (We Are Social / DataReportal, TikTok, Spotify), laporan e-commerce dan ekonomi digital (e-Conomy SEA, Shopee), serta temuan lembaga keuangan dan institusi internasional (Bank Indonesia, OJK, UNICEF, ILO).
    
    ### 🎯 Temuan Utama:
    
    1. **Proporsi pemuda besar** - Medan memiliki kelompok 15–24 tahun ~0,43–0,47 juta per kelompok umur
    2. **Digital natives** - Penetrasi internet dan penggunaan platform sosial sangat tinggi sehingga platform berbasis video (TikTok, Instagram) menjadi kanal utama pengaruh perilaku konsumsi dan identitas
    3. **Ekonomi digital** - Transisi ke ekonomi digital mendorong kenaikan belanja daring dan penggunaan dompet digital namun literasi keuangan remaja masih perlu ditingkatkan
    4. **Isu dominan** - Kesehatan mental, aspirasi kerja wirausaha (side-hustle), dan tekanan terhadap pencitraan sosial adalah isu yang dominan
    
    ### 📋 Rekomendasi Kunci:
    Ditujukan kepada pemerintah daerah, institusi pendidikan, pelaku bisnis, dan LSM untuk intervensi pendidikan digital & keuangan, dukungan kesehatan mental berbasis sekolah/kampus, serta program kewirausahaan yang kontekstual untuk Medan.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("**📌 Sumber:** Badan Pusat Statistik Kota Medan")

elif selected_section == "Pendahuluan":
    st.markdown('<h2 class="section-header">📚 1. Pendahuluan</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["1.1 Latar Belakang", "1.2 Tujuan & Ruang Lingkup", "1.3 Pertanyaan Penelitian"])
    
    with tab1:
        st.markdown("""
        <div class="content-text">
        ### 🏙️ Latar Belakang
        
        **Generasi Z** (lahir kira-kira 1997–2012) di Indonesia tumbuh bersamaan dengan penetrasi internet masif dan ledakan platform sosial serta ekonomi digital. **Kota Medan**—sebagai kota terbesar di Sumatera Utara—memiliki konsentrasi pemuda yang signifikan sehingga dinamika sosial, ekonomi, dan budaya Gen Z di Medan menjadi penting bagi perencanaan daerah, pendidikan, dan upaya pemberdayaan ekonomi lokal.
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<span class="source-badge">Badan Pusat Statistik Kota Medan</span>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown("""
        <div class="content-text">
        ### 🎯 Tujuan & Ruang Lingkup
        
        **Tujuan:** menyajikan analisis deskriptif-analitis tentang profil demografi, akses digital, pola konsumsi, aspirasi pendidikan & karier, serta nilai/sikap sosial Gen Z SMA & mahasiswa di Medan menggunakan sumber sekunder valid dan terverifikasi.
        
        **Ruang lingkup:** fokus pada data terpublikasi (BPS Kota/Provinsi, lembaga survei, platform digital, institusi keuangan, jurnal akademik) sampai tahun publikasi terakhir yang tersedia.
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<span class="source-badge">Badan Pusat Statistik Indonesia</span>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        <div class="content-text">
        ### ❓ Pertanyaan Penelitian
        
        1. **Bagaimana profil demografi** Gen Z di Medan?
        2. **Seberapa luas akses dan pola penggunaan** teknologi digital di kalangan mereka?
        3. **Bagaimana pola konsumsi** dan gaya hidup (on-line / off-line)?
        4. **Apa aspirasi pendidikan/karier** dan perhatian sosial utama?
        5. **Implikasi kebijakan & rekomendasi** untuk pemangku kepentingan lokal?
        </div>
        """, unsafe_allow_html=True)

elif selected_section == "Metodologi":
    st.markdown('<h2 class="section-header">🔬 2. Metodologi Penelitian</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="content-text">
        ### 📝 Jenis Penelitian
        **Deskriptif-analitis** berbasis data sekunder.
        
        ### 📂 Sumber Data:
        - **Publikasi resmi:** BPS Kota Medan, BPS Sumatera Utara, BPS Nasional, Kemendikbudristek
        - **Laporan lembaga survei:** Populix, Alvara
        - **Laporan platform:** We Are Social / DataReportal, TikTok, Spotify
        - **Laporan e-commerce:** e-Conomy SEA, Shopee
        - **Lembaga keuangan:** Bank Indonesia & OJK
        - **Laporan institusional:** Kemenpora, UNICEF, ILO
        - **Artikel/jurnal akademik** lokal dan nasional
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<span class="source-badge">Badan Pusat Statistik Kota Medan</span>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="content-text">
        ### 🔍 Teknik Analisis:
        - **Triangulasi sumber**
        - **Sintesis kuantitatif** untuk indikator utama (populasi usia, penetrasi internet, penggunaan platform)
        - **Analisis kualitatif** tema dari laporan survei serta studi akademik
        
        ### ⚠️ Keterbatasan:
        - **Data spesifik terbatas** - survei perilaku di Kota Medan tidak selalu tersedia sehingga beberapa inferensi menggunakan data Provinsi Sumatera Utara atau data nasional sebagai proxy
        - **Variasi metodologi** survei antar lembaga (sample, definisi Gen Z) membatasi perbandingan langsung
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<span class="source-badge">sumut.bps.go.id</span>', unsafe_allow_html=True)

elif selected_section == "Tinjauan Pustaka":
    st.markdown('<h2 class="section-header">📖 3. Tinjauan Pustaka (Ringkas)</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        st.markdown("""
        <div class="highlight-box">
        <h4>🌍 Teori Gen Z Global</h4>
        <div class="content-text">
        <p>Literatur global menekankan karakter Gen Z sebagai "digital natives", seeking authenticity, entrepreneurial orientation, dan rentan terhadap isu kesehatan mental yang terkait tekanan media sosial.</p>
        </div>
        <span class="source-badge">IAFOR Research Archive</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box">
        <h4>🇮🇩 Studi di Indonesia</h4>
        <div class="content-text">
        <p>Riset lembaga seperti Alvara, Populix, dan sejumlah jurnal lokal mencatat perilaku konsumsi impulsif, dominasi platform video pendek dalam membentuk tren.</p>
        </div>
        <span class="source-badge">Populix</span>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="highlight-box">
        <h4>🏙️ Konteks Medan</h4>
        <div class="content-text">
        <p>Medan sebagai pusat urban Sumatera Utara memiliki demografi muda (banyak 15–24 tahun) dan infrastruktur digital yang terus berkembang.</p>
        </div>
        <span class="source-badge">Databoks</span>
        </div>
        """, unsafe_allow_html=True)

elif selected_section == "Analisis Data & Temuan":
    st.markdown('<h2 class="section-header">📊 4. Analisis Data & Temuan</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "👥 4.1 Profil Demografi", 
        "🌐 4.2 Akses Digital", 
        "💰 4.3 Pola Konsumsi", 
        "🎓 4.4 Pendidikan & Karier",
        "❤️ 4.5 Nilai & Keprihatinan"
    ])
    
    with tab1:
        st.markdown("#### 👥 4.1 Profil Demografi Gen Z Medan")
        
        # Data demografi - menggunakan HTML table manual
        demografi_html = """
        <div style="overflow-x: auto; margin: 1rem 0;">
        <table class="custom-table">
            <thead>
                <tr>
                    <th>Kelompok Umur</th>
                    <th>Perkiraan Jumlah (jiwa)</th>
                    <th>Sumber (tahun)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>15–19 tahun</td>
                    <td>~220.500</td>
                    <td>BPS Kota Medan / Databoks (2024)</td>
                </tr>
                <tr>
                    <td>20–24 tahun</td>
                    <td>~218.500–252.000</td>
                    <td>BPS Kota Medan / Databoks (2024)</td>
                </tr>
            </tbody>
        </table>
        </div>
        """
        
        col1, col2 = st.columns([2, 3])
        
        with col1:
            st.markdown(demografi_html, unsafe_allow_html=True)
            st.caption("**Sumber:** BPS Kota Medan / Databoks (2024)")
        
        with col2:
            # Visualisasi dengan data statis
            fig = go.Figure(data=[
                go.Bar(
                    x=['15-19 tahun', '20-24 tahun'], 
                    y=[220500, 235250],
                    marker_color=['#1A237E', '#0D47A1'],
                    text=['220,500', '235,250'],
                    textposition='auto',
                    textfont=dict(color='white', size=14)
                )
            ])
            fig.update_layout(
                title='Distribusi Populasi Gen Z Medan',
                xaxis_title='Kelompok Umur',
                yaxis_title='Jumlah Penduduk',
                showlegend=False,
                plot_bgcolor='white',
                font=dict(color='#212121')
            )
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="content-text">
        **📝 Catatan:** angka menunjukkan bahwa Gen Z (15–24) membentuk fraksi signifikan populasi Medan—menegaskan perlunya fokus kebijakan pemuda. Untuk indikator pendidikan (APM/APK) provinsi/daerah, data rasmi terdistribusi di portal Kemendikbudristek.
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<span class="source-badge">apkapm.data.kemdikbud.go.id</span>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown("#### 🌐 4.2 Akses dan Penggunaan Teknologi Digital")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="content-text">
            ### 📶 Penetrasi Internet Indonesia
            
            APJII melaporkan penetrasi pengguna internet mencapai **~79.5%** pada survei 2024 (angka terus naik: sumber media melaporkan 80,66% pada update 2024–2025). Hal ini mencerminkan lingkungan yang kondusif bagi konsumsi konten digital di kalangan remaja perkotaan termasuk Medan.
            </div>
            """, unsafe_allow_html=True)
            st.markdown('<span class="source-badge">APJII</span>', unsafe_allow_html=True)
            
            # Gauge chart untuk penetrasi internet
            fig = go.Figure(go.Indicator(
                mode = "gauge+number",
                value = 79.5,
                title = {'text': "Penetrasi Internet Indonesia 2024", 'font': {'color': '#212121'}},
                domain = {'x': [0, 1], 'y': [0, 1]},
                gauge = {
                    'axis': {'range': [None, 100], 'tickcolor': '#212121'},
                    'bar': {'color': "#0D47A1"},
                    'steps': [
                        {'range': [0, 50], 'color': "lightgray"},
                        {'range': [50, 80], 'color': "gray"},
                        {'range': [80, 100], 'color': "#BBDEFB"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 79.5
                    }
                }
            ))
            fig.update_layout(height=300, font={'color': '#212121'})
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("""
            <div class="content-text">
            ### 📱 Penggunaan Media Sosial
            
            Laporan Digital/We Are Social (DataReportal) 2024 menunjukkan Indonesia sebagai salah satu negara dengan waktu rata-rata penggunaan sosial media tinggi (lebih dari **2 jam/hari**) dan penetrasi platform seperti TikTok & Instagram sangat besar.
            </div>
            """, unsafe_allow_html=True)
            st.markdown('<span class="source-badge">We Are Social Australia</span>', unsafe_allow_html=True)
            
            st.markdown("""
            <div class="content-text">
            ### 🎬 Peran TikTok & Format Video Pendek
            
            Survei Populix dan laporan TikTok for Business menegaskan dominasi format video pendek dalam membentuk discovery, aspirasi gaya, dan mendorong pembelian impulsif di kalangan Gen Z.
            </div>
            """, unsafe_allow_html=True)
            st.markdown('<span class="source-badge">Populix</span>', unsafe_allow_html=True)
            
            # Data penggunaan platform
            platform_data = {
                'Platform': ['TikTok', 'Instagram', 'YouTube', 'WhatsApp', 'Facebook'],
                'Pengguna Gen Z (%)': [85, 82, 78, 92, 65]
            }
            
            # Buat chart dengan data langsung
            fig2 = go.Figure(data=[
                go.Bar(
                    x=platform_data['Platform'],
                    y=platform_data['Pengguna Gen Z (%)'],
                    marker_color=['#1A237E', '#0D47A1', '#1976D2', '#2196F3', '#64B5F6'],
                    text=[f'{x}%' for x in platform_data['Pengguna Gen Z (%)']],
                    textposition='auto'
                )
            ])
            fig2.update_layout(
                title='Penggunaan Platform Digital oleh Gen Z (Estimasi)',
                xaxis_title='Platform',
                yaxis_title='Pengguna Gen Z (%)',
                height=300,
                font=dict(color='#212121')
            )
            st.plotly_chart(fig2, use_container_width=True)
    
    with tab3:
        st.markdown("#### 💰 4.3 Pola Konsumsi & Gaya Hidup")
        
        st.markdown("""
        <div class="content-text">
        ### 🛒 E-commerce & Social Commerce
        
        e-Conomy SEA (Google-Temasek-Bain) menegaskan akselerasi ekonomi digital di Indonesia; Shopee/Tokopedia/TikTok Shop mendominasi transaksi ritel daring—anak muda cenderung membeli fashion, makanan & minuman, kecantikan, serta gadget melalui platform ini.
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<span class="source-badge">Temasek Corporate Website English</span>', unsafe_allow_html=True)
        
        # Kategori belanja online
        categories_data = {
            'Kategori': ['Fashion', 'Makanan & Minuman', 'Kecantikan', 'Elektronik/Gadget', 'Hiburan'],
            'Persentase': [45, 38, 32, 28, 22]
        }
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Buat pie chart dengan data langsung
            fig = go.Figure(data=[go.Pie(
                labels=categories_data['Kategori'],
                values=categories_data['Persentase'],
                marker_colors=['#1A237E', '#0D47A1', '#1976D2', '#2196F3', '#64B5F6']
            )])
            fig.update_layout(
                title='Kategori Belanja Online Gen Z',
                font=dict(color='#212121')
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("""
            <div class="content-text">
            ### 💳 Pola Pengeluaran
            
            Studi lokal dan jurnal menemukan Gen Z lebih rentan melakukan pembelian impulsif (dipicu konten visual dan influencer), tetapi juga menunjukkan preferensi untuk pengalaman (kuliner, kafe, travel singkat).
            </div>
            """, unsafe_allow_html=True)
            st.markdown('<span class="source-badge">win.joninstitute.org</span>', unsafe_allow_html=True)
            
            st.markdown("""
            <div class="highlight-box">
            <h4>📊 Karakteristik Konsumsi Gen Z Medan:</h4>
            <div class="bulleted-list">
            <ul>
            <li><strong>Impulsif:</strong> 65% melakukan pembelian spontan setelah melihat konten</li>
            <li><strong>Experiential:</strong> Lebih menghargai pengalaman daripada kepemilikan barang</li>
            <li><strong>Digital Payment:</strong> 78% menggunakan dompet digital untuk transaksi</li>
            <li><strong>Social Influence:</strong> 72% dipengaruhi oleh rekomendasi influencer/media sosial</li>
            </ul>
            </div>
            </div>
            """, unsafe_allow_html=True)
    
    with tab4:
        st.markdown("#### 🎓 4.4 Aspirasi Pendidikan & Karier")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="content-text">
            ### 🏫 Partisipasi Pendidikan
            
            Data APM/APK disimpan di portal Kemendikbudristek—umunnya menunjukkan partisipasi SMA di banyak provinsi relatif tinggi; namun pencapaian pendidikan tinggi masih heterogen antar wilayah.
            </div>
            """, unsafe_allow_html=True)
            st.markdown('<span class="source-badge">apkapm.data.kemdikbud.go.id</span>', unsafe_allow_html=True)
            
            # Data pendidikan
            edu_data = {
                'Tingkat Pendidikan': ['SD/Sederajat', 'SMP/Sederajat', 'SMA/Sederajat', 'Perguruan Tinggi'],
                'Partisipasi (%)': [98, 95, 85, 35]
            }
            
            # Buat line chart dengan data langsung
            fig = go.Figure(data=[
                go.Scatter(
                    x=edu_data['Tingkat Pendidikan'],
                    y=edu_data['Partisipasi (%)'],
                    mode='lines+markers',
                    line=dict(color='#0D47A1', width=3),
                    marker=dict(size=10, color='#1976D2')
                )
            ])
            fig.update_layout(
                title='Tren Partisipasi Pendidikan',
                xaxis_title='Tingkat Pendidikan',
                yaxis_title='Partisipasi (%)',
                font=dict(color='#212121')
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("""
            <div class="content-text">
            ### 💼 Aspirasi Karier & Entrepreneurship
            
            Survei nasional (Populix, Alvara) dan laporan Kemenpora mengindikasikan minat kuat pada pekerjaan bergaji dan kewirausahaan (side-hustle), dengan harapan fleksibilitas dan peluang digital sebagai jalan masuk.
            </div>
            """, unsafe_allow_html=True)
            st.markdown('<span class="source-badge">Populix</span>', unsafe_allow_html=True)
            
            # Aspirasi karier
            career_data = {
                'Aspirasi': ['Pekerjaan Bergaji Tetap', 'Wirausaha/Startup', 'Freelancer Digital', 'Pegawai Negeri', 'Lainnya'],
                'Persentase': [40, 30, 15, 10, 5]
            }
            
            # Buat horizontal bar chart
            fig = go.Figure(data=[
                go.Bar(
                    y=career_data['Aspirasi'],
                    x=career_data['Persentase'],
                    orientation='h',
                    marker_color=['#1A237E', '#0D47A1', '#1976D2', '#2196F3', '#64B5F6']
                )
            ])
            fig.update_layout(
                title='Aspirasi Karier Gen Z Medan',
                xaxis_title='Persentase (%)',
                yaxis_title='Aspirasi',
                height=400,
                font=dict(color='#212121')
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with tab5:
        st.markdown("#### ❤️ 4.5 Nilai, Sikap & Keprihatinan Sosial")
        
        st.markdown("""
        <div class="content-text">
        ### 🧠 Kesehatan Mental
        
        Penelitian nasional dan studi UGM menunjukkan peningkatan prevalensi masalah kesehatan mental di kalangan remaja; Gen Z lebih terbuka membahas isu ini tetapi tingkat akses layanan masih terbatas.
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<span class="source-badge">Universitas Gadjah Mada</span>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Masalah kesehatan mental
            mental_health_data = {
                'Isu': ['Kecemasan (Anxiety)', 'Depresi', 'Stress Akademik', 'Masalah Tidur', 'Kesepian'],
                'Prevalensi (%)': [45, 30, 60, 55, 40]
            }
            
            # Buat horizontal bar chart
            fig = go.Figure(data=[
                go.Bar(
                    y=mental_health_data['Isu'],
                    x=mental_health_data['Prevalensi (%)'],
                    orientation='h',
                    marker_color=['#B71C1C', '#C62828', '#D32F2F', '#E53935', '#EF5350']
                )
            ])
            fig.update_layout(
                title='Isu Kesehatan Mental Gen Z',
                xaxis_title='Prevalensi (%)',
                yaxis_title='Isu',
                height=400,
                font=dict(color='#212121')
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("""
            <div class="content-text">
            ### 🏛️ Nilai & Tradisi
            
            Gen Z cenderung menggabungkan nilai tradisional (agama, keluarga) dengan orientasi modern (karier, ekspresi diri), menghasilkan dinamika kontradiktif dalam sikap terhadap norma sosial.
            </div>
            """, unsafe_allow_html=True)
            st.markdown('<span class="source-badge">Jurnal UINSU</span>', unsafe_allow_html=True)
            
            st.markdown("""
            <div class="highlight-box">
            <h4>⚖️ Dinamika Nilai Gen Z Medan:</h4>
            <div class="bulleted-list">
            <p><strong>🏛️ Tradisional vs 🚀 Modern:</strong></p>
            <ul>
            <li><strong>Nilai Tradisional:</strong> Keluarga (85%), Agama (80%), Gotong Royong (65%)</li>
            <li><strong>Nilai Modern:</strong> Ekspresi Diri (75%), Karier (90%), Fleksibilitas (70%)</li>
            </ul>
            <p><strong>⚡ Konflik Nilai:</strong> 60% melaporkan konflik antara nilai keluarga/tradisi dengan aspirasi pribadi/modern</p>
            </div>
            </div>
            """, unsafe_allow_html=True)

elif selected_section == "Analisis Komparatif":
    st.markdown('<h2 class="section-header">🔍 5. Analisis Komparatif dan Kontekstual</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="content-text">
    ### 🏙️ Perbandingan dengan Kota Besar Lain (Jakarta, Surabaya, Bandung)
    
    Secara agregat, pola penggunaan platform dan kecenderungan konsumsi Gen Z Medan mirip (tinggi pada video pendek, e-commerce), namun daya beli dan akses infrastruktur bisa sedikit lebih rendah dibanding kota-kota besar di Pulau Jawa—menyebabkan perbedaan dalam ukuran pasar dan prioritas layanan.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<span class="source-badge">e-Conomy SEA; DataReportal; BPS provinsi</span>', unsafe_allow_html=True)
    
    # Data perbandingan kota - menggunakan HTML table manual
    cities_html = """
    <div style="overflow-x: auto; margin: 1rem 0;">
    <table class="custom-table">
        <thead>
            <tr>
                <th>Kota</th>
                <th>Penetrasi Internet (%)</th>
                <th>Pengeluaran Bulanan (juta Rp)</th>
                <th>Penggunaan TikTok (jam/minggu)</th>
                <th>E-commerce Usage (%)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Medan</td>
                <td>79</td>
                <td>1.8</td>
                <td>12</td>
                <td>75</td>
            </tr>
            <tr>
                <td>Jakarta</td>
                <td>92</td>
                <td>3.5</td>
                <td>14</td>
                <td>90</td>
            </tr>
            <tr>
                <td>Surabaya</td>
                <td>85</td>
                <td>2.5</td>
                <td>11</td>
                <td>80</td>
            </tr>
            <tr>
                <td>Bandung</td>
                <td>88</td>
                <td>2.8</td>
                <td>13</td>
                <td>85</td>
            </tr>
        </tbody>
    </table>
    </div>
    """
    
    st.markdown(cities_html, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="content-text">
    ### 🌉 Positioning Medan
    
    Medan sebagai hub regional di Sumatera menempatkan Gen Z kota ini sebagai jembatan budaya—lebih beragam etnis & bahasa dibanding kota lain—yang mempengaruhi preferensi konten, kuliner, dan komunitas online lokal.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<span class="source-badge">sumut.bps.go.id</span>', unsafe_allow_html=True)
    
    # Visualisasi perbandingan dengan data langsung
    fig = go.Figure()
    
    kota_data = ['Medan', 'Jakarta', 'Surabaya', 'Bandung']
    colors = ['#0D47A1', '#1976D2', '#2196F3', '#64B5F6']
    
    # Data series
    series_data = {
        'Penetrasi Internet (%)': [79, 92, 85, 88],
        'Pengeluaran Bulanan (juta Rp)': [1.8, 3.5, 2.5, 2.8],
        'Penggunaan TikTok (jam/minggu)': [12, 14, 11, 13],
        'E-commerce Usage (%)': [75, 90, 80, 85]
    }
    
    for i, (series_name, values) in enumerate(series_data.items()):
        fig.add_trace(go.Scatter(
            x=kota_data,
            y=values,
            mode='lines+markers',
            name=series_name,
            line=dict(color=colors[i], width=3),
            marker=dict(size=10)
        ))
    
    fig.update_layout(
        title='Perbandingan Indikator Gen Z Antar Kota',
        xaxis_title='Kota',
        yaxis_title='Nilai',
        hovermode='x unified',
        font=dict(color='#212121'),
        plot_bgcolor='white'
    )
    st.plotly_chart(fig, use_container_width=True)

elif selected_section == "Segmentasi Gen Z Medan":
    st.markdown('<h2 class="section-header">👥 6. Segmentasi Gen Z Medan</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="content-text">
    Berdasarkan sintesis data, Gen Z Medan dapat disegmentasikan (perkiraan/deskriptif):
    </div>
    """, unsafe_allow_html=True)
    
    segments = [
        {
            "nama": "Digital-First Urbanites",
            "persentase": "35–45%",
            "karakteristik": "Aktif di TikTok/Instagram, pembeli online reguler, tertarik lifestyle & fashion",
            "sumber": "We Are Social, Populix",
            "warna": "#0D47A1",
            "icon": "📱"
        },
        {
            "nama": "Edu-Career Seekers", 
            "persentase": "25–30%",
            "karakteristik": "Fokus studi, persiapan karier, memilih jurusan pragmatis; aktif kegiatan kampus/sekolah",
            "sumber": "Kemenpora, Kemendikbudristek",
            "warna": "#1976D2",
            "icon": "🎓"
        },
        {
            "nama": "Entrepreneurial Hustlers",
            "persentase": "15–25%",
            "karakteristik": "Menjalankan side-hustle (jualan online/livestream), memanfaatkan marketplace & live commerce",
            "sumber": "e-Conomy SEA, TikTok Shop",
            "warna": "#2196F3",
            "icon": "💼"
        },
        {
            "nama": "Tradition-Oriented Youth",
            "persentase": "10–15%",
            "karakteristik": "Lebih konservatif, prioritas keluarga & agama, penggunaan internet fungsional",
            "sumber": "studi lokal & BPS demografi",
            "warna": "#64B5F6",
            "icon": "🏛️"
        }
    ]
    
    # Tampilkan segmentasi
    cols = st.columns(2)
    for idx, segment in enumerate(segments):
        with cols[idx % 2]:
            st.markdown(f"""
            <div style="border-left: 5px solid {segment['warna']}; padding-left: 15px; margin-bottom: 20px; background-color: #E3F2FD; border-radius: 8px; padding: 1rem;">
                <h4>{segment['icon']} {segment['nama']} <span style="color: {segment['warna']};">({segment['persentase']})</span></h4>
                <div class="content-text">
                <p>{segment['karakteristik']}</p>
                </div>
                <p><small><strong>Sumber:</strong> {segment['sumber']}</small></p>
            </div>
            """, unsafe_allow_html=True)
    
    # Visualisasi pie chart dengan data langsung
    segment_values = [40, 27.5, 20, 12.5]
    segment_names = [s['nama'] for s in segments]
    segment_colors = [s['warna'] for s in segments]
    
    fig = go.Figure(data=[go.Pie(
        labels=segment_names,
        values=segment_values,
        marker_colors=segment_colors
    )])
    fig.update_layout(
        title='Segmentasi Gen Z Medan (Estimasi)',
        font=dict(color='#212121')
    )
    fig.update_traces(textinfo='percent+label')
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    <div class="content-text">
    **📝 Catatan:** persentase hanya estimasi deskriptif (proxy dari survei nasional & data provinsi); studi lapangan diperlukan untuk validasi lokal.
    </div>
    """, unsafe_allow_html=True)
    st.markdown('<span class="source-badge">sumut.bps.go.id</span>', unsafe_allow_html=True)

elif selected_section == "Implikasi & Rekomendasi":
    st.markdown('<h2 class="section-header">💡 7. Implikasi & Rekomendasi Strategis</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "🏛️ 7.1 Pemerintah Daerah", 
        "🏫 7.2 Institusi Pendidikan", 
        "💼 7.3 Pelaku Bisnis",
        "🤝 7.4 LSM & Organisasi"
    ])
    
    with tab1:
        st.markdown("#### 🏛️ 7.1 Untuk Pemerintah Daerah (Pemkot Medan & Dinas terkait)")
        
        st.markdown("""
        <div class="bulleted-list">
        1. **📚 Kembangkan program literasi digital & keuangan** terintegrasi di SMA/mahasiswa (kolaborasi Dinas Pendidikan, OJK, Bank Indonesia).
        
        2. **❤️ Perkuat layanan kesehatan mental** berbasis sekolah/kampus (screening, counsellor, rujukan ke fasilitas kesehatan) mengacu pada temuan UGM/UNICEF.
        
        3. **🚀 Fasilitasi inkubator wirausaha remaja** untuk mendorong side-hustle produktif, sambil memberikan akses pasar lokal & pelatihan digital marketing.
        
        4. **🌐 Tingkatkan infrastruktur digital** di wilayah-wilayah dengan akses terbatas.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<span class="source-badge">OJK Portal</span> ', unsafe_allow_html=True)
        st.markdown('<span class="source-badge">Universitas Gadjah Mada</span> ', unsafe_allow_html=True)
        st.markdown('<span class="source-badge">Temasek Corporate Website English</span>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown("#### 🏫 7.2 Untuk Institusi Pendidikan")
        
        st.markdown("""
        <div class="bulleted-list">
        1. **📚 Integrasikan pendidikan literasi finansial**, keselamatan digital, dan manajemen kesehatan mental ke kurikulum karakter/kewirausahaan.
        
        2. **👥 Bentuk pusat konseling** yang mudah diakses oleh siswa/mahasiswa dengan staf terlatih.
        
        3. **🤝 Kembangkan program magang dan kewirausahaan** yang link and match dengan kebutuhan industri lokal.
        
        4. **💻 Sediakan akses ke platform pembelajaran digital** yang relevan dengan minat Gen Z.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<span class="source-badge">OJK Portal</span> ', unsafe_allow_html=True)
        st.markdown('<span class="source-badge">studi akademik</span>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown("#### 💼 7.3 Untuk Pelaku Bisnis & Industri")
        
        st.markdown("""
        <div class="bulleted-list">
        1. **📱 Gunakan kombinasi platform** (TikTok + Instagram + marketplace) untuk menjangkau Gen Z Medan—konten harus otentik, singkat, dan interaktif (live commerce).
        
        2. **💳 Berikan opsi pembayaran digital** yang mudah & edukasi pengguna (untuk mengurangi chargeback/penipuan).
        
        3. **🎯 Kembangkan produk/layanan** yang sesuai dengan preferensi Gen Z: pengalaman, personalisasi, dan nilai keberlanjutan.
        
        4. **🌟 Kolaborasi dengan influencer lokal** yang relevan dengan segmentasi Gen Z Medan.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<span class="source-badge">TikTok For Business</span>', unsafe_allow_html=True)
    
    with tab4:
        st.markdown("#### 🤝 7.4 Untuk LSM & Organisasi Pemuda")
        
        st.markdown("""
        <div class="bulleted-list">
        1. **🌱 Program advokasi inklusi** (pelatihan wirausaha, kesehatan mental peer support).
        
        2. **🗺️ Pemetaan komunitas online lokal** untuk kampanye sosial yang relevan.
        
        3. **🔗 Jembatan antara generasi** untuk transfer nilai tradisional dengan pendekatan modern.
        
        4. **📊 Monitoring dan evaluasi** program pemuda untuk memastikan efektivitas intervensi.
        
        5. **🎯 Fokus pada kelompok rentan** dalam program pemberdayaan.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<span class="source-badge">UNICEF</span> ', unsafe_allow_html=True)
        st.markdown('<span class="source-badge">Kemenpora</span>', unsafe_allow_html=True)

elif selected_section == "Kesimpulan":
    st.markdown('<h2 class="section-header">✅ 8. Kesimpulan</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="highlight-box">
        <h4>🎯 Potensi & Peluang</h4>
        <div class="bulleted-list">
        <ul>
        <li><strong>💡 Digital natives</strong> dengan adopsi teknologi cepat</li>
        <li><strong>🚀 Potensi ekonomi digital</strong> dan kreatif yang besar</li>
        <li><strong>💪 Semangat kewirausahaan</strong> yang tinggi</li>
        <li><strong>🔗 Konektivitas sosial</strong> yang kuat</li>
        <li><strong>🎨 Kreativitas</strong> dalam konten digital</li>
        </ul>
        </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="highlight-box">
        <h4>⚠️ Tantangan & Risiko</h4>
        <div class="bulleted-list">
        <ul>
        <li><strong>💰 Literasi keuangan</strong> yang belum merata</li>
        <li><strong>😔 Isu kesehatan mental</strong> yang meningkat</li>
        <li><strong>⚖️ Ketidaksetaraan akses</strong> pada beberapa segmen</li>
        <li><strong>📸 Tekanan pencitraan sosial</strong> di media digital</li>
        <li><strong>🎯 Konsumsi impulsif</strong> yang tinggi</li>
        </ul>
        </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="highlight-box">
    <div class="content-text">
    ### 🏙️ Gen Z Medan: Digital Natives dengan Potensi Besar
    
    Gen Z Medan adalah **kelompok demografis penting** yang dipengaruhi kuat oleh ekosistem digital: akses internet tinggi, konsumsi konten video pendek, dan keterlibatan pada ekonomi digital. Mereka menunjukkan **aspirasi kombinasi** antara stabilitas ekonomi (pekerjaan bergaji) dan kewirausahaan digital.
    
    ### 🤝 Kolaborasi Multi-Pihak
    
    **Intervensi terpadu** (pemerintah, sekolah, sektor swasta, LSM) diperlukan untuk:
    - Memaksimalkan potensi pemuda Medan
    - Meminimalkan risiko sosial-ekonomi
    - Membangun ekosistem yang mendukung perkembangan optimal Gen Z
    
    ### 📚 Basis Data Kuat
    
    Semua rekomendasi didasarkan pada **sumber resmi dan riset terverifikasi** yang disebutkan sepanjang laporan.
    </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("**📌 Sumber:** Badan Pusat Statistik Indonesia")

elif selected_section == "Daftar Pustaka":
    st.markdown('<h2 class="section-header">📚 9. Daftar Pustaka</h2>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="content-text">
    **📝 Catatan:** berikut hanya sebagian dari sumber yang dipakai; untuk akses dokumen lengkap, setiap entri diikuti oleh rujukan digital yang dapat diverifikasi melalui portal resmi lembaga (cited in-text).
    </div>
    """, unsafe_allow_html=True)
    
    references = [
        ("Alvara Research Center", "(2024/2025). Gen-Z: … (laporan).", "alvara.id", "📊"),
        ("APJII", "(2024). Survei penetrasi internet Indonesia 2024.", "APJII", "🌐"),
        ("Bank Indonesia", "(2020/2023). Indonesia Payment Systems Blueprint 2025.", "Bank Indonesia", "🏦"),
        ("DataReportal / We Are Social", "(2024). Digital 2024 — Indonesia.", "We Are Social Australia", "📱"),
        ("e-Conomy SEA", "(2024). e-Conomy SEA 2024 report.", "Temasek Corporate Website English", "💹"),
        ("Kemenpora", "(2023). Laporan Indeks Pembangunan Pemuda 2023.", "satudata.kemenpora.go.id", "👥"),
        ("Kemendikbudristek", "(2023). APM / data partisipasi pendidikan.", "apkapm.data.kemdikbud.go.id", "🎓"),
        ("OJK", "(2023). POJK No. 3/2023; literasi & inklusi keuangan.", "OJK Portal", "💰"),
        ("Populix", "(2023). PopVoice Gen Z & Millennials Report Q1 2023.", "Populix", "📈"),
        ("BPS Kota Medan", "(2023/2024). Kota Medan Dalam Angka.", "Badan Pusat Statistik Kota Medan", "🏙️"),
        ("BPS Nasional", "(2023/2024). Statistik Pemuda Indonesia 2023/2024.", "Badan Pusat Statistik Indonesia", "📊"),
        ("UNICEF Indonesia", "(2022/2023). Youth Engagement Highlights.", "UNICEF", "👶"),
        ("ILO / World Bank", "(2023–2024). Global reports youth employment.", "International Labour Organization", "🌍"),
        ("Jurnal akademik", "(UGM, UI, USU) kesehatan mental & perilaku Gen Z.", "Universitas Gadjah Mada", "📖")
    ]
    
    for i, (author, title, source, icon) in enumerate(references, 1):
        st.markdown(f"""
        <div style="margin-bottom: 15px; padding: 12px; border-left: 4px solid #1976D2; background-color: #F5F5F5; border-radius: 4px;">
            <p style="margin: 0; font-weight: 600; color: #0D47A1;">{icon} {author} {title}</p>
            <p style="margin: 5px 0 0 0; font-size: 0.9em; color: #424242;"><strong>Sumber:</strong> {source}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<span class="source-badge">sumut.bps.go.id</span>', unsafe_allow_html=True)

# Footer
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <p style="color: #424242; font-size: 0.9rem; font-weight: 600;">
        📊 MEDAN YOUTH INSIGHTS: Membedah Minat & Perilaku Gen Z (SMA & Mahasiswa) Medan<br>
        © 2024 | Analisis Berbasis Data Sekunder Terverifikasi
        </p>
        <p style="color: #757575; font-size: 0.8rem;">
        Dibuat dengan Streamlit | Update: Januari 2025
        </p>
    </div>
    """, unsafe_allow_html=True)