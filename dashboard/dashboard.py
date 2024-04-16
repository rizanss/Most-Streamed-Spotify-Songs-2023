import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Mengambil data dari URL
@st.cache_data
def load_data():
    spotify_df = pd.read_csv('https://raw.githubusercontent.com/rizanss/Most-Streamed-Spotify-Songs-2023/main/data/most_streamed_spotify_songs_analysis.csv', encoding='latin1')
    return spotify_df

spotify_df = load_data()

# Menghilangkan baris pada index ke 574
spotify_df = spotify_df.drop(spotify_df.iloc[[574]].index)

# Konversi kolom 'streams' menjadi tipe data float
spotify_df['streams'] = spotify_df['streams'].astype(float)

# Menambahkan kolom baru 'streams in million'
spotify_df['streams_in_million'] = spotify_df['streams'].apply(lambda x: x / 1000000).round(2)
spotify_df.head()

# Melakukan pemetaan dari nomor bulan ke nama bulan
month_names = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Des'}
# Membuat kolom baru bernama 'Month_Abbreviation'
spotify_df['Month_Abbreviation'] = spotify_df['released_month'].map(month_names)
spotify_df.head()

# Tab "Top 10 Lagu"
def top_10_songs():
    st.subheader('Top 10 Lagu Dengan Streams Terbanyak')
    
    # Kelompokkan data berdasarkan 'track_name' dan hitung jumlah total streaming
    top_tracks = spotify_df.groupby('track_name')['streams_in_million'].sum().reset_index()

    # Urutkan data berdasarkan jumlah total streaming secara menurun
    top_tracks = top_tracks.sort_values(by='streams_in_million', ascending=False)

    # Ambil 10 lagu teratas
    top_10_tracks = top_tracks.head(10)

    # Visualisasikan dalam bentuk grafik batang
    fig, ax = plt.subplots(figsize=(8, 5))  # Perkecil ukuran plot
    sns.barplot(x='streams_in_million', y='track_name', data=top_10_tracks, palette='bright', ax=ax)
    plt.title('Top 10 Lagu Dengan Streams Terbanyak')
    plt.xlabel('Jumlah Streams (dalam juta)')
    plt.ylabel('Judul Lagu')
    st.pyplot(fig)

    # Tampilkan tabel dengan data top 10 lagu
    st.write(top_10_tracks)

# Tab "Top 10 Artis"
def top_10_artists():
    st.subheader('Top 10 Artis Dengan Streams Terbanyak')
    
    # Kelompokkan data berdasarkan 'artist(s)_name' dan hitung jumlah total streaming
    top_artists = spotify_df.groupby('artist(s)_name')['streams_in_million'].sum().reset_index()

    # Urutkan data berdasarkan jumlah total streaming secara menurun
    top_artists = top_artists.sort_values(by='streams_in_million', ascending=False)

    # Ambil 10 artis teratas
    top_10_artists = top_artists.head(10)

    # Visualisasikan dalam bentuk grafik batang
    fig, ax = plt.subplots(figsize=(8, 5))  # Perkecil ukuran plot
    sns.barplot(x='streams_in_million', y='artist(s)_name', data=top_10_artists, palette='bright', ax=ax)
    plt.title('Top 10 Artis Dengan Streams Terbanyak')
    plt.xlabel('Jumlah Streams (dalam juta)')
    plt.ylabel('Nama Artis')
    st.pyplot(fig)

    # Tampilkan tabel dengan data top 10 artis
    st.write(top_10_artists)
    
# Tab "The Effect of Collaboration on The Number of Streams"
def collaboration_effect():
    st.subheader('Pengaruh Kolaborasi terhadap Jumlah Streaming')

    # Pengaruh kolaborasi terhadap jumlah streams
    featuring_songs = spotify_df.filter(items=['artist(s)_name', 'artist_count', 'streams_in_million'], axis=1)

    # Visualisasi Pengaruh Kolaborasi terhadap Jumlah Streaming
    featuring_songs_plt = px.scatter(featuring_songs, x='artist_count', y='streams_in_million', width=1200,
                                     height=700, template='plotly_white', title='The Effect of Collaboration on The Number of Streams',
                                     color='streams_in_million', labels={'artist_count': 'Number of Artist', 'streams_in_million': 'Number of Streams'})

    st.plotly_chart(featuring_songs_plt)

# Tab "Pengaruh Bulan"
def effect_of_month():
    st.subheader('Pengaruh Bulan Terhadap Jumlah Streams')

    # Kelompokkan data berdasarkan 'released_month' dan hitung jumlah total streaming
    streams_by_month = spotify_df.groupby('released_month')['streams_in_million'].sum().reset_index()

    # Urutkan data berdasarkan bulan
    streams_by_month = streams_by_month.sort_values(by='released_month')

    # Visualisasikan perubahan jumlah streaming dari bulan ke bulan
    fig, ax = plt.subplots(figsize=(8, 5))  # Perkecil ukuran plot
    sns.lineplot(x='released_month', y='streams_in_million', data=streams_by_month, marker='o', color='blue')
    plt.title('Pengaruh Bulan Terhadap Jumlah Streams')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Streams (dalam juta)')
    plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.grid(True)
    st.pyplot(fig)

# Tampilkan dashboard dengan tiga tab
def main():
    st.title('Dashboard Analisis Data Spotify')

    # Sidebar dengan opsi tab
    tab = st.sidebar.radio('Navigation', ['Top 10 Lagu', 'Top 10 Artis', 'Pengaruh Kolaborasi', 'Pengaruh Bulan'])

    if tab == 'Top 10 Lagu':
        top_10_songs()
    elif tab == 'Top 10 Artis':
        top_10_artists()
    elif tab == 'Pengaruh Kolaborasi':
        collaboration_effect()
    elif tab == 'Pengaruh Bulan':
        effect_of_month()

if __name__ == '__main__':
    main()