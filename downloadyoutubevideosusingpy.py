import webbrowser

#enter the url of video which you want to download
# url="----------------"
#you can use any youtube url here
url="https://www.youtube.com/watch?v=cjzYKwOLKoY"

#as we add ss in front of youtube to download the videos of youtube from Savefrom.net

#https://www.youtube.com/
#https://www.ssyoutube.com/
#so the position at which we add ss is [:12]after and [12:]before that
#here download is a variable,you can use any variable name
download=url[:12]+"ss"+url[12:]

webbrowser.open(download)
