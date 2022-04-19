data_riwayat = [["game_id", "nama", "harga", "user_id", "tahun_beli"],
                ["GAME001", "Journey", "120000", "3", "2020"],
                ["GAME001", "Journey", "120000", "6", "2021"],
                ["GAME002", "Hitman 3", "370000", "4", "2021"],
                ["GAME004", "Forza Horizon 5", "550000", "3", "2022"],
                ["GAME005", "Sekiro", "250000", "5", "2022"]]


def length(data_riwayat):
    count = 0
    for i in data_riwayat:
        count += 1
    return count

def riwayat_user(user_id, data_riwayat):
    list = []
    for item in data_riwayat:
        if item[3] == user_id:
            list += item[3]
    return list


def riwayat(data_riwayat):
    user_id = input("id: ")

    if length(data_riwayat) == 0:
        print("Maaf, kamu tidak ada riwayat pembelian game. ketik perintah beli_game untuk membeli")
    else:
        riwayat_user(user_id, data_riwayat)
        for i in range(length(data_riwayat[3])):
            for j in range(length(data_riwayat[3])):
                if user_id == data_riwayat[i][3]:
                    print(data_riwayat[i][j], end=' ')
    return

print(riwayat(data_riwayat))
