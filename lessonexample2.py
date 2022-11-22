class Player(): 
    def __init__(self,name,level,hp,mp,attack,defence):
        self.name      = name    # 名前
        self.level     = level   # レベル
        self.maxhp     = hp      # 最大HP
        self.hp        = hp      # 現在HP
        self.maxmp     = mp      # 最大MP
        self.mp        = mp      # 現在MP
        self.attack    = attack  # 攻撃力
        self.defence   = defence # 防御力
    # ステータス情報
    def disp_info(self):
        print("-----ステータス情報-----")
        print("名前: %s" % self.name)
        print("Level: %2d" % self.level)
        print("HP: %3d/%3d" % (self.hp,self.maxhp))
        print("MP: %3d/%3d" % (self.mp,self.maxmp))
        print("攻撃力:%3d" % self.attack)
        print("防御力:%3d" % self.defence)
 
         
# 黒魔道士クラス（サブクラス）
# スーパークラスである冒険者クラスを継承
class BlackMage(Player): # 継承するクラスは括弧内 () に書く 
    # costだけMPを消費して魔法を唱えて（爆発させる）メソッド
    def use_magic(self,cost):
        if cost > self.mp:
            print("MPが足りない！")
        else:
            self.mp -= cost # MP消費
            print("MPを%d消費して魔法を唱えた！(残りMP:%d)" % (cost,self.mp))
            print("あたり一面で爆発が起こった！")
    # ※コンストラクタ（__init__関数）も継承されるので書かなくてOK（そのまま使う場合は）
 
party2 = BlackMage("るか",12,45,30,30,25) # Player(冒険者)クラスを継承しているので、__init__ もPlayerクラスのものを使える（もう1回書かなくてもOK）
party2.disp_info()  # Player(冒険者)クラスを継承しているので、Playerクラスのメソッドを使える
party2.use_magic(3) # Mageクラスで新たに定義したメソッドを利用