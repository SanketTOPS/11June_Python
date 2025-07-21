from pytubefix import YouTube

url="https://www.youtube.com/watch?v=1JKuv-OWpM8&list=RD1JKuv-OWpM8&start_radio=1"

YouTube(url).streams.first().download()