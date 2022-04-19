data_game = [['id', 'nama', 'kategori', 'tahun_rilis', 'harga', 'stok'],
             ['GAME001', 'Journey', 'Adventure', 2020, 120000, 3],
             ['GAME002', 'Hitman 3', 'Action', 2021, 370000, 5],
             ['GAME003', 'Skyrim', 'RPG', 2011, 200000, 1],
             ['GAME004', 'Forza Horizon 5', 'Racing', 2021, 550000, 9],
             ['GAME005', 'Sekiro', 'Action', 2019, 250000, 0]]


def length(game):
    count = 0
    for i in (data_game):
        count += 1
    return count

def isIdValid(id_game):
    isValid = False
    for i in range(1, length(id_game)):
        if data_game[i][0] == id_game:
            isValid = True
    return isValid

def updateData(id_game, nama_game, kategori, tahun_rilis, harga):
    for i in range(length(data_game)):
        if data_game[i][0] == id_game:
            if length(nama_game) > 0:
                data_game[i][1] = nama_game
            if length(kategori) > 0:
                data_game[i][2] = kategori
            if length(tahun_rilis) > 0:
                data_game[i][3] = tahun_rilis
            if length(harga) > 0:
                data_game[i][4] = harga
    return

def ubah_game(game):
    id_game = input("Masukkan ID game: ")
    nama_game = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun_rilis = input("Masukkan tahun rilis: ")
    harga = input("Masukkan harga: ")

    for i in range(0, length(data_game)):
        if isIdValid(id_game) == True:
            updateData(id_game, nama_game, kategori, tahun_rilis, harga)
            for i in range(length(data_game[0])):
                for j in range(length(data_game)):
                    if id_game == data_game[i][0]:
                        print(data_game[i][j], end =' ')
        else:
            print("ID game invalid!")
            id_game = input("Masukkan ID game: ")

    print("Game diupdate!")
    return

print(ubah_game(data_game))