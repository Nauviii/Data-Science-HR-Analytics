import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

st.set_page_config(layout="wide")


#  Utilities 
def ensure_cluster_column(df: pd.DataFrame) -> pd.DataFrame:
    df2 = df.copy()
    if "Cluster" in df2.columns:
        df2 = df2.reset_index(drop=True)
        return df2

    idx_name = df2.index.name if df2.index.name is not None else "index"
    df2 = df2.reset_index()
    df2 = df2.rename(columns={idx_name: "Cluster"})
    return df2


#  Data Loader 
@st.cache_data
def load_summary(path: str) -> pd.DataFrame:
    df = joblib.load(path)
    return ensure_cluster_column(df)


#  Plot Functions 
def plot_cluster_proportion(df: pd.DataFrame) -> None:
    fig = px.pie(
        df,
        names="Cluster",
        values="Cluster Size",
        title="Distribusi Ukuran Cluster"
    )
    st.plotly_chart(fig, use_container_width=True)


def plot_attrition_proportion(df: pd.DataFrame) -> None:
    fig = px.bar(
        df,
        x="Cluster",
        y="Attrition Proportion",
        title="Attrition Proportion per Cluster",
        text="Attrition Proportion"
    )
    fig.update_traces(texttemplate='%{text:.2%}', textposition='outside')
    st.plotly_chart(fig, use_container_width=True)


#  Display Functions 
def show_summary(df: pd.DataFrame) -> None:
    st.subheader("📊 Ringkasan Cluster")
    st.dataframe(df)

    col1, col2 = st.columns(2)
    with col1:
        plot_cluster_proportion(df)
    with col2:
        plot_attrition_proportion(df)


def show_detail(df: pd.DataFrame) -> None:
    st.subheader("🔍 Analisis Detail per Cluster")

    cluster_options = df["Cluster"].tolist()
    selected_cluster = st.selectbox("Pilih Cluster", cluster_options)

    cluster_row = df.loc[df["Cluster"] == selected_cluster].squeeze()

    # --- Karakteristik Cluster (Improved) ---
    st.write("### Karakteristik Cluster")

    # Tampilkan tabel ringkas
    char_df = pd.DataFrame(cluster_row).reset_index()
    char_df.columns = ["Atribut", "Nilai"]
    st.dataframe(char_df, use_container_width=True)

    # Pisahkan numerik & kategorik dari Series
    exclude_cols = ["Cluster"]
    char_data = cluster_row.drop(labels=exclude_cols, errors="ignore")

    num_data = char_data[char_data.apply(lambda x: pd.api.types.is_numeric_dtype(type(x)))]
    cat_data = char_data[~char_data.apply(lambda x: pd.api.types.is_numeric_dtype(type(x)))]


    # Kalau ada kategorik, tampilkan tabel kecil
    if not cat_data.empty:
        st.write("#### Atribut Kategorikal")
        st.table(cat_data.reset_index().rename(columns={"index": "Atribut", 0: "Nilai"}))



def show_insight(df: pd.DataFrame) -> None:
    st.subheader("💡 Insight & Rekomendasi")
    high_attrition_cluster = df.loc[df["Attrition Proportion"].idxmax()]
    low_attrition_cluster = df.loc[df["Attrition Proportion"].idxmin()]

    st.markdown(f"""
- **Cluster dengan attrition tertinggi**: Cluster **{int(high_attrition_cluster['Cluster'])}** 
  (Proporsi Attrition = **{high_attrition_cluster['Attrition Proportion']:.2%}**)
- **Cluster dengan attrition terendah**: Cluster **{int(low_attrition_cluster['Cluster'])}** 
  (Proporsi Attrition = **{low_attrition_cluster['Attrition Proportion']:.2%}**)
""")

    st.write("### Rekomendasi Strategi Retensi")
    st.markdown("""
- Untuk cluster dengan attrition tinggi:
  - Tingkatkan program career development & mentoring.
  - Review sistem kompensasi & benefit (terutama bagi level junior).
  - Pertimbangkan fleksibilitas kerja dan beban kerja.

- Untuk cluster dengan attrition rendah:
  - Pertahankan kepuasan kerja melalui penghargaan & insentif.
  - Pastikan jalur karier tetap jelas agar loyalitas terjaga.
""")


#  Main App 
def main() -> None:
    st.title("📈 Dashboard Analisis Clustering - Attrition")

    df_summary = load_summary("data_summary.joblib")  

    tab1, tab2, tab3 = st.tabs(["Ringkasan", "Detail Cluster", "Insight"])

    with tab1:
        show_summary(df_summary)

    with tab2:
        show_detail(df_summary)

    with tab3:
        show_insight(df_summary)


if __name__ == "__main__":
    main()
