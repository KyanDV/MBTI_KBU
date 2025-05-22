import streamlit as st
import numpy as np

# Daftar pertanyaan MBTI (40 pertanyaan)
questions = [
    # Extraversion (E) vs Introversion (I) - 10 pertanyaan
    "1. Saya merasa berenergi setelah menghabiskan waktu dengan banyak orang.",
    "2. Saya lebih suka berbicara daripada mendengarkan dalam percakapan.",
    "3. Saya senang menjadi pusat perhatian dalam kelompok.",
    "4. Saya mudah bosan jika sendirian terlalu lama.",
    "5. Saya lebih memilih kerja kelompok daripada bekerja sendiri.",
    "6. Saya sering mengungkapkan pikiran saya secara spontan.",
    "7. Saya memiliki banyak teman dan kenalan.",
    "8. Saya merasa lebih nyaman di acara sosial daripada di rumah sendirian.",
    "9. Saya senang memulai percakapan dengan orang asing.",
    "10. Saya cenderung berpikir keras setelah berbicaran.",

    # Sensing (S) vs Intuition (N) - 10 pertanyaan
    "11. Saya lebih fokus pada fakta daripada teori abstrak.",
    "12. Saya lebih suka petunjuk langkah demi langkah daripada ide besar.",
    "13. Saya percaya pengalaman lebih penting daripada imajinasi.",
    "14. Saya lebih tertarik pada 'apa yang ada' daripada 'apa yang mungkin'.",
    "15. Saya lebih suka hal-hal praktis daripada konsep filosofis.",
    "16. Saya memperhatikan detail kecil dalam lingkungan sekitar.",
    "17. Saya lebih mengandalkan bukti nyata daripada firasat.",
    "18. Saya lebih nyaman dengan rutinitas yang jelas.",
    "19. Saya lebih suka sejarah daripada sains fiksi.",
    "20. Saya lebih memilih solusi yang sudah terbukti daripada ide baru.",

    # Thinking (T) vs Feeling (F) - 10 pertanyaan
    "21. Saya lebih memilih logika daripada perasaan saat mengambil keputusan.",
    "22. Saya lebih peduli kebenaran daripada harmoni dalam diskusi.",
    "23. Kritik objektif lebih penting bagi saya daripada dukungan emosional.",
    "24. Saya cenderung analitis daripada empatik.",
    "25. Saya lebih mudah memisahkan emosi dari fakta.",
    "26. Saya lebih menghargai keadilan daripada belas kasihan.",
    "27. Saya lebih suka debat intelektual daripada percakapan emosional.",
    "28. Saya lebih sering menggunakan 'kepala' daripada 'hati'.",
    "29. Saya lebih fokus pada hasil daripada perasaan orang lain.",
    "30. Saya percaya bahwa kebenaran harus diutamakan meski menyakiti perasaan.",

    # Judging (J) vs Perceiving (P) - 10 pertanyaan
    "31. Saya suka membuat rencana terlebih dahulu sebelum bertindak.",
    "32. Saya lebih nyaman dengan jadwal yang terstruktur.",
    "33. Saya tidak suka menunda-nunda pekerjaan.",
    "34. Saya lebih memilih kepastian daripada fleksibilitas.",
    "35. Saya merasa stres jika tidak memiliki daftar tugas yang jelas.",
    "36. Saya lebih suka menyelesaikan proyek sebelum bersantai.",
    "37. Saya cenderung rapi dan terorganisir.",
    "38. Saya lebih suka keputusan cepat daripada menimbang terlalu lama.",
    "39. Saya merasa tidak nyaman dengan perubahan mendadak.",
    "40. Saya lebih suka aturan yang jelas daripada kebebasan mutlak."
]

# Database tipe MBTI + Deskripsi + Pekerjaan yang Cocok
mbti_data = {
    "ISTJ": {
        "deskripsi": "Inspektur - Teliti, terorganisir, dan suka bekerja dengan data serta sistem yang membutuhkan akurasi tinggi.",
        "pekerjaan": ["Auditor IT", "Analis Data", "Teknisi IT", "Insinyur IT"]
    },
    "ISFJ": {
        "deskripsi": "Pemelihara - Perhatian dan teliti, cocok di posisi yang membutuhkan dukungan teknis dan pemeliharaan sistem.",
        "pekerjaan": ["IT Support", "Administrator Sistem", "Pengelola Database"]
    },
    "INFJ": {
        "deskripsi": "Konselor - Unggul dalam memahami kebutuhan pengguna dan merancang solusi IT yang human-centered.",
        "pekerjaan": ["Konsultan IT", "Analis Bisnis", "Pengembang Produk"]
    },
    "INTJ": {
        "deskripsi": "Perencana - Strategis, visioner, dan analitis, cocok untuk peran yang memerlukan perencanaan dan pengembangan sistem kompleks.",
        "pekerjaan": ["System Analyst", "Project Manager", "Programmer", "Business Analyst"]
    },
    "INTP": {
        "deskripsi": "Pemikir - Kreatif, logis, dan inovatif, sangat cocok untuk pekerjaan teknis dan analitis yang menuntut pemecahan masalah dan inovasi.",
        "pekerjaan": [
            "Programmer", "Security Engineer", "Arsitek IT", "Business Analyst",
            "Web Developer", "Data Scientist", "Machine Learning Engineer",
            "Cyber Security Specialist", "Blockchain Developer", "DevOps Engineer"
        ]
    },
    "ESTJ": {
        "deskripsi": "Eksekutor - Terorganisir dan tegas, cocok memimpin proyek dan mengelola operasi IT.",
        "pekerjaan": ["Manajer Proyek IT", "Administrator Jaringan", "Analis Sistem"]
    },
    "ESFJ": {
        "deskripsi": "Pemberi - Komunikatif dan peduli, cocok untuk posisi yang memerlukan interaksi dengan pengguna dan pelatihan.",
        "pekerjaan": ["IT Support", "Trainer IT", "Manajer Layanan Pelanggan IT"]
    },
    "ENFJ": {
        "deskripsi": "Guru - Visioner dan mampu memotivasi tim, cocok di posisi manajerial dan pengembangan produk IT.",
        "pekerjaan": ["Manajer Proyek", "Konsultan IT", "Pengembang Produk"]
    },
    "ENFP": {
        "deskripsi": "Penginspirasi - Kreatif dan komunikatif, cocok di bidang pengembangan produk dan pemasaran digital.",
        "pekerjaan": ["Product Manager", "Konsultan IT", "Digital Marketer"]
    },
    "ISTP": {
        "deskripsi": "Pengrajin - Praktis dan suka tantangan teknis, cocok untuk pekerjaan hands-on di bidang IT.",
        "pekerjaan": ["Programmer", "Network Engineer", "Security Analyst"]
    },
    "ISFP": {
        "deskripsi": "Seniman - Kreatif dan peka, cocok untuk desain antarmuka dan multimedia.",
        "pekerjaan": ["UI/UX Designer", "Multimedia Specialist"]
    },
    "INFP": {
        "deskripsi": "Idealis - Kreatif dan idealis, cocok untuk pengembangan konten dan software yang inovatif.",
        "pekerjaan": ["Content Developer", "Software Developer", "Digital Creator"]
    },
    "ESTP": {
        "deskripsi": "Pengusaha - Energik dan praktis, cocok untuk peran yang dinamis dan berorientasi hasil.",
        "pekerjaan": ["Network Administrator", "IT Sales", "Cybersecurity Specialist"]
    },
    "ESFP": {
        "deskripsi": "Penghibur - Sosial dan adaptif, cocok untuk pekerjaan yang melibatkan interaksi dan kreativitas.",
        "pekerjaan": ["IT Support", "Social Media Manager", "Digital Content Creator"]
    },
    "ENTJ": {
        "deskripsi": "Komandan - Tegas, terorganisir, dan visioner, cocok untuk posisi manajerial dan strategis di IT.",
        "pekerjaan": ["Project Manager", "Financial Analyst", "Network Administrator", "Auditor", "Konsultan IT"]
    },
    "ENTP": {
        "deskripsi": "Pendebat - Kreatif dan suka tantangan, cocok untuk pekerjaan yang membutuhkan inovasi dan pemikiran konseptual.",
        "pekerjaan": ["System Analyst", "Data Scientist", "Konsultan IT", "Product Manager"]
    }
}

threshold = 30.5

# Kategori indeks (start, end)
categories = {
    "E/I": (0, 10),
    "S/N": (10, 20),
    "T/F": (20, 30),
    "J/P": (30, 40),
}

if "current_q" not in st.session_state:
    st.session_state.current_q = 0
    st.session_state.answers = []
    st.session_state.category_scores = {"E/I": 0, "S/N": 0, "T/F": 0, "J/P": 0}

st.title("Tes Kepribadian MBTI")
st.write("Berikan skor 1-5:")
st.write("1 = Sangat Tidak Setuju, 5 = Sangat Setuju")

def get_category_for_question(idx):
    for cat, (start, end) in categories.items():
        if start <= idx < end:
            return cat
    return None

# Fungsi lompat ke pertanyaan pertama kategori berikutnya
def jump_to_next_category(current_idx):
    for cat, (start, end) in categories.items():
        if current_idx < end:
            # jika current_idx masih di bawah end kategori ini, lompat ke awal kategori berikutnya
            if current_idx < start:
                return start
            else:
                # lompat ke kategori berikutnya jika ada
                cat_keys = list(categories.keys())
                current_cat_idx = cat_keys.index(get_category_for_question(current_idx))
                if current_cat_idx + 1 < len(cat_keys):
                    next_cat = cat_keys[current_cat_idx + 1]
                    return categories[next_cat][0]
                else:
                    return 40  # sudah akhir pertanyaan
    return 40

def advance_question(skor):
    idx = st.session_state.current_q
    cat = get_category_for_question(idx)
    st.session_state.answers.append(skor)
    st.session_state.category_scores[cat] += skor

    # Cek threshold kategori saat ini
    if st.session_state.category_scores[cat] >= threshold:
        # Lompat ke kategori berikutnya
        next_q = jump_to_next_category(idx)
        st.session_state.current_q = next_q
    else:
        st.session_state.current_q += 1

st.write(f"**Pertanyaan {st.session_state.current_q + 1} dari {len(questions)}**")

if st.session_state.current_q < len(questions):
    skor = st.slider(questions[st.session_state.current_q], 1, 5, 3, key=f"slider_{st.session_state.current_q}")

    if st.button("Pertanyaan Berikutnya"):
        advance_question(skor)
        st.stop() 

else:
    e_score = st.session_state.category_scores["E/I"]
    s_score = st.session_state.category_scores["S/N"]
    t_score = st.session_state.category_scores["T/F"]
    j_score = st.session_state.category_scores["J/P"]

    ei = "E" if e_score > threshold else "I"
    sn = "S" if s_score > threshold else "N"
    tf = "T" if t_score > threshold else "F"
    jp = "J" if j_score > threshold else "P"

    mbti_type = ei + sn + tf + jp

    st.subheader("Hasil Tes MBTI")
    st.write(f"**Tipe Kepribadian Anda: {mbti_type}**")
    st.write(f"**Deskripsi:** {mbti_data[mbti_type]['deskripsi']}")
    st.write("**Pekerjaan yang Cocok:**")
    for i, job in enumerate(mbti_data[mbti_type]['pekerjaan'], 1):
        st.write(f"{i}. {job}")

    if st.button("Ulangi Tes"):
        st.session_state.current_q = 0
        st.session_state.answers = []
        st.session_state.category_scores = {"E/I": 0, "S/N": 0, "T/F": 0, "J/P": 0}
        st.experimental_rerun()
