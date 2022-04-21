data_game = [['id', 'nama', 'kategori', 'tahun_rilis', 'harga', 'stok'],
             ['GAME001', 'Journey', 'Adventure', 2020, 120000, 3],
             ['GAME002', 'Hitman 3', 'Action', 2021, 370000, 5],
             ['GAME003', 'Skyrim', 'RPG', 2011, 200000, 1],
             ['GAME004', 'Forza Horizon 5', 'Racing', 2021, 550000, 9],
             ['GAME005', 'Sekiro', 'Action', 2019, 250000, 0]]

data_user = [["id", "username", "nama", "password", "role", "saldo"],
             [0, "rafi", "rafi", "rafi", "admin", 0],
             [1, "bat_man", "batman", "kelelawar", "user", 0],
             [2, "baim", "ibrahim", "baimsipsip", "user", 0],
             [3, "ard_studios", "ardhan", "dandan123", "user", 0],
             [4, "super_man", "superman", "kuat", "user", 0]]

data_kepemilikan = [["game_id", "user_id"],
                    ["GAME001", 1],
                    ["GAME001", 2],
                    ["GAME002", 3],
                    ["GAME004", 2],
                    ["GAME005", 5]]


def length(game):
    count = 0
    for _ in data_game:
        count += 1
    return count


def datauser(user_id, data_user):
    count = 0
    for item in data_user:
        if item[0] == user_id:
            return item, count
        count += 1
    return


def datagame(id_game, data_game):
    count = 0
    for item in data_game:
        if item[0] == id_game:
            return item, count
        count = + 1
    return

def sudahada(data_kepemilikan, data_game, data_user):
    for item in data_kepemilikan:
        if item[0] == data_game[0] and item[1] == data_user[0]:
            return item[0], item[1]

def saldo(user_id, data_user):
    saldo = 0
    for i in range(length(data_user)):
        if data_user[i][0] == user_id:
            saldo += data_user[i][5]
    return saldo

def buy_game(data_kepemilikan, data_game, data_user):
    id_game = input("Masukkan ID Game: ")
    user_id = input("ID: ")
    datauser(user_id, data_user)
    datagame(id_game, data_game)

    harga = 0
    for i in range(length(data_game)):
        if id_game == data_game[i][0]:
            harga += int(data_game[i][4])
            if data_game[i][5] == 0:
                print("Stok game tersebut sedang habis!")
        if (sudahada(data_kepemilikan, data_game, data_user)):
            print("Anda sudah memiliki game tersebut!")
        elif saldo(user_id, data_user) < harga:
                print("Saldo anda tidak cukup untuk membeli game tersebut!")
        else:
            saldocek = str(saldo(user_id, data_user) - harga)
            stockcek = str(int(data_game[i][5] - 1))
            print(f"Game {data_game[i][1]} berhasil dibeli!")
    return

