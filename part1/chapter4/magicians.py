if __name__ == '__main__':
    magicians = ['alice', 'david', 'carolina']
    for magician in magicians:  # 末尾冒号告诉python，下一行是循环的第一行
        # 相同缩进
        print(magician)
        print(f"i can't wait to see your next trick, {magician.title()}.\n")
    print("thank you")
