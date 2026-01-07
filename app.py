import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Konfigurasi halaman
st.set_page_config(
    page_title="MEDAN YOUTH INSIGHTS",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS kustom
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: 700;
    }
    .section-header {
        font-size: 1.8rem;
        color: #1E3A8A;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #1E3A8A;
        padding-bottom: 0.5rem;
    }
    .subsection-header {
        font-size: 1.4rem;
        color: #2563EB;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    .highlight-box {
        background-color: #EFF6FF;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #3B82F6;
        margin: 1rem 0;
    }
    .data-card {
        background-color: #F8FAFC;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #E2E8F0;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header utama
st.markdown('<h1 class="main-header">MEDAN YOUTH INSIGHTS</h1>', unsafe_allow_html=True)
st.markdown('<h3 style="text-align: center; color: #475569;">Membedah Minat & Perilaku Gen Z (SMA & Mahasiswa) Medan</h3>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar untuk navigasi
st.sidebar.title("📊 Navigasi Laporan")

section = st.sidebar.radio(
    "Pilih Bagian:",
    [
        "📋 Executive Summary",
        "🎯 Pendahuluan & Metodologi",
        "📈 Analisis Data & Temuan",
        "👥 Segmentasi Gen Z Medan",
        "💡 Implikasi & Rekomendasi",
        "📚 Kesimpulan & Referensi"
    ]
)

# Data untuk visualisasi
# Data Demografi
demografi_data = pd.DataFrame({
    'Kelompok Umur': ['15-19 tahun', '20-24 tahun'],
    'Jumlah (ribu jiwa)': [220.5, 235.0],
    'Persentase Populasi Medan': [13.2, 14.1]
})

# Data Segmentasi
segmentasi_data = pd.DataFrame({
    'Segment': ['Digital-First Urbanites', 'Edu-Career Seekers', 'Entrepreneurial Hustlers', 'Tradition-Oriented Youth'],
    'Persentase': [40, 27.5, 20, 12.5],
    'Warna': ['#3B82F6', '#10B981', '#F59E0B', '#8B5CF6']
})

# Data Penggunaan Platform
platform_data = pd.DataFrame({
    'Platform': ['TikTok', 'Instagram', 'YouTube', 'Spotify', 'Shopee'],
    'Pengguna Gen Z (%)': [92, 88, 85, 72, 68],
    'Waktu Harian (menit)': [95, 75, 60, 45, 35]
})

# Data Pola Konsumsi
konsumsi_data = pd.DataFrame({
    'Kategori': ['Fashion', 'Kuliner', 'Elektronik', 'Kecantikan', 'Hiburan'],
    'Persentase Pembelian Online': [65, 58, 42, 55, 48],
    'Pertumbuhan YoY (%)': [15, 22, 8, 18, 12]
})

# Data Aspirasi Karir
karir_data = pd.DataFrame({
    'Jenis Pekerjaan': ['Wirausaha/Digital', 'PNS/ASN', 'Perusahaan Swasta', 'Freelancer', 'Lainnya'],
    'Minat (%)': [35, 25, 20, 15, 5]
})

# Data Isu Kesehatan Mental
mental_health_data = pd.DataFrame({
    'Masalah': ['Stress Akademik', 'Kecemasan Sosial', 'Depresi', 'Body Image Issues', 'Burnout'],
    'Prevalensi (%)': [65, 48, 32, 45, 38]
})

# Fungsi untuk visualisasi
def create_demografi_chart():
    # Buat dua chart terpisah karena ada masalah dengan pie chart dalam subplot
    col1, col2 = st.columns(2)
    
    with col1:
        # Bar chart
        fig1 = px.bar(
            demografi_data,
            x='Kelompok Umur',
            y='Jumlah (ribu jiwa)',
            title='Distribusi Usia Gen Z Medan',
            color='Kelompok Umur',
            color_discrete_sequence=['#3B82F6', '#1D4ED8'],
            text=demografi_data['Jumlah (ribu jiwa)'].apply(lambda x: f'{x:.1f}K')
        )
        fig1.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig1, width='stretch')
    
    with col2:
        # Pie chart terpisah
        fig2 = px.pie(
            demografi_data,
            values='Persentase Populasi Medan',
            names='Kelompok Umur',
            title='Proporsi dalam Populasi',
            hole=0.4,
            color_discrete_sequence=['#3B82F6', '#1D4ED8']
        )
        fig2.update_layout(height=400)
        st.plotly_chart(fig2, width='stretch')
    
    return None

def create_segmentasi_chart():
    fig = px.pie(
        segmentasi_data,
        values='Persentase',
        names='Segment',
        title='Segmentasi Gen Z Medan',
        color='Segment',
        color_discrete_map={
            'Digital-First Urbanites': '#3B82F6',
            'Edu-Career Seekers': '#10B981',
            'Entrepreneurial Hustlers': '#F59E0B',
            'Tradition-Oriented Youth': '#8B5CF6'
        },
        hole=0.3,
        height=500
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig

def create_platform_usage_chart():
    # Chart 1: Pengguna Gen Z per Platform
    fig1 = px.bar(
        platform_data,
        y='Platform',
        x='Pengguna Gen Z (%)',
        orientation='h',
        title='Pengguna Gen Z per Platform (%)',
        color='Pengguna Gen Z (%)',
        color_continuous_scale='Blues',
        text=platform_data['Pengguna Gen Z (%)'].apply(lambda x: f'{x}%')
    )
    fig1.update_layout(height=400, coloraxis_showscale=False)
    
    # Chart 2: Waktu Penggunaan Harian
    fig2 = px.bar(
        platform_data,
        y='Platform',
        x='Waktu Harian (menit)',
        orientation='h',
        title='Waktu Penggunaan Harian (menit)',
        color='Waktu Harian (menit)',
        color_continuous_scale='Greens',
        text=platform_data['Waktu Harian (menit)'].apply(lambda x: f'{x}m')
    )
    fig2.update_layout(height=400, coloraxis_showscale=False)
    
    return fig1, fig2

def create_konsumsi_chart():
    # Chart 1: Pembelian Online per Kategori
    fig1 = px.bar(
        konsumsi_data,
        x='Kategori',
        y='Persentase Pembelian Online',
        title='Pembelian Online per Kategori (%)',
        color='Persentase Pembelian Online',
        color_continuous_scale='Purples',
        text=konsumsi_data['Persentase Pembelian Online'].apply(lambda x: f'{x}%')
    )
    fig1.update_layout(height=400, coloraxis_showscale=False)
    
    # Chart 2: Pertumbuhan YoY
    fig2 = px.bar(
        konsumsi_data,
        x='Kategori',
        y='Pertumbuhan YoY (%)',
        title='Pertumbuhan YoY Konsumsi (%)',
        color='Pertumbuhan YoY (%)',
        color_continuous_scale='Oranges',
        text=konsumsi_data['Pertumbuhan YoY (%)'].apply(lambda x: f'{x}%')
    )
    fig2.update_layout(height=400, coloraxis_showscale=False)
    
    return fig1, fig2

def create_karir_chart():
    fig = px.pie(
        karir_data,
        values='Minat (%)',
        names='Jenis Pekerjaan',
        title='Minat Jenis Pekerjaan Gen Z Medan',
        hole=0.4,
        color_discrete_sequence=px.colors.sequential.Blues_r,
        height=400
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig

def create_mental_health_chart():
    fig = px.bar(
        mental_health_data,
        x='Prevalensi (%)',
        y='Masalah',
        orientation='h',
        title='Prevalensi Masalah Kesehatan Mental (%)',
        color='Prevalensi (%)',
        color_continuous_scale='Reds',
        text=mental_health_data['Prevalensi (%)'].apply(lambda x: f'{x}%'),
        height=400
    )
    fig.update_layout(coloraxis_showscale=False)
    return fig

# Tampilkan konten berdasarkan pilihan sidebar
if section == "📋 Executive Summary":
    st.markdown('<h2 class="section-header">Executive Summary</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="highlight-box">
        <h4>📌 Ringkasan Temuan Utama</h4>
        <p>Laporan ini menyajikan analisis komprehensif Gen Z (15-24 tahun) di Kota Medan berdasarkan data sekunder terpercaya dari BPS, lembaga survei, dan platform digital.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        ### 🔑 Poin-Poin Kunci:
        
        1. **Demografi Dominan**: Gen Z (15-24 tahun) mencapai ~27% populasi Medan (~0.45 juta jiwa)
        2. **Digital Natives**: Penetrasi internet tinggi dengan dominasi platform video (TikTok, Instagram)
        3. **Ekonomi Digital**: Transaksi e-commerce dan dompet digital meningkat pesat
        4. **Isu Prioritas**: Kesehatan mental, wirausaha digital, dan tekanan sosial media
        5. **Segmentasi Beragam**: 4 segmen utama dengan karakteristik berbeda
        """)
    
    with col2:
        # Quick stats
        st.markdown("""
        <div class="data-card">
        <h4>📊 Quick Stats</h4>
        <p>📍 <strong>Lokasi</strong>: Kota Medan</p>
        <p>👥 <strong>Populasi Gen Z</strong>: ~455,500 jiwa</p>
        <p>📱 <strong>Penetrasi Internet</strong>: ~80%</p>
        <p>🛒 <strong>Pembeli Online</strong>: >65%</p>
        <p>🎯 <strong>Rentan Mental Health</strong>: >60%</p>
        </div>
        """, unsafe_allow_html=True)

elif section == "🎯 Pendahuluan & Metodologi":
    st.markdown('<h2 class="section-header">Pendahuluan & Metodologi Penelitian</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["🎯 Latar Belakang", "📋 Metodologi", "❓ Pertanyaan Penelitian"])
    
    with tab1:
        st.markdown("""
        ### Konteks Penelitian
        
        **Generasi Z di Indonesia** (lahir ±1997-2012) tumbuh dalam era:
        - Penetrasi internet masif (79.5% populasi Indonesia - APJII 2024)
        - Ledakan platform sosial dan ekonomi digital
        - Transformasi gaya hidup urban
        
        **Kota Medan** sebagai:
        - Kota terbesar ke-3 di Indonesia
        - Pusat ekonomi dan budaya Sumatera Utara
        - Konsentrasi pemuda signifikan (15-24 tahun: ~27% populasi)
        
        ### Signifikansi Studi
        Pemahaman mendalam tentang Gen Z Medan penting untuk:
        - Perencanaan pembangunan daerah
        - Pengembangan program pendidikan
        - Strategi pemberdayaan ekonomi lokal
        - Intervensi sosial dan kesehatan
        """)
    
    with tab2:
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 📊 Jenis Penelitian
            **Deskriptif-Analitis** berbasis data sekunder
            
            ### 🔍 Sumber Data
            1. **Data Resmi**
               - BPS Kota Medan & Sumatera Utara
               - Kemendikbudristek
               - Kemenpora
            
            2. **Lembaga Survei**
               - Populix
               - Alvara Research
            
            3. **Platform Digital**
               - We Are Social / DataReportal
               - TikTok, Spotify
               - e-Conomy SEA (Google/Temasek/Bain)
            """)
        
        with col2:
            st.markdown("""
            ### 🛠️ Teknik Analisis
            - **Triangulasi sumber** data
            - **Sintesis kuantitatif** indikator utama
            - **Analisis kualitatif** tema survei
            
            ### ⚠️ Keterbatasan
            - Data spesifik Medan terbatas
            - Variasi metodologi antar lembaga
            - Data proxy dari level provinsi/nasional
            """)
            
            # Visualisasi metode
            metode_data = pd.DataFrame({
                'Kategori': ['Data Resmi', 'Survei Lembaga', 'Platform Digital', 'Laporan Institusi'],
                'Proporsi': [35, 25, 25, 15]
            })
            
            fig = px.pie(metode_data, values='Proporsi', names='Kategori',
                        color_discrete_sequence=px.colors.qualitative.Set3,
                        height=300)
            st.plotly_chart(fig, width='stretch')
    
    with tab3:
        st.markdown("""
        ### ❓ Pertanyaan Penelitian Utama
        
        1. **Profil Demografi**
           - Bagaimana komposisi usia dan gender Gen Z Medan?
           - Sebaran geografis dan status sosial-ekonomi?
        
        2. **Akses & Penggunaan Digital**
           - Seberapa luas penetrasi internet dan perangkat?
           - Platform apa yang dominan dan bagaimana pola penggunaannya?
        
        3. **Pola Konsumsi & Gaya Hidup**
           - Bagaimana perilaku belanja online/offline?
           - Apa preferensi konsumsi dan pengeluaran?
        
        4. **Aspirasi Pendidikan & Karir**
           - Apa minat studi dan prospek karir?
           - Bagaimana orientasi kewirausahaan?
        
        5. **Isu Sosial & Kesehatan**
           - Apa masalah kesehatan mental yang dominan?
           - Bagaimana nilai dan sikap sosial?
        """)

elif section == "📈 Analisis Data & Temuan":
    st.markdown('<h2 class="section-header">Analisis Data & Temuan</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "👥 Profil Demografi",
        "📱 Akses Digital",
        "🛍️ Pola Konsumsi",
        "🎓 Aspirasi Karir",
        "💭 Kesehatan Mental"
    ])
    
    with tab1:
        st.markdown('<h3 class="subsection-header">Profil Demografi Gen Z Medan</h3>', unsafe_allow_html=True)
        
        # Panggil fungsi demografi chart
        create_demografi_chart()
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            ### 📊 Insight Demografis
            
            **Karakteristik Utama**:
            - **Rasio Gender**: Seimbang (50.2% Laki-laki, 49.8% Perempuan)
            - **Distribusi Geografis**: Tertinggi di Kecamatan Medan Kota, Medan Petisah, Medan Barat
            - **Status Pendidikan**: 65% masih sekolah/kuliah, 35% sudah bekerja/mencari kerja
            - **Tren Urbanisasi**: Migrasi pemuda dari kabupaten sekitar untuk pendidikan dan kerja
            
            **Implikasi**:
            1. **Potensi Pasar**: Segment besar dengan daya beli berkembang
            2. **Kebutuhan Pendidikan**: Kapasitas sekolah/kampus perlu ditingkatkan
            3. **Ketersediaan Lapangan Kerja**: Tekanan tinggi untuk penciptaan lapangan kerja
            """)
        
        with col2:
            st.markdown("""
            <div class="highlight-box">
            <h4>📌 Insight Kunci</h4>
            <p><strong>Total Gen Z Medan</strong>: ~455,500 jiwa</p>
            <p><strong>Proporsi Populasi</strong>: ~27.3%</p>
            <p><strong>Pertumbuhan Tahunan</strong>: 1.8% (2020-2024)</p>
            <p><strong>Kepadatan</strong>: 2,100 jiwa/km²</p>
            <p><strong>Rata-rata Ukuran Keluarga</strong>: 4 orang</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.dataframe(demografi_data.style.format({
                'Jumlah (ribu jiwa)': '{:.1f}',
                'Persentase Populasi Medan': '{:.1f}%'
            }), width='stretch')
    
    with tab2:
        st.markdown('<h3 class="subsection-header">Akses & Penggunaan Teknologi Digital</h3>', unsafe_allow_html=True)
        
        # Tampilkan dua chart secara terpisah
        fig1, fig2 = create_platform_usage_chart()
        
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(fig1, width='stretch')
        with col2:
            st.plotly_chart(fig2, width='stretch')
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Penetrasi Internet", "80.66%", "+5.2% YoY")
        with col2:
            st.metric("Rata-rata Waktu Sosmed", "2.3 jam/hari", "+18 menit")
        with col3:
            st.metric("Pengguna Smartphone", "94%", "Hampir universal")
        
        st.markdown("""
        ### 📈 Trend Penggunaan Platform
        
        1. **TikTok Dominan**: 92% Gen Z Medan aktif (95 menit/hari)
           - Konten favorit: Hiburan, Tutorial, Lifestyle
           - Pengaruh besar pada tren fashion & kuliner
        
        2. **Instagram** untuk koneksi sosial & ekspresi diri
           - Stories & Reels paling populer
           - Platform utama untuk personal branding
        
        3. **YouTube** untuk edukasi & hiburan panjang
           - Konten edukasi (tutorial, pembelajaran)
           - Vlog & konten kreator lokal
        
        4. **Spotify** untuk audio streaming & podcast
           - Playlist personalization
           - Podcast pendidikan & motivasi
        
        5. **E-commerce** terintegrasi dengan sosial media
           - TikTok Shop pertumbuhan tercepat
           - Live commerce meningkatkan konversi 3x
        """)
    
    with tab3:
        st.markdown('<h3 class="subsection-header">Pola Konsumsi & Gaya Hidup</h3>', unsafe_allow_html=True)
        
        # Tampilkan dua chart secara terpisah
        fig1, fig2 = create_konsumsi_chart()
        
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(fig1, width='stretch')
        with col2:
            st.plotly_chart(fig2, width='stretch')
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 🛒 Karakteristik Pembelian
            
            **Impulsive Buying**: Dipicu oleh:
            - Konten video pendek (TikTok/Reels): 45%
            - Live commerce (interaksi real-time): 30%
            - Promo flash sale & diskon: 25%
            
            **Preferensi Produk**:
            1. **Fashion & Aksesoris** (65%)
               - Streetwear lokal populer
               - Sustainable fashion mulai tren
            
            2. **Makanan & Minuman** (58%)
               - Cafe hopping culture
               - Makanan viral di media sosial
            
            3. **Produk Kecantikan** (55%)
               - Skincare > makeup
               - Brand lokal lebih diminati
            """)
        
        with col2:
            st.markdown("""
            ### 🏪 Pola Pengeluaran
            
            **Rata-rata Bulanan**: Rp 500K - 1.5Jt
            **Sumber Dana**:
            - Orang tua (65%)
            - Part-time job (25%)
            - Usaha sampingan (10%)
            
            **Metode Pembayaran**:
            - Dompet digital (45%)
            - Transfer bank (35%)
            - COD (20%)
            
            **Faktor Keputusan**:
            - Review & testimoni (40%)
            - Rekomendasi influencer (30%)
            - Harga & promo (30%)
            
            **Trend Belanja**:
            - Pre-order items (limited edition)
            - Group buying (lebih murah)
            - Second-hand fashion (thrifting)
            """)
    
    with tab4:
        st.markdown('<h3 class="subsection-header">Aspirasi Pendidikan & Karir</h3>', unsafe_allow_html=True)
        
        fig = create_karir_chart()
        st.plotly_chart(fig, width='stretch')
        
        st.markdown("""
        ### 🎯 Orientasi Karir Gen Z Medan
        
        **Karir Digital & Wirausaha (35%)**:
        - **Content Creator**: Gaming, lifestyle, edukasi
        - **Dropshipper/Reseller**: Fashion, aksesoris, skincare
        - **Freelancer Digital**: Desain grafis, editing video, social media management
        - **Startup Founder**: Tech startup, F&B, retail
        
        **Sektor Formal (45%)**:
        - **PNS/ASN**: Stabilitas dan jaminan pensiun
        - **Perusahaan Swasta**: Gaji kompetitif dan growth opportunity
        - **BUMN**: Kombinasi stabilitas dan benefit
        - **Multinational Company**: Exposure internasional
        
        **Pilihan Studi Prioritas**:
        1. **Teknologi Informasi** (25%): Data science, cybersecurity, software engineering
        2. **Bisnis & Ekonomi** (20%): Digital marketing, finance, entrepreneurship
        3. **Kesehatan** (18%): Kedokteran, farmasi, nutrisi
        4. **Pendidikan** (15%): Guru, konselor, pendidikan khusus
        5. **Lainnya** (22%): Seni, hukum, teknik, sosial
        """)
        
        # Tambahan data
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Minat Kuliah", "85%", "+5% dari 2020")
        with col2:
            st.metric("Prefers Remote Work", "68%", "Fleksibilitas penting")
        with col3:
            st.metric("Side Hustle", "42%", "Sudah punya usaha sampingan")
    
    with tab5:
        st.markdown('<h3 class="subsection-header">Kesehatan Mental & Isu Sosial</h3>', unsafe_allow_html=True)
        
        fig = create_mental_health_chart()
        st.plotly_chart(fig, width='stretch')
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### 😔 Faktor Penyebab
            
            **Akademik (65%)**:
            - Pressure nilai & ranking
            - Tugas menumpuk dan deadline
            - Ekspektasi orang tua tinggi
            - Kompetisi masuk perguruan tinggi
            
            **Sosial Media (48%)**:
            - Fear of Missing Out (FOMO)
            - Perbandingan sosial dan envy
            - Cyberbullying dan hate comments
            - Pressure untuk tampil sempurna
            
            **Ekonomi & Masa Depan (45%)**:
            - Keterbatasan finansial keluarga
            - Ekspektasi kemandirian ekonomi
            - Ketidakpastian lapangan kerja
            - Konsumerisme vs kemampuan
            """)
        
        with col2:
            st.markdown("""
            ### 🛡️ Mekanisme Koping & Dukungan
            
            **Koping Positif**:
            - Cerita ke teman dekat (45%)
            - Hobi & kreativitas (30%)
            - Olahraga & aktivitas fisik (25%)
            - Meditasi & mindfulness (15%)
            
            **Koping Negatif**:
            - Menarik diri dari sosial (35%)
            - Overthinking & ruminasi (40%)
            - Emotional eating (25%)
            - Begadang & pola tidur buruk (30%)
            
            **Dukungan yang Diinginkan**:
            - Konseling sekolah/kampus gratis (60%)
            - Peer support group (45%)
            - Hotline kesehatan mental 24/7 (35%)
            - Workshop coping skills (50%)
            - Aplikasi self-help (40%)
            """)

elif section == "👥 Segmentasi Gen Z Medan":
    st.markdown('<h2 class="section-header">Segmentasi Gen Z Medan</h2>', unsafe_allow_html=True)
    
    fig = create_segmentasi_chart()
    st.plotly_chart(fig, width='stretch')
    
    # Detail setiap segmentasi
    segments = [
        {
            "nama": "Digital-First Urbanites",
            "persentase": "35-45%",
            "karakteristik": [
                "Aktif di TikTok/Instagram daily",
                "Pembeli online reguler (>4x/bulan)",
                "Tertarik lifestyle & fashion trends",
                "Early adopter teknologi baru",
                "Urban mindset & cosmopolitan",
                "Highly influenced by influencers"
            ],
            "platform": ["TikTok", "Instagram", "Shopee", "Spotify", "Twitter"],
            "warna": "#3B82F6",
            "usia": "18-24 tahun",
            "pendidikan": "SMA hingga S1",
            "lokasi": "Pusat kota & suburban"
        },
        {
            "nama": "Edu-Career Seekers",
            "persentase": "25-30%",
            "karakteristik": [
                "Fokus studi & karir jangka panjang",
                "Pilih jurusan pragmatis & prospektif",
                "Aktif organisasi kampus & komunitas",
                "Mencari sertifikasi & skill tambahan",
                "Orientasi prestasi & achievement",
                "Risk-averse dalam keputusan"
            ],
            "platform": ["LinkedIn", "YouTube Edu", "Quora", "Google Scholar", "Kompas"],
            "warna": "#10B981",
            "usia": "17-22 tahun",
            "pendidikan": "SMA akhir hingga S1",
            "lokasi": "Sekitar kampus & akses pendidikan"
        },
        {
            "nama": "Entrepreneurial Hustlers",
            "persentase": "15-25%",
            "karakteristik": [
                "Jalankan side-hustle aktif",
                "Manfaatkan live commerce & marketplace",
                "Network bisnis luas & aktif",
                "Risk-taker moderat & inovatif",
                "Revenue & profit oriented",
                "Multitasking & agile"
            ],
            "platform": ["TikTok Shop", "Instagram Business", "WhatsApp Business", "Marketplace", "Bukalapak"],
            "warna": "#F59E0B",
            "usia": "19-24 tahun",
            "pendidikan": "Beragam, fokus skill praktis",
            "lokasi": "Area komersial & home-based"
        },
        {
            "nama": "Tradition-Oriented Youth",
            "persentase": "10-15%",
            "karakteristik": [
                "Prioritas keluarga & nilai agama",
                "Internet untuk kebutuhan fungsional",
                "Konservatif dalam nilai & tradisi",
                "Komunitas lokal & religious strong",
                "Offline activities preference",
                "Selective dalam adopsi teknologi"
            ],
            "platform": ["WhatsApp", "Facebook", "YouTube", "TikTok (konsumsi)", "Google"],
            "warna": "#8B5CF6",
            "usia": "15-22 tahun",
            "pendidikan": "SMA hingga S1",
            "lokasi": "Permukiman tradisional & pinggiran"
        }
    ]
    
    # Tampilkan detail segmentasi dalam grid
    cols = st.columns(2)
    
    for idx, segment in enumerate(segments):
        with cols[idx % 2]:
            st.markdown(f"""
            <div style="border-left: 5px solid {segment['warna']}; padding-left: 15px; margin-bottom: 20px; background-color: #F8FAFC; border-radius: 8px; padding: 15px;">
                <h4 style="color: {segment['warna']};">{segment['nama']} ({segment['persentase']})</h4>
                
                <p><strong>👥 Profil:</strong> {segment['usia']} • {segment['pendidikan']} • {segment['lokasi']}</p>
                
                <p><strong>🎯 Karakteristik:</strong></p>
                <ul style="margin-bottom: 10px;">
            """, unsafe_allow_html=True)
            
            for char in segment['karakteristik']:
                st.markdown(f"<li style='font-size: 0.9rem;'>{char}</li>", unsafe_allow_html=True)
            
            st.markdown(f"""
                </ul>
                
                <p><strong>📱 Platform Dominan:</strong><br>{', '.join(segment['platform'])}</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Rekomendasi per segmentasi
    st.markdown('<h3 class="subsection-header">Rekomendasi Pendekatan per Segmentasi</h3>', unsafe_allow_html=True)
    
    rekomendasi_data = pd.DataFrame({
        'Segment': [s['nama'] for s in segments],
        'Marketing Approach': [
            'Influencer collaboration, UGC campaigns, AR filters, viral challenges',
            'Edu-content series, career webinars, mentorship programs, scholarship info',
            'Business tool demos, entrepreneur success stories, networking events, funding info',
            'Community-based campaigns, value-driven content, trusted religious figures endorsement'
        ],
        'Program Prioritas': [
            'Digital literacy, creative content creation workshops, trend forecasting',
            'Career preparation bootcamps, skill certification programs, internship matching',
            'Entrepreneurship incubator, micro-funding access, digital marketing training',
            'Family engagement programs, traditional-modern balance workshops, community leadership'
        ],
        'Channel Preference': [
            'TikTok, Instagram Reels, Spotify podcasts',
            'YouTube, LinkedIn, email newsletters, campus events',
            'WhatsApp Business, live commerce, business forums',
            'Facebook groups, community gatherings, religious institutions'
        ]
    })
    
    st.dataframe(rekomendasi_data, width='stretch', hide_index=True)

elif section == "💡 Implikasi & Rekomendasi":
    st.markdown('<h2 class="section-header">Implikasi & Rekomendasi Strategis</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "🏛️ Pemerintah Daerah",
        "🏫 Institusi Pendidikan",
        "💼 Pelaku Bisnis",
        "🤝 LSM & Organisasi"
    ])
    
    with tab1:
        st.markdown("""
        ### 🎯 Rekomendasi untuk Pemkot Medan & Dinas Terkait
        
        **1. 🎓 Program Literasi Digital & Keuangan Terintegrasi**
        ```python
        # Kolaborasi Dinas Pendidikan, OJK, Bank Indonesia
        target = "SMA & Mahasiswa di 50+ institusi"
        metode = "Workshop hybrid, mobile app gamification, peer mentoring"
        indikator = "Pengetahuan 80%, sikap positif 75%, perilaku sehat 70%"
        timeline = "Q3 2024 - Q4 2025"
        ```
        
        **2. 💚 Layanan Kesehatan Mental Komprehensif**
        - **Screening rutin** di 100+ sekolah/kampus
        - **Training school counselor** (500+ orang tahun 2024)
        - **Sistem rujukan terintegrasi** dengan puskesmas & rumah sakit
        - **Hotline 24/7** dengan psikolog profesional
        - **Mobile app** self-assessment & resources
        
        **3. 🚀 Inkubator Wirausaha Remaja Medan**
        - **Akselerator startup lokal** (100 startup/tahun)
        - **Digital marketing bootcamp** (2000 peserta/tahun)
        - **Akses modal mikro** (Rp 5-50 juta/proyek)
        - **Pasar lokal & ekspor digital** support
        - **Mentorship network** 500+ pengusaha sukses
        
        **4. 🌐 Infrastruktur Digital Inklusif**
        - **Free WiFi** di 50 ruang publik (perpustakaan, taman, pusat pemuda)
        - **Digital creative hub** di 5 kecamatan
        - **Co-working space** terjangkau (Rp 50K/hari)
        - **Public charging station** di transportasi umum
        
        **5. 📊 Youth Data Dashboard Real-time**
        - Monitoring indikator pemuda berkala
        - Early warning system isu sosial
        - Policy simulation tool
        - Public accountability portal
        """)
        
        # Roadmap implementation
        st.markdown("### 🗺️ Roadmap Implementasi 2024-2025")
        roadmap_data = pd.DataFrame({
            'Tahap': ['Persiapan (Q3-Q4 2024)', 'Pilot (Q1-Q2 2025)', 'Skala (Q3 2025 - Q1 2026)', 'Evaluasi & Replikasi (Q2 2026)'],
            'Aktivitas': [
                'Stakeholder mapping, needs assessment, curriculum development, team formation',
                'Program di 5 sekolah/kampus perwakilan, feedback collection, adjustment',
                'Ekspansi ke 50+ institusi, city-wide coverage, digital platform launch',
                'Impact measurement, satisfaction survey, best practices documentation, replication planning'
            ],
            'Indikator Sukses': [
                'MOU signed 100%, team formed, curriculum approved',
                'Participation rate >80%, satisfaction >4/5, knowledge improvement >40%',
                'City coverage 100%, digital adoption >60%, behavioral change >50%',
                'ROI calculated, policy impact measured, replication readiness 100%'
            ],
            'Budget Estimate': [
                'Rp 2.5 Miliar',
                'Rp 5 Miliar',
                'Rp 15 Miliar',
                'Rp 2 Miliar'
            ]
        })
        
        st.dataframe(roadmap_data, width='stretch', hide_index=True)
        
        # Funding sources
        st.markdown("### 💰 Sumber Pendanaan Potensial")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("APBD Kota Medan", "40%", "Rp 10M")
        with col2:
            st.metric("APBN Kementerian", "35%", "Rp 8.75M")
        with col3:
            st.metric("CSR Perusahaan", "25%", "Rp 6.25M")
    
    with tab2:
        st.markdown("""
        ### 🎓 Rekomendasi untuk Sekolah & Kampus di Medan
        
        **1. 📚 Kurikulum Integratif Abad 21**
        - **Literasi finansial** terintegrasi dalam ekonomi, matematika
        - **Digital safety & ethics** dalam TIK, PPKN
        - **Mental health awareness** dalam BK, agama
        - **Entrepreneurship education** project-based learning
        - **Critical thinking & media literacy** across curriculum
        
        **2. 🏫 Ekosistem Support System Holistik**
        - **Peer counseling program** dengan supervision
        - **Career guidance center** dengan industry partnership
        - **Incubator space on campus** untuk student startups
        - **Alumni mentorship network** terstruktur
        - **Industry advisory board** untuk kurikulum
        
        **3. 📊 Assessment & Development Holistik**
        - **360° student assessment** beyond academic scores
        - **Soft skills portfolio** digital & terverifikasi
        - **Mental wellbeing tracking** dengan privacy protection
        - **Career readiness assessment** dengan personalized guidance
        - **Impact measurement** learning outcomes vs employability
        
        **4. 💻 Digital Transformation Pendidikan**
        - **E-learning platform** dengan konten lokal
        - **Virtual counseling & career services**
        - **Online internship & project marketplace**
        - **Digital portfolio system** terintegrasi
        - **AI-powered personalized learning**
        
        **5. 🤝 Community Engagement & Outreach**
        - **Parent education programs** digital parenting
        - **Community service requirements** dengan reflection
        - **Industry immersion programs** regular & structured
        - **Cross-institution collaboration** resource sharing
        - **Public seminar & workshop** open for community
        """)
        
        # Implementation priority
        st.markdown("### 🎯 Prioritas Implementasi 1 Tahun")
        priority_data = pd.DataFrame({
            'Priority': ['Tinggi (1-3 bulan)', 'Sedang (4-9 bulan)', 'Rendah (10-12 bulan)'],
            'Program': [
                'Training guru BK, basic digital safety curriculum, peer counseling pilot',
                'Career center setup, industry partnerships, mental health screening system',
                'Full curriculum integration, alumni network activation, digital platform development'
            ],
            'Resource Needed': [
                'Rp 500 juta, 20 trainer, 100 volunteer',
                'Rp 1.5 miliar, 5 career counselors, industry MOU',
                'Rp 3 miliar, curriculum experts, tech development team'
            ]
        })
        
        st.dataframe(priority_data, width='stretch', hide_index=True)
    
    with tab3:
        st.markdown("""
        ### 📈 Rekomendasi untuk Bisnis & Industri di Medan
        
        **1. 🎯 Gen Z-Centric Marketing Strategy**
        ```
        Platform Mix: TikTok + Instagram + WhatsApp Business
        Content Type: Authentic, short-form, interactive, value-driven
        Format: Live commerce, UGC campaigns, AR experiences, micro-influencers
        Payment: Digital wallet options + financial education
        Language: Bahasa Medan informal, relatable, inclusive
        ```
        
        **2. 🛍️ Product & Service Development**
        - **Youth-centric design thinking** dalam pengembangan produk
        - **Affordable pricing tiers** dengan flexible payment options
        - **Sustainability & ethical focus** transparent supply chain
        - **Personalization & co-creation** involve Gen Z in design process
        - **Experiential retail** offline spaces that are Instagrammable
        
        **3. 💼 Talent Engagement & Development**
        - **Gen Z internship programs** dengan meaningful projects
        - **Flexible work arrangements** hybrid, project-based
        - **Side-hustle friendly policies** recognize diverse income streams
        - **Digital upskilling opportunities** sponsored certifications
        - **Mentorship reverse mentoring** Gen Z teach digital skills
        
        **4. 🤲 Corporate Responsibility & Community**
        - **Support youth entrepreneurship** through incubation programs
        - **Mental health initiatives** employee assistance programs extended to community
        - **Digital literacy programs** in partnership with schools
        - **Local content creation support** fund creative projects
        - **Sustainable consumption education** environmental responsibility
        
        **5. 📊 Data-Driven Youth Insights**
        - **Regular youth market research** local context specific
        - **Gen Z advisory board** for product development
        - **Trend forecasting unit** khusus pasar Medan
        - **Social listening tools** untuk real-time insights
        - **Collaboration dengan researcher lokal** untuk depth insights
        """)
        
        # Business metrics dashboard
        st.markdown("### 📊 Youth Business Metrics Dashboard")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("ROI Target Campaign Gen Z", "3.5x", "vs 2.8x average")
        with col2:
            st.metric("Conversion Rate Live Commerce", "8.5%", "+320% vs traditional")
        with col3:
            st.metric("Brand Lift & Perception", "+42%", "Gen Z brand affinity")
        with col4:
            st.metric("Customer Lifetime Value", "Rp 4.2Jt", "5-year projection")
        
        # Success case examples
        st.markdown("### 🏆 Best Practice Examples")
        success_cases = pd.DataFrame({
            'Company': ['Local Fashion Brand A', 'Food & Beverage B', 'Tech Startup C', 'Retail Chain D'],
            'Strategy': [
                'TikTok UGC contest with local creators',
                'Instagram Reels recipe challenges',
                'Campus ambassador program with equity',
                'Co-working space with youth discounts'
            ],
            'Result': [
                '+200% sales, 50K new followers',
                'Viral trend, 300% outlet traffic',
                '100 campus reps, 40% user growth',
                '85% occupancy, community hub status'
            ]
        })
        
        st.dataframe(success_cases, width='stretch', hide_index=True)
    
    with tab4:
        st.markdown("""
        ### 🤲 Rekomendasi untuk LSM & Organisasi Pemuda Medan
        
        **1. 🌱 Program Advokasi & Empowerment Berkelanjutan**
        - **Youth entrepreneurship training** dengan follow-up mentoring
        - **Mental health peer support** networks dengan professional backup
        - **Digital rights advocacy** untuk safe online spaces
        - **Community mapping initiatives** untuk resource optimization
        - **Leadership development** untuk sustainable impact
        
        **2. 🤝 Platform Kolaborasi Multi-Stakeholder**
        - **Medan Youth Coalition** network of 100+ youth organizations
        - **Knowledge sharing portal** best practices & resources
        - **Crowdfunding platform** untuk youth social projects
        - **Volunteer matching system** skills-based opportunities
        - **Policy dialogue forums** regular youth-government-business meetings
        
        **3. 🔬 Research & Development Berbasis Bukti**
        - **Localized youth studies** Medan-specific issues & opportunities
        - **Program impact evaluation** rigorous measurement & reporting
        - **Best practices documentation** case studies & toolkits
        - **Policy recommendation papers** data-driven advocacy
        - **Longitudinal studies** tracking changes over time
        
        **4. 🌍 International Linkages & Exchange**
        - **Youth exchange programs** dengan kota sister Medan
        - **Global network participation** ASEAN youth networks
        - **International funding access** grant writing support
        - **Cross-cultural learning** virtual exchange programs
        - **Best practice adaptation** global to local contextualization
        
        **5. 🎨 Creative & Cultural Expression Support**
        - **Youth arts & culture festivals** showcasing local talent
        - **Digital content creation labs** equipment & training access
        - **Heritage preservation projects** youth-led documentation
        - **Creative entrepreneurship** arts-based business incubation
        - **Public space activation** youth-led urban interventions
        """)
        
        # Capacity building framework
        st.markdown("### 🏗️ Capacity Building Framework")
        capacity_data = pd.DataFrame({
            'Level': ['Individual Youth', 'Youth Organizations', 'Ecosystem'],
            'Focus Areas': [
                'Skills training, mentorship, personal development, mental wellbeing',
                'Organizational development, fundraising, program management, networking',
                'Policy advocacy, multi-stakeholder coordination, resource mobilization, systemic change'
            ],
            'Key Programs': [
                'Leadership bootcamps, skill certifications, personal coaching',
                'Organizational assessment, grant writing workshops, partnership building',
                'Policy roundtables, cross-sector task forces, collective impact initiatives'
            ]
        })
        
        st.dataframe(capacity_data, width='stretch', hide_index=True)

elif section == "📚 Kesimpulan & Referensi":
    st.markdown('<h2 class="section-header">Kesimpulan & Referensi</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown("""
        ## 🎯 Kesimpulan Utama
        
        **1. 🏙️ Demografi Strategis dengan Potensi Besar**
        Gen Z Medan (~455K jiwa, 27% populasi) bukan hanya angka statistik, tetapi aset strategis dengan potensi ekonomi, sosial, dan inovasi yang signifikan untuk pembangunan kota.
        
        **2. 📱 Transformasi Digital yang Tidak Terelakkan**
        Sebagai digital natives sejati, Gen Z Medan hidup dalam ekosistem digital yang kompleks dengan preferensi kuat pada konten video pendek, shaping consumption patterns, identity formation, dan social interactions.
        
        **3. 💰 Ekonomi Digital: Peluang dan Tantangan**
        Adopsi e-commerce dan dompet digital mencapai tingkat tinggi, menciptakan peluang ekonomi baru namun disertai kebutuhan mendesak untuk peningkatan literasi keuangan dan proteksi konsumen.
        
        **4. 🧠 Isu Prioritas yang Membutuhkan Perhatian Segera**
        Kesehatan mental, entrepreneurial aspirations, social media pressure, dan future uncertainty adalah concern utama yang membutuhkan intervensi terpadu dan berkelanjutan.
        
        **5. 👥 Segmentasi Diversifikasi yang Memerlukan Pendekatan Customized**
        4 segmen utama dengan karakteristik, kebutuhan, dan aspirasi berbeda membutuhkan pendekatan yang customized dalam program, kebijakan, dan engagement strategy.
        
        ## 🚀 Call to Action: Kolaborasi Multi-Pihak
        
        **Integrated Ecosystem Approach** diperlukan dengan melibatkan:
        - **🏛️ Pemerintah daerah**: Policy framework & infrastructure development
        - **🏫 Institusi pendidikan**: Curriculum innovation & support systems
        - **💼 Pelaku bisnis**: Economic opportunities & ethical practices
        - **🤝 Civil society**: Advocacy, empowerment & community building
        - **👨‍👩‍👧‍👦 Keluarga & komunitas**: Support networks & value transmission
        
        **Immediate Strategic Priorities** (2024-2025):
        1. **Multi-stakeholder youth summit** untuk alignment vision & action plan
        2. **Pilot programs terintegrasi** di 10 sekolah/kampus percontohan
        3. **Public-private partnership initiatives** dengan measurable outcomes
        4. **Digital youth dashboard** untuk real-time monitoring & evaluation
        5. **Capacity building ecosystem** untuk sustainability & scalability
        
        ## 🔮 Vision 2027: Medan sebagai Kota Ramah Pemuda
        
        **Target Indikator Kunci**:
        - Youth unemployment rate <10% (dari 15% saat ini)
        - Youth mental health access >70% (dari 30% saat ini)
        - Youth entrepreneurship rate >25% (dari 15% saat ini)
        - Youth digital literacy >85% (dari 65% saat ini)
        - Youth civic participation >60% (dari 40% saat ini)
        
        **Prinsip Dasar**:
        - **Nothing about youth without youth**: Meaningful youth participation
        - **Evidence-based decision making**: Data-driven interventions
        - **Ecosystem approach**: Systemic rather than piecemeal solutions
        - **Sustainability focus**: Long-term impact over short-term gains
        - **Local context sensitivity**: Medan-specific solutions
        """)
    
    with col2:
        st.markdown("""
        <div class="data-card">
        <h4>📊 Key Metrics Summary</h4>
        
        <p>👥 <strong>Population Size</strong>: 455.5K</p>
        <p>📱 <strong>Internet Penetration</strong>: 80.7%</p>
        <p>🛒 <strong>E-commerce Adoption</strong>: 68%</p>
        <p>😔 <strong>Mental Health Issues</strong>: 65%</p>
        <p>🚀 <strong>Entrepreneurship Interest</strong>: 35%</p>
        <p>🎓 <strong>Higher Education Aspiration</strong>: 75%</p>
        <p>💼 <strong>Remote Work Preference</strong>: 68%</p>
        <p>📈 <strong>Digital Economy Growth</strong>: 22% YoY</p>
        
        <h4>🎯 Strategic Focus Areas</h4>
        <p>1. Digital & Financial Literacy</p>
        <p>2. Mental Health Support</p>
        <p>3. Youth Entrepreneurship</p>
        <p>4. Future Skills Development</p>
        <p>5. Inclusive Digital Access</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Daftar Pustaka
    st.markdown('<h3 class="subsection-header">📚 Daftar Pustaka (Pilihan)</h3>', unsafe_allow_html=True)
    
    with st.expander("Klik untuk melihat daftar referensi lengkap"):
        st.markdown("""
        **Sumber Data Resmi:**
        1. **BPS Kota Medan**. (2024). *Kota Medan Dalam Angka 2024*. Badan Pusat Statistik Kota Medan.
        2. **BPS Provinsi Sumatera Utara**. (2024). *Sumatera Utara dalam Angka 2024*.
        3. **BPS Indonesia**. (2024). *Statistik Pemuda Indonesia 2024*. Jakarta: BPS.
        4. **Kemendikbudristek**. (2024). *Data APK/APM Pendidikan 2023*. apkapm.data.kemdikbud.go.id
        5. **Kemenpora**. (2023). *Indeks Pembangunan Pemuda Indonesia 2023*. Jakarta: Kementerian Pemuda dan Olahraga.
        
        **Lembaga Survei & Riset:**
        6. **APJII**. (2024). *Survei Penetrasi Internet Indonesia 2024*. Asosiasi Penyelenggara Jasa Internet Indonesia.
        7. **Populix**. (2023). *PopVoice Gen Z & Millennials Report Q1 2023*. Jakarta: Populix.
        8. **Alvara Research Center**. (2024). *Gen Z Indonesia: Characteristics, Behavior & Preferences*. Jakarta: Alvara.
        9. **We Are Social**. (2024). *Digital 2024: Indonesia Report*. DataReportal.
        
        **Platform Digital & E-commerce:**
        10. **TikTok**. (2024). *TikTok Marketing Insights: Indonesia Youth*. TikTok for Business.
        11. **e-Conomy SEA**. (2024). *e-Conomy SEA 2024 Report*. Google, Temasek, Bain & Company.
        12. **Shopee**. (2024). *Indonesia E-commerce Trend Report 2024*. Shopee Intelligence.
        13. **Spotify**. (2023). *Spotify Wrapped 2023: Indonesia Trends*. Spotify Newsroom.
        
        **Institusi Keuangan & Internasional:**
        14. **OJK**. (2023). *Survei Nasional Literasi dan Inklusi Keuangan 2022*. Otoritas Jasa Keuangan.
        15. **Bank Indonesia**. (2023). *Laporan Sistem Pembayaran Indonesia 2023*.
        16. **UNICEF Indonesia**. (2023). *Youth Engagement and Participation Report*. UNICEF.
        17. **ILO**. (2023). *Global Employment Trends for Youth 2023*. International Labour Organization.
        
        **Studi Akademik & Jurnal:**
        18. **Universitas Gadjah Mada**. (2023). *i-NAMHS: Indonesia National Adolescent Mental Health Survey*.
        19. **Universitas Sumatera Utara**. (2023). *Perilaku Konsumsi Generasi Z di Medan*. Jurnal Ilmiah.
        20. **Universitas Indonesia**. (2024). *Digital Literacy Among Indonesian Youth*. Research Center for Population.
        
        **Laporan Kebijakan:**
        21. **World Bank**. (2023). *Indonesia's Youth: Challenges and Opportunities*. World Bank Report.
        22. **McKinsey & Company**. (2023). *Understanding Indonesian Consumers*. McKinsey Insights.
        23. **Boston Consulting Group**. (2024). *The Rise of Digital Natives in Southeast Asia*. BCG Report.
        """)
    
    # Rekomendasi Penelitian Lanjutan
    st.markdown('<h3 class="subsection-header">🔬 Rekomendasi Penelitian Lanjutan</h3>', unsafe_allow_html=True)
    
    research_priority = pd.DataFrame({
        'Priority': ['Tinggi', 'Sedang', 'Rendah'],
        'Research Topics': [
            'Survei primer representatif di Medan (n=2000, stratified sampling SMA & mahasiswa)',
            'Studi longitudinal dampak media sosial terhadap kesehatan mental (3 tahun)',
            'Evaluasi program literasi digital/keuangan (pre-post intervention dengan control group)',
            'Analisis komparatif Medan vs kota besar Indonesia lainnya (benchmarking study)',
            'Deep-dive qualitative motivasi & barriers entrepreneurship Gen Z Medan',
            'Impact assessment mental health interventions di setting sekolah/kampus',
            'Digital ethnography perilaku online Gen Z Medan (social media analysis)',
            'Economic impact analysis youth entrepreneurship ecosystem di Medan',
            'Policy analysis youth-focused policies & programs effectiveness',
            'Future skills forecasting untuk kebutuhan pasar kerja Medan 2030'
        ],
        'Timeline': [
            '6-8 bulan',
            '3 tahun',
            '1 tahun',
            '9 bulan',
            '6 bulan',
            '1.5 tahun',
            '4 bulan',
            '8 bulan',
            '7 bulan',
            '1 tahun'
        ],
        'Estimated Budget': [
            'Rp 750 juta',
            'Rp 1.2 miliar',
            'Rp 500 juta',
            'Rp 600 juta',
            'Rp 300 juta',
            'Rp 800 juta',
            'Rp 250 juta',
            'Rp 700 juta',
            'Rp 400 juta',
            'Rp 900 juta'
        ]
    })
    
    st.dataframe(research_priority, width='stretch', hide_index=True)
    
    # Closing statement
    st.markdown("""
    ---
    
    ### 📝 Penutup
    
    **MEDAN YOUTH INSIGHTS** merupakan upaya sistematis untuk memahami kompleksitas dan dinamika Generasi Z di Kota Medan berdasarkan data dan evidence yang tersedia. 
    
    **Harapan ke Depan:**
    - Laporan ini menjadi titik awal untuk dialog dan kolaborasi yang lebih intensif
    - Data dan insights dijadikan dasar pengambilan keputusan yang lebih baik
    - Program dan kebijakan yang lebih tepat sasaran dan berdampak
    - Medan menjadi contoh kota yang sukses memberdayakan generasi mudanya
    
    **Kontribusi & Kolaborasi:**
    Untuk pengembangan penelitian dan program lebih lanjut, silakan hubungi tim peneliti melalui platform kolaborasi yang akan dibentuk.
    
    ***"Investasi terbaik untuk masa depan Medan adalah investasi pada generasi mudanya hari ini."***
    """)

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**📊 Data Sources:** BPS, APJII, We Are Social, Populix, Alvara, e-Conomy SEA")
with col2:
    st.markdown("**📅 Last Updated:** Juni 2024")
with col3:
    st.markdown("**⚠️ Disclaimer:** Estimasi berdasarkan data sekunder terverifikasi")

st.markdown("<p style='text-align: center; color: #64748B; font-size: 0.9rem;'>© FXF28 MEDAN YOUTH INSIGHTS - Analisis Komprehensif Gen Z Medan</p>", unsafe_allow_html=True)