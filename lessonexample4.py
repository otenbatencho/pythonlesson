# クラス「冒険者（プレイヤー）」
class Player():
    def __init__(self,name):
        self.name      = name    # 名前
    # 自己紹介関数、引数 opponent には相手の名前を入れる
    def introduction(self,opponent):
        print("私の名前は" + self.name + "。よろしくね" + opponent + "さん。")
 
# クラス「魔道士」（Playerを継承）
class Mage(Player): 
    def introduction(self,opponent): # 自己紹介関数をオーバーライド
        print("私の名前は" + self.name + "です。" + opponent + "さん、これからよろしくお願いします！")
 
# クラス「忍者」（Playerを継承）
class Ninja(Player):
    def introduction(self,opponent): # 自己紹介関数をオーバーライド
        print("拙者、" + self.name + "と申す。" + opponent + "殿、よろしくでござる。")
 
 
 
party1 = Player("アルク")   # 冒険者クラス
party2 = Mage("レフィア")   # 魔道士クラス
party3 = Ninja("イングス")  # 忍者クラス
 
# 同じ introduction でも3つの動作が微妙に違う、これがポリモフィズム！
party1.introduction("ルーネス")
party2.introduction("ルーネス") 
party3.introduction("ルーネス") 