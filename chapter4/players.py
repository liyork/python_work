if __name__ == '__main__':
    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    print(players[0:3])  # [0,3)
    print(players[:4])
    print(players[-3:])  # 最后三名

    for player in players[:3]:
        print(player.title())

    # 切片是一种复制而不是指向原来list
    new_player = players[0:3]
    new_player[0] = 'aaaa'
    print(players)
    print(new_player)
