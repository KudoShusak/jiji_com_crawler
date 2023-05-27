import re
import requests
import time
from datetime import datetime
import json
from bs4 import BeautifulSoup

# クローリングを開始するURL（Workship MagazineのTOPページ）
start_url = "https://www.jiji.com/"

prefix = '{:%Y%m%d_%H%M%S}_'.format(datetime.now())

# クローリング結果保存ファイル
result_file = f"{prefix}crawlingresult.log"

# テキストデータ保存ファイル
text_file = f"{prefix}textdata.log"

# 大抵の記事ページはこちらでテキスト抽出
# urlに、"/jc/article?" または "/jc/v8?" を含むページに対応
# 非対応："/jc/market?", "/jc/p?"
# （v6はクイズ, v7はarticleへのリンク, v4はv8へのリンク）
# 入力：BeautifulSoupでパースしたjiji.comのhtml1ページ分
# 出力：１、２のリスト
# 　１：ニュース本文のタイトル<h1>段落タイトル<h2>本文<p>のリスト
# 　２：１からタグを除いたテキストデータのリスト
def gettext_article(jijisoup):

    txthtmllist = []
    txtlist = []

    title = jijisoup.find(class_="ArticleTitle").find("h1")
    #print(title)
    txthtmllist.append(title)
    txtlist.append(title.text)

    element = jijisoup.find("article")
    ArticleText = element.find(class_="ArticleText clearfix")
    figcaptionlist = ArticleText.find_all("figcaption")

    for contents in ArticleText.find_all(['h2','p'], class_=""):
        fig_flg = False
        for figcaptionsrc in figcaptionlist:
            if contents == figcaptionsrc.find("p"):
                fig_flg = True

        if fig_flg != True:
            if contents.find("span") == None and contents.find("i") == None:

                txthtmllist.append(contents)

                # テキストの整形
                # strにキャストして、brタグを改行(\n)に置き換えて、\tを消す
                nobrtxt = str(contents).replace('<br/>','\n').replace('\t','')
                # 他のタグを消すために再度パース
                minisoup = BeautifulSoup(nobrtxt, "html.parser")
                # '\n'で分割して、''以外をリストに格納することで不要な改行のない1行ごとのリストを作成。
                txtlist.extend([s for s in minisoup.text.split('\n') if s != '']) 

    return [txthtmllist,txtlist]


# エンタメ動画ページ用
# urlに、"/jc/ent?" または "/jc/movie?" を含むページに対応
# 入力：BeautifulSoupでパースしたjiji.comのhtml1ページ分
# 出力：１、２のリスト
# 　１：ニュース本文のタイトル<h1>段落タイトル<h2>本文<p>のリスト
# 　２：１からタグを除いたテキストデータのリスト
def gettext_ent(jijisoup):

    txthtmllist = []
    txtlist = []

    title = jijisoup.find(class_="ArticleTitle").find("h1")
    #print(title)
    txthtmllist.append(title)
    txtlist.append(title.text)

    element = jijisoup.find(class_="ArticleText MovieDateArticleText clearfix")

    for contents in element.find_all(['h2','p'], class_=""):

        if contents.find("span") == None and contents.find("a") == None:

            txthtmllist.append(contents)

            # テキストの整形
            # \tを消して、\nで分割し、''以外をリストに格納することで不要な改行のない1行ごとのリストを作成。
            t_list = contents.text.replace('\t','').split('\n')
            txtlist.extend([s for s in t_list if s != ''])

    return [txthtmllist,txtlist]

# d4ページ対応
# urlに、"/jc/d4?" を含むページに対応
# 入力：BeautifulSoupでパースしたjiji.comのhtml1ページ分
# 出力：１、２のリスト
# 　１：ニュース本文のタイトル<h1>段落タイトル<h2>本文<p>のリスト
# 　２：１からタグを除いたテキストデータのリスト

def gettext_d4(jijisoup):
    element = jijisoup.find(class_="MainPhotoText")

    txthtmllist = []
    txtlist = []

    for contents in element.find_all(['h2','p']):

        if contents.find("span") == None and contents.find("a") == None:

            txthtmllist.append(contents)

            # テキストの整形
            # \tを消して、\nで分割し、''以外をリストに格納することで不要な改行のない1行ごとのリストを作成。
            t_list = contents.text.replace('\t','').split('\n')
            txtlist.extend([s for s in t_list if s != ''])

    return [txthtmllist,txtlist]

# save_dataをJSON形式でresult_fileに追記する。
def save_result(save_data, filename=result_file):

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(json.dumps(save_data, ensure_ascii=False) + '\n')
    f.close()

    return

# テキストデータのlistを指定の形式でtext_fileに追記する
def save_text(textlist, filename=text_file):

    jointxt = '\n'.join(textlist)
    save_data = {"text" : jointxt}

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(json.dumps(save_data, ensure_ascii=False) + '\n')
    f.close()

    return

#### クローリング ####

# アクセスするURL(初期値はクローリングを開始するURL)
url = start_url
urllist = [url]

# クロール済みリスト
#crawledlist = ["https:dummy.com"]
crawledlist = []

for i in range(8):
    print(f'{i + 1}段目クローリング開始')

    linklist = []
    # 対象ページのhtml
    for url in urllist:
        #　同じURLを何度もクロールしない
        if url in crawledlist:
            continue

        time.sleep(0.5) # データ取得前に少し待つ

        try:
            html = requests.get(url)
            soup = BeautifulSoup(html.content, "html.parser")

            # 次のループで使うURLの候補として<a>タグのリストをため込む
            linklist.extend(soup.find_all("a"))

            # テキスト抽出
            if "/jc/article?" in url or "/jc/v8?" in url :
                cont_txt = gettext_article(soup)
                cont_save_data = {"url":url, "contents": [str(cont_txt[0]), cont_txt[1]]}
                save_result(cont_save_data, filename = result_file)
                save_text(cont_txt[1], filename = text_file)
                print("article", cont_txt[1]) # 動作確認
            elif "/jc/ent?" in url or "/jc/movie?" in url:
                cont_txt = gettext_ent(soup)
                cont_save_data = {"url":url, "contents": [str(cont_txt[0]), cont_txt[1]]}
                save_result(cont_save_data, filename = result_file)
                save_text(cont_txt[1], filename = text_file)
                print("ent", cont_txt[1]) # 動作確認
            elif "/jc/d4?" in url :
                cont_txt = gettext_d4(soup)
                cont_save_data = {"url":url, "contents": [str(cont_txt[0]), cont_txt[1]]}
                save_result(cont_save_data, filename = result_file)
                save_text(cont_txt[1], filename = text_file)
                print("d4", cont_txt[1]) # 動作確認

        except:
            # 何かエラーが出てもとりあえず続ける
            print(f'Error: {url}')
            continue


    # 使い終わったurllistをクロール済みリストに
    crawledlist.extend(urllist)
    crawledlist = list(set(crawledlist)) # 重複削除

    # 次のループのためのurllistを作る
    urllist = []
    for link in linklist:
        # 取得した<a>タグのリストからURLを抽出
        for url in re.findall('<a.+?href="(.+?)".*?>', str(link)):
            # 先頭が'/'の場合は、"https://www.jiji.com"を先頭に追加して取得
            if url[0] == '/':
                urllist.append(f"https://www.jiji.com{url}")
            # jiji.com 又は、jiji.co.jp であることを期待して"jiji.co"のあるURLを取得
            if "jiji.co" in url:
                urllist.append(url)

    urllist = list(set(urllist)) # 重複削除
