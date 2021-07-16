from _base import * 
import unicodedata

def norm(text):
    return unicodedata.normalize('NFKC', text)
    
def create():
    category_master_path = f'{project_root}/data/mst_categories.csv'
    keyword_master_path = f'{project_root}/data/mst_keywords.csv'


    category_master = []
    categories = [
        '不祥事, 体制変更, デジタル, 事業環境, マーケティング, ソーシャル'.split(', '),
        ['ニューノーマル'],
        ['凸版リリース']
    ]
    j = 1
    for i in range(len(categories)):
        for category in categories[i]:
            category_master.append((j, category, i+1, j))
            j += 1

    category_master = pd.DataFrame(category_master, columns=['category_id', 'category_name', 'category_kind', 'sort_no'])
    for col in ['created_user_id', 'updated_user_id', 'created_at', 'updated_at', 'deleted_at']:
        category_master[col] = np.nan 
    category_master.to_csv(category_master_path, index=False, quoting=csv.QUOTE_NONNUMERIC)
    print(category_master)


    category_keywords = {
        '不祥事': 'リコール、製品回収、製品不良、不祥事、損害賠償、謝罪、謝罪会見、偽装、不正、不正取引、製品事故、PL法、談合、偽造、偽物、個人情報、顧客情報、情報流出、サイバー攻撃、誤送信、営業停止、脱法、情報漏洩、脆弱性',
        '体制変更': '新会社、新工場、新組織、新体制、体制変更、統合、上場、資本、提携、買収、M&A、株式化、IPO、TOB、就任、退任', 
        'デジタル': 'DX、AI、5G、ロボット、イノベーション、挑戦、RPA、ビックデータ、XR、シェアリング、サブスク、ポピュリズム',
        '事業環境': '景気、日銀短観、規制、制度変更、ガイドライン、為替、関税',
        'マーケティング': '新商品、新サービス、創刊、リニューアル、新発売、新店舗、開店、新機能、価格改定、マイナーチェンジ、セールスプロモーション、ＴＶＣＭ、企業イベント、ＰＲ、CRM、商標、ロゴ、閉店、販売促進、店頭、社名変更',
        'ソーシャル': 'エネルギー、通信、教育、医療、エコ、温暖化、持続可能、SDGs',
        'ニューノーマル': '遠隔、リモート、バーチャル、オンライン、非接触、非対面、テレワーク、リモートワーク'
    }
    
    category_master = pd.read_csv(category_master_path)
    category_number = dict(zip(category_master['category_name'], category_master['category_id']))
    


    keyword_master = []
    j = 1
    for category, keywords in category_keywords.items():
        keywords = keywords.split('、')
        keywords = list(map(norm, keywords))
        category_id = category_number[category]
        k = 1
        for keyword in keywords:
            keyword_master.append((j, keyword, category_id, k))
            j += 1
            k += 1
    keyword_master = pd.DataFrame(keyword_master, columns=['keyword_id', 'keyword', 'category_id', 'sort_no'])
    for col in ['created_user_id', 'updated_user_id', 'created_at', 'updated_at', 'deleted_at']:
        keyword_master[col] = np.nan 
    keyword_master.to_csv(keyword_master_path, index=False, quoting=csv.QUOTE_NONNUMERIC)
    print(keyword_master)




    '''
    ここからは mst_gen_categories, mst_gen_keywords
    '''
    category_master_path = f'{project_root}/data/mst_gen_categories.csv'
    keyword_master_path = f'{project_root}/data/mst_gen_keywords.csv'


    category_master = []
    categories = [
        'スポーツ, 政治, 社会, 文化, 天気, 経済, 国際, 技術, 宣伝'.split(', ')
    ]
    j = 1
    for i in range(len(categories)):
        for category in categories[i]:
            category_master.append((j, category, i, j))
            j += 1

    category_master = pd.DataFrame(category_master, columns=['category_id', 'category_name', 'category_kind', 'sort_no'])
    for col in ['created_user_id', 'updated_user_id', 'created_at', 'updated_at', 'deleted_at']:
        category_master[col] = np.nan 
    category_master.to_csv(category_master_path, index=False, quoting=csv.QUOTE_NONNUMERIC)
    print(category_master)


    category_keywords = {
        'スポーツ': [
            'Ｊ１','Ｊ２','Ｊ3','J１','J2','J3','サッカー','フィギュア','ラグビー','柔道','トライアスロン',
            '剣道','ゴルフ','テニス','相撲','バロンドール','五輪', 'オリンピック', '世界選手権','国体','競泳','体操',
            'ボクシング','野球','大リーグ','バドミントン','クライミング','スポーツ','野手','投手','卓球', '連勝', '優勝',
            '勝利', '敗北', '点差', '失点'
        ],
        '政治': [
            '関税','政府','自民党','自民','安倍首相','安倍','石破','米軍','米国務長官','トランプ','プーチン',
            '国民民主党','国民投票','国会','軍拡','平和条約','投票','総裁選','知事','首相','与党','野党', '議員', '参院', '衆院'
        ],
        '社会': [
            '社説','殺害','事件','逮捕','新幹線','地震','災害','事故','自殺','拳銃','ハリケーン','通報','首脳','議員',
            '豚コレラ','被災地','調査','西日本豪雨','海洋汚染','医療','患者','死亡','関空連絡橋','地裁','神戸市','大阪市',
            'サマータイム','プログラミング学習','社会','パナマ文書','ふるさと納税','起訴','女性差別','原子力','原発',
            '難民','残業','国交省 ','国交省'
        ],
        '文化': [
            '安室','俳優','出産','育児','余録','おかず','猫と','グレーヘア','ツーリズム','バンド','アイドル','料理法','文学',
            '文化','映画','将棋', '囲碁','死去','訃報','傑作','女流本因坊','栄養士'
        ],
        '天気': [
            '天気予報','天気','猛暑','酷暑','暖冬','台風','豪雨','雨','傘'
        ],
        '経済': [
            '株主総会','経団連','NISA','日産','トヨタ','企業','経済','事業','丸紅','金融','スタートアップ',
            'アップル','マリオット', 'アマゾン','武田薬品','ファーウェイ','三菱重工','景気','経産省','マイクロソフト','仮想通貨'
        ],
        '国際': [
            '国際','米軍','米国務長官','トランプ','プーチン','中国','EU','ＥＵ','世界','ＦＲＢ','台湾','ガーナ','アメリカ','欧州',
            '米政府','米国','香港', '関税','ロシア','ＩＷＣ','下院','パナマ文書','独与党','米中貿易','難民','インド', '北朝鮮',
            'ベラルーシ', 'シリア', ' 韓国'
        ],
        '技術': [
            'デザインツール','AI','研究','遺伝子','マイクロスコープ','技術','３Ｄプリンタ','スマートウォッチ','ビットコイン',
            '人工知能','ロケット','ロボット', '科学','オープンソース','感情推定'
        ], 
        '宣伝': [
            '番組','文化放送','紹介する','見られた映像','ライブ','イベント', '好評発売中'
        ]
    }
    
    category_master = pd.read_csv(category_master_path)
    category_number = dict(zip(category_master['category_name'], category_master['category_id']))
    
    keyword_master = []
    j = 1
    for category, keywords in category_keywords.items():
        # keywords = keywords.split('、')
        keywords = list(map(norm, keywords))
        category_id = category_number[category]
        k = 1
        for keyword in keywords:
            keyword_master.append((j, keyword, category_id, k))
            j += 1
            k += 1
    keyword_master = pd.DataFrame(keyword_master, columns=['keyword_id', 'keyword', 'category_id', 'sort_no'])
    for col in ['created_user_id', 'updated_user_id', 'created_at', 'updated_at', 'deleted_at']:
        keyword_master[col] = np.nan 
    keyword_master.to_csv(keyword_master_path, index=False, quoting=csv.QUOTE_NONNUMERIC)
    print(keyword_master)


    

if __name__ == '__main__':
    create()