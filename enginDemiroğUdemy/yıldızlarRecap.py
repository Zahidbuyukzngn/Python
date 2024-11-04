kaçYıldız=int(input("lütfen kaç yıldız olacağını belirtiniz: "))

yıldız=""

#kaçyıldıza +1 ekleyerek kullancının girdiği inputu karşılamış oldu range de sınır dahil olmadığı için
for i in range(1,kaçYıldız+1):
    yıldız+="*"
    print(yıldız)