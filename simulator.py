import coin
import random

def main():
    heads, tails = 0, 0

    for i in range(1000):
        new_coin = coin.coin(random.choice(['heads', 'tails']))
        toss_res = new_coin.toss()
        if toss_res == 'heads':
            heads += 1
        else:
            tails += 1
    
    print("Percentage of heads:", heads/10)
    print("Percentage of tails:", tails/10)

if __name__ == "__main__":
    main()
