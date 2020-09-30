import os

def higscore():
    with open("Highscore.txt", "r") as high:
        text = high.readlines()
        text_int = []
        for line in text:
            text_int.append(int(line))
        print(text)
        print(text_int)
        text_int.sort(reverse=True)
        print(text_int)
        #print(text)
        for line in text_int:
            '''if line > "1000":
                print(line)'''
            if int(line) > 1000:
                print(line)

def main():
    higscore()

if __name__ == "__main__":
    main()