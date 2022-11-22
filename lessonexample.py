class Player(): # クラス「冒険者（プレイヤー）」
    def __init__(self,name,level,hp,mp,attack,defence):
        self.__name      = name    # 名前
        self.__level     = level   # レベル
        self.__maxhp     = hp      # 最大HP
        self.__hp        = hp      # 現在HP
        self.__maxmp     = mp      # 最大MP
        self.__mp        = mp      # 現在MP
        self.__attack    = attack  # 攻撃力
        self.__defence   = defence # 防御力
    # ステータス情報
    def disp_info(self):
        print("-----ステータス情報-----")
        print("名前: %s" % self.__name)
        print("Level: %2d" % self.__level)
        print("HP: %3d/%3d" % (self.__hp,self.__maxhp))
        print("MP: %3d/%3d" % (self.__mp,self.__maxmp))
        print("攻撃力:%3d" % self.__attack)
        print("防御力:%3d" % self.__defence)
    # メソッドも __（アンダーバー2つ）付けると外部からは見えなくなる
    def __debug(self,hp):
        self.__hp = hp 
 
 
         
# カプセル化された状態
party1 = Player("ももやま",10,50,20,40,30) 
party1.disp_info() # メソッドからであれば __ (アンダーバー2つ)付いた変数にアクセスできる